import smtplib
from email.message import EmailMessage
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


SMTP_SERVER = 'smtp.gmail.com'


class Mailer(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send(self, recipient_address, content):
        smtp_client = self.setting_client()
        msg = self.create_content(recipient_address, content)
        smtp_client.send_message(msg)
        logger.debug({
            'action': 'send',
            'message': msg
        })
        smtp_client.quit()

    def create_content(self, recipient_address, content):
        msg = EmailMessage()
        msg.set_content(str(content))
        msg['Subject'] = 'Subject'
        msg['From'] = self.username
        msg['To'] = recipient_address
        return msg

    def setting_client(self):
        smtp_client = smtplib.SMTP_SSL(host=SMTP_SERVER)
        smtp_client.set_debuglevel(1)
        smtp_client.login(user=self.username, password=self.password)
        return smtp_client


if __name__ == '__main__':
    pass
