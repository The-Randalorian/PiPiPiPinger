# Rename this file to config.py and change the settings below

# E-Mail Settings
port = 465  # For SSL
smtp_server = "smtp.sample.com"  # Enter the address of the smtp server
sender_email = "sender@sample.com"  # Enter your address
receiver_emails = "receiver1@sample.com, receiver2@sample.com"  # Enter receiver addresses separated by ", "
password = "samplepassword123"  # password for the email server
alert_message = """\
Subject: Device Unreachable

The device is currently unable to be reached.
"""  # Message to send when the device cannot be reached
clear_message = """\
Subject: Device Now Reachable

The device is now able to be reached.
"""  # Message to send when the device can be reached again

# Ping Settings
target = "127.0.0.1"  # IP of the device
delay = 300  # time to wait between pings
threshold = 0.8  # what ratio of pings must fail for the device to be considered unreachable

# Error settings
error_receiver_emails = "error@sample.com"
error_delay = 60
error_block = 12 * 60 * 60 / error_delay  # sends an email every 12 hours
error_threshold = 2
