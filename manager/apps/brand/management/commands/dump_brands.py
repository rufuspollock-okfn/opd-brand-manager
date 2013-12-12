from django.core.management.base import BaseCommand, CommandError
from manager.apps.brand.models import Brand
from manager.libs.snippets.csv_unicode_writer import UnicodeWriter
from django.core.files.storage import default_storage as storage


class Command(BaseCommand):
    args = ''
    help = "Dump brand informations default 'dumps/latest.csv' path."

    def handle(self, *args, **options):
        try:
            with storage.open('dumps/latest.csv', 'w') as fp:
                writer = UnicodeWriter(fp)
                brand_list = Brand.dumpable_list()
                writer.writerows(brand_list)
                fp.close()
        except Exception, e:
            raise CommandError('Error while dumping brands: %s' % e.strerror)

        self.stdout.write('Successfully dumped %d brands.' % len(brand_list))
