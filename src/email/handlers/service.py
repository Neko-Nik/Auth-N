"""
Handles all the Email related tasks
"""


from src.utils.base.libraries import smtplib, logging
from src.utils import retry
from src.utils.base.constants import EMAIL_CONFIG


@retry(exceptions=Exception, total_tries=3, initial_wait=0.5, backoff_factor=2, logger=logging)
def send_mail_to_recipients(to_emails: list[str], subject: str, body: str) -> None:
    """
    Send an email to the list of recipients with the subject and body
    param: to_emails: list[str]: List of email addresses of the recipients
    param: subject: str: Subject of the email
    param: body: str: Body of the email
    return: None
    """
    with smtplib.SMTP(host=EMAIL_CONFIG["smtp_server"], port=EMAIL_CONFIG["port"]) as server:
        server.starttls()
        server.login(user=EMAIL_CONFIG["user_name"], password=EMAIL_CONFIG["password"])
        for email in to_emails:
            server.sendmail(from_addr=EMAIL_CONFIG["from_email"], to_addrs=email, msg=f"Subject: {subject}\n\n{body}")

