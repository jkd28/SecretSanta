import random
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

IS_DEBUG = True
MY_EMAIL = "abcdef@gmail.com"  # the one running the code should supply their email here
MY_PASSWORD = ""  # password associated with the gmail account above. Don't commit this with the value saved
EMAIL_SUBJECT = ""


email_mappings = {
    # key:value pairs in the form of "name:email_address"
}


santas = [
    # a list of names that should match the keys from above email_mappings
]


# We don't want to print some details on every run, since the one running the code would see all the pairings!
def print_if_debug(msg):
    if IS_DEBUG:
        print(msg)


def get_pairs():
    choose = santas.copy()
    result = []
    for name in santas:
        print_if_debug("Processing for {}".format(name))
        names = santas.copy()
        names.pop(names.index(name))
        chosen = random.choice(list(set(choose) & set(names)))
        result.append((name, chosen))
        choose.pop(choose.index(chosen))
    return result


pairings = []
pairs_created = False
while not pairs_created:
    try:
        pairings = get_pairs()
        print_if_debug(pairings)
        pairs_created = True
        break
    except IndexError:
        print("INVALID PAIRS, TRYING AGAIN")


port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(MY_EMAIL, MY_PASSWORD)

    for gift_giver, gift_receiver in pairings:
        print("Sending for {}".format(gift_giver))

        # create fresh message object for every giver, otherwise weirdness ensues
        message = MIMEMultipart("alternative")
        message["Subject"] = EMAIL_SUBJECT
        message["From"] = MY_EMAIL

        gift_giver_email = email_mappings[gift_giver]
        message["To"] = gift_giver_email
        print_if_debug("Giver: {}({})\tGiftee: {}".format(gift_giver, gift_giver_email, gift_receiver))

        email_text = """\
        Hey there {},

        You'll be giving to {} this year!
        Happy Holidays?
        """.format(gift_giver, gift_receiver)
        message.attach(MIMEText(email_text, "plain"))

        print_if_debug(message)
        server.sendmail(MY_EMAIL, gift_giver_email, message.as_string())
