import smtplib  # permite crear smtp server
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar a os.path

# template obj con html leido como str
html = Template(Path('index.html').read_text())
body = html.substitute({'name': 'yourname'})

email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'email'
email['subject'] = 'this is a test'

email.set_content(body, 'html')  # body

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@gmail.com', 'pwd')
    smtp.send_message(email)
    print('all good')
