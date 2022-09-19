from __future__ import annotations
import datetime as dt
from dataclasses import dataclass, field


@dataclass
class MailTracker:
    id: str
    current_location: str
    target_location: str

    def __repr__(self) -> str:
        return f"""
    ===== Tracker =====
    id : {self.id}
    loc: {self.target_location}
    ===================
    """


@dataclass
class Mail:
    address: str
    return_address: str
    postal_amount: float

    tracker: MailTracker = None
    valid: bool = False

    def __repr__(self):
        return f"""
    ===== Mail =====
    address: {self.address}
    postage: {self.postal_amount}
    return : {self.return_address}
    ================
    """

    def send_mail(self, post_office: PostOffice):
        post_office.post_mail(self)
        return


@dataclass
class PostOffice:
    post_office_loc_id: str
    postal_queue: list[Mail] = field(default_factory=lambda: [])
    delivery_queue: list[Mail] = field(default_factory=lambda: [])

    def post_mail(self, mail: Mail):
        self.postal_queue.insert(-1, mail)

    def _perform_address_check(self, mail: Mail):
        print(f">> checking mail")
        print(mail)
        if mail.address and mail.postal_amount > 0.5:
            mail.valid = True
        return mail

    def _add_mail_tracking(self, mail: Mail):
        print(f">> Adding tracking on Mail")

        target_location = mail.address if mail.valid else mail.return_address

        new_tracker = MailTracker(
            id=dt.datetime.now().strftime("%Y%d%m%H%M%S%f"),
            current_location=self.post_office_loc_id,
            target_location=target_location,
        )

        mail.tracker = new_tracker
        return mail

    def _add_to_delivery_queue(self, mail: Mail):
        print(">> Prepare delivery")
        print(mail.tracker)
        self.delivery_queue.append(mail)
        return

    def process_mails(self):
        while self.postal_queue:
            print('-' * 30)
            mail = self.postal_queue.pop()

            self._perform_address_check(mail)
            self._add_mail_tracking(mail)
            self._add_to_delivery_queue(mail)

        return


if __name__ == '__main__':
    post_office = PostOffice(post_office_loc_id='small-town-office-0')

    # someone send a mail and post it to the post office
    new_mail = Mail(address='my friend address', return_address='my address', postal_amount=0.6)
    new_mail.send_mail(post_office)

    invalid_mail = Mail(address='address 1888 road', return_address='231 Road', postal_amount=0)
    invalid_mail.send_mail(post_office)

    # post office process the mail
    post_office.process_mails()
