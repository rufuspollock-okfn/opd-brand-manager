from django.core.mail import send_mail
from django.core.urlresolvers import reverse


class EmailNotification:

    msg_from = 'OKFN team <noreply@okfn.org>'

    def __init__(self, msg_to, msg_from=None):
        self.msg_to = msg_to
        if msg_from:
            self.msg_from = msg_from

    def send_mail(self, subject, message):
        send_mail(subject, message, self.msg_from, [self.msg_to],
                  fail_silently=True)

    def create_notification(self, brand_nm, bsin):
        brand_url = reverse('brand', args=(bsin,))
        subject = "%s added to the OKFN brand repository" % brand_nm
        message = """Dear contributor,

Your brand %s was added to the OKFN brand respository under BSIN %s.
More details at http://product.okfn.org%s .

Thank you for your contribution.

Regards,
OKFN brand manager team""" % (brand_nm, bsin, brand_url)

        self.send_mail(subject, message)

    def delete_notification(self, brand_nm, comment):
        subject = "%s rejected from OKFN brand repository" % brand_nm
        message = """Dear contributor,

Your brand proposal for %s was rejected from the OKFN brand respository.

Moderator comment : %s

Thank you for your contribution.

Regards,
OKFN brand manager team""" % (brand_nm, comment)

        self.send_mail(subject, message)
