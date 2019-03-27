import json
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# read_mail_config reads user email and password from config.json.
def read_mail_config():
    with open('core/smtp/config.json') as conf:
        c = conf.read()
    return json.loads(c)


# send_pokemon sends a random pokemon to the list of subscribers.
def send_pokemon(pokemon, image, users):
    # Create the SMTP client that will send pokemail.
    conf_obj = read_mail_config()

    sender_email = conf_obj['email']
    receiver_email = "luke.brady@ung.edu"
    password = conf_obj['password']

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    html = """\
    <html>
      <body>
        <h3>A wild {}{} has appeared.</h3>
        <img src = "{}"/>
      </body>
    </html>
    """.format(str(pokemon[0]).upper(), pokemon[1:], image)

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
