import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

class MailingList:
    '''Manage groups of e-mail addresses for sending e-mails.'''

    def __init__(self):
        self.email_map = defaultdict(set)

    def send_email(self, subject, message, from_addr, *to_addrs, host="localhost", port=1025, **headers):
        headers = {} if headers is None else headers
        email = MIMEText(message)
        email['Subject'] = subject
        email['From'] = from_addr

        for header, value in headers.items():
            email[header] = value

        sender = smtplib.SMTP(host, port)

        for addr in to_addrs:
            del email['To']
            email['To'] = addr
            sender.sendmail(from_addr, addr, email.as_string())
        sender.quit()

    def add_to_group(self, email, group):
        self.email_map[email].add(group)
    
    def emails_in_groups(self, *groups):
        groups = set(groups)
        emails_in_groups_list = []
        
        for email, group in self.email_map.items():
            if group.intersection(groups):
                emails_in_groups_list.append(email)

        return emails_in_groups_list
    
    def send_mailing(self, subject, message, from_addr, *groups, **kwargs):
        emails_by_groups = self.emails_in_groups(*groups)
        self.send_email(subject, message, from_addr, *emails_by_groups)


mailing_list = MailingList()
mailing_list.add_to_group("diegofelipe.moreno@gmail.com", "office")
mailing_list.add_to_group("to2@example.com", "home")
mailing_list.add_to_group("to3@example.com", "home")
mailing_list.add_to_group("to4@example.com", "friends")
mailing_list.add_to_group("to5@example.com", "family")
mailing_list.send_mailing("A model subject", "The message contents", "from@example.com", "office", "home", "home")
mailing_list.send_mailing("A Party", "Friends and family only: a party", "me@example.com", "friends", "family", headers={"Reply-To": "me2@example.com"})

#oso = mailing_list.emails_in_groups("office", "home", "home")
#print(oso)
