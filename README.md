# Secret Santa Script

The following script is a simple script to create a Secret Santa draw.
The conditions of this Secret Santa are that two people cannot be eachothers Secret Santa, instead
the draw is distributed as a cyclic list.

In order to run the script you need to perform two steps:

1. Create a copy of the `config.ini.template` called `config.ini` and
   fill in the values of your email address, as well as the names and email
   addresses of the participants of the Secret Santa. In order to allow this
   program to send an email from your email account, you need to provide an `app_password` or token
   which has access to your account. Instructions on how to generate an app password for a Gmail account can be found [here](https://support.google.com/mail/answer/185833?hl=en).
   Note that each participant name must uniquely identify the particpant, so if you have two participants with the same name, make sure you use different names in the config to identify them.

2. Once you have finished filling out the config file, simply run
   `python secret_santa.py` from your command line.
