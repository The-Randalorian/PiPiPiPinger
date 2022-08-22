# Rename this file to config.py and change the settings below

# E-Mail Settings
port = 465  # For SSL
smtp_server = "smtp.sample.com"
sender_email = "sender@sample.com"  # Enter your address
receiver_emails = "receiver1@sample.com, receiver2@sample.com"  # Enter receiver addresses separated by ", "
password = "samplepassword123"
alert_message = """\
Subject: Device Unreachable

The device is currently unable to be reached.
"""
clear_message = """\
Subject: Device Now Reachable

The device is now able to be reached.
"""

# Ping Settings
target = "127.0.0.1"
delay = 300
threshold = 0.8

# Error settings
error_receiver_emails = "error@sample.com"
error_delay = 60
error_block = 12 * 60 * 60 / error_delay  # sends an email every 12 hours
error_threshold = 2
