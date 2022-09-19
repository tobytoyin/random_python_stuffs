from __future__ import annotations
import datetime as dt
from dataclasses import dataclass, field

# NOTE -
# Create a subscription dictionary to store all possible events
# This allows external class to use this dictionary to call function
# rather than having direct dependency with another class

# In general, a pub-sub approach do the following:
# 1. the Handler class generate a subscription by putting its functional entry point
# 2. the Publisher/ users pick the subscribed function from the dictionary and pass in data
# 3. the Subscribers invoke the function using the data
# 4. the function triggers the logics stored within the Handler

subs = dict()


def subscribe(event_type: str, fn):
    """
    `subscribe` creates callback functions into `subs` that allow
        future users to invoke them later
    """
    if not event_type in subs:
        subs[event_type] = []
    subs[event_type].append(fn)


def unsubscribe(event_type: str):
    """
    Tear down callback functions and making it non-invokable
    """
    if not event_type in subs:
        return
    del subs[event_type]


def post_event(event_type: str, data):
    """
    Allow other users to invoke the functions with data,
        without having to create an explicit dependency to another class
    """
    if not event_type in subs:
        return

    for fn in subs[event_type]:
        fn(data)


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

    def send_mail_event(self, post_office_id):
        # NOTE - Sending mails become a publication of a new event,
        # This allows us to invoke a function that is being subscribed
        #   without having to know what class that function belongs to

        post_event(f'post_mail_{post_office_id}', self)
        return


@dataclass
class PostOffice:
    post_office_loc_id: str
    delivery_queue: list[Mail] = field(default_factory=lambda: [])

    def start_post_office(self):
        subscribe(f'post_mail_{self.post_office_loc_id}', self.process_mail)

    def close_post_office(self):
        unsubscribe(f'post_mail_{self.post_office_loc_id}')

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

    def process_mail(self, mail):
        # NOTE - Instead of handling a queue by invoke itself.
        # The subscribers have the freedom to control when this can be invoked
        #   thus leaving out the needs to manually trigger this class again and again

        self._perform_address_check(mail)
        self._add_mail_tracking(mail)
        self._add_to_delivery_queue(mail)
        return


if __name__ == '__main__':
    post_office = PostOffice(post_office_loc_id='small-town-office-0')
    post_office.start_post_office()

    # someone send a mail and post it to the post office
    new_mail = Mail(address='my friend address', return_address='my address', postal_amount=0.6)
    new_mail.send_mail_event('small-town-office-0')

    invalid_mail = Mail(address='address 1888 road', return_address='231 Road', postal_amount=0)
    invalid_mail.send_mail_event('small-town-office-0')

    # some late mails
    post_office.close_post_office()

    late_mail = Mail(address='29999 Road', return_address='None', postal_amount=1.2)
    late_mail.send_mail_event('small-town-office-0')
