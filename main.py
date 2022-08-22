import smtplib
import ssl
import time
import traceback

import pythonping

from config import *


def send_alert():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, alert_message)


def send_clear():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, clear_message)


def send_error(tb):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, error_receiver_emails, f"""\
Subject: Error in Monitoring Application

An error occurred in a monitoring application monitoring device {target}. More details are provided below.

{tb}
""")


if __name__ == '__main__':
    error_count = 0
    while True:
        # noinspection PyBroadException
        try:
            out = pythonping.ping(target)
            # print(out.packet_loss)
            if out.packet_loss > threshold:
                send_alert()
                while out.packet_loss > threshold:
                    time.sleep(delay)
                    out = pythonping.ping(target, count=10)
                send_clear()
            time.sleep(delay)
            error_count = max(0, error_count - 1)  # decrement error count when succeeding
        except Exception:
            if error_count >= error_threshold and (error_count - error_threshold) % error_block == 0:
                tb = traceback.format_exc()
                traceback.print_exc()
                send_error(tb)
            time.sleep(error_delay)
            error_count += 1
