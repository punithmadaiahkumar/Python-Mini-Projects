# Send Email from CSV
This project contains a simple bulk email script
which sends the same message to a list of recipients.


### Tech Stack:
+ Python

### Libraries:
+ smtplib
+ email

### To execute the project/play:
+ Run `pip install -r requirements.txt`
+ `mails.csv` should contain the email addresses to send the message to.
+ `credentials.txt` should contain your SMTP server login credentials, with your user name and your password on sepate lines, with no additional whitespace or other decorations.
+ Execute `python3 send_mail.py`

### Development ideas:

+ A proper email sender would use `Cc:` or `Bcc:` and send the same message just once.

+ Don't play frivolously with this; your email provider, and/or the recipient's, may have automatic filters which quickly block anyone who sends multiple identical messages.

+ The script simply hardcodes the conventions for Gmail only. Other providers may use a different port number and authentication regime.
