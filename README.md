## Secret Santa Email Generator
A very basic secret santa pairing generator, using GMAIL smtp. 

The code isn't production level, but then again, is it ever?

Usage: `> python secretsanta.py`  
Easy enough, right? Just be sure to populate the variables at the top to make sure it doesn't explode:
```
MY_EMAIL = "abcdef@gmail.com"  # the one running the code should supply their email here
MY_PASSWORD = ""  # password associated with the gmail account above. Don't commit this with the value saved
EMAIL_SUBJECT = ""
```
If you have 2FA setup on your GMAIL account, there will probably be some issues with authentication. You'll have to go here: https://support.google.com/accounts/answer/185833?hl=en and follow the directions for creating an App-specific password for mail.