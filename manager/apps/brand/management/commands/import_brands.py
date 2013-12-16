from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from django.conf import settings
from manager.apps.brand.models import Brand, BrandType
from manager.libs.snippets.http_tools import http_destination_exists
from manager.libs.snippets.csv_unicode_reader import UnicodeReader
from manager.libs.snippets.bsin import BSIN
import urlparse


class Command(BaseCommand):
    args = ''
    help = "Import POD format 'pod.csv' brand informations from current "
    "directory."
    csv_path = 'manager/apps/brand/management/commands/pod.csv'

    def handle(self, *args, **options):
        try:

            # Check brand types, create them if they do not exist
            BrandType.objects.get_or_create(
                brand_type_cd=1, brand_type_nm='Manufacturer-brand')
            BrandType.objects.get_or_create(
                brand_type_cd=2, brand_type_nm='Retailer-brand')

            total_count = 0
            imported_count = 0

            with open(self.csv_path, 'rb') as fp:
                reader = UnicodeReader(fp, delimiter=',', quotechar='"')
                media = urlparse.urlparse(settings.MEDIA_URL)
                for row in reader:
                    try:
                        optional_kwargs = {}
                        BSIN.BSINValidator(row[0])
                        brand_logo = 'brand/logo/%s.jpg' % row[0]
                        if not http_destination_exists(
                                media.netloc, urlparse.urljoin(media.path,
                                                               brand_logo)):
                            print "Brand logo could not be found ( %s )" % \
                                brand_logo
                        else:
                            optional_kwargs['brand_logo'] = brand_logo

                        if row[4] != 'NULL':
                            optional_kwargs['brand_link'] = row[4]

                        created = Brand.objects.get_or_create(
                            bsin=row[0],
                            brand_nm=row[1],
                            brand_type_cd_id=row[3],
                            flag_delete=False,
                            **optional_kwargs
                        )[1]

                        if created:
                            imported_count += 1
                        total_count += 1

                    except ValidationError:
                        # Not a BSIN
                        print "Value is not a BSIN ( %s )" % row[0]
                        pass

        except Exception, e:
            raise CommandError('Error while importing brands: %s' % e.strerror)

        self.stdout.write('Successfully imported %d brands. (%d total)' % (
            imported_count, total_count))
