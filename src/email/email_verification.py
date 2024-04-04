"""
This will send the email verification link to the given user_id and automatically generate the verification link
"""

from src.utils.base.libraries import Session, datetime, timedelta, timezone, random
from src.utils.models import Error
from .handlers.service import send_mail_to_recipients
from src.utils.base.constants import EMAIL_RELATED_ERROR_MESSAGES, EMAIL_TEMPLATES
from src.database import get_user_by_user_id, add_new_otp_to_user, validate_otp_and_update_verification_flag


def generate_random_otp() -> str:
    """
    Generate a random OTP
    return: str: Random OTP
    """
    return str(random.randint(100000, 999999))


def send_verification_email(session: Session, user_id: str) -> str | Error:
    """
    Send a verification email to the user
    Usecase: Send an email to the user for email verification or password reset
    param: session: str: Email address of the recipient
    param: verification_link: str: Verification link
    """
    user = get_user_by_user_id(db=session, user_id=user_id)
    if isinstance(user, Error):
        return user

    if user.is_email_verified:
        return Error(**EMAIL_RELATED_ERROR_MESSAGES["email_already_verified"])

    # Generate a random OTP
    otp = generate_random_otp()
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=15)
    add_new_otp_to_user(db=session, user_id=user_id, otp=otp, expiration_time=expiration_time)

    send_mail_to_recipients(to_emails=[user.email], subject=EMAIL_TEMPLATES["email_verification"]["subject"], body=EMAIL_TEMPLATES["email_verification"]["body"].format(verification_otp=otp))

    return "Email sent successfully"

    
def verify_otp_for_user_email(session: Session, user_id: str, otp: str) -> str | Error:
    """
    Verify the email address of the user
    Same can be used to any kind of verification process not just email
    param: user_id: str: User ID
    param: otp: str: OTP entered by the user
    return: None
    """
    user = get_user_by_user_id(db=session, user_id=user_id)
    if isinstance(user, Error):
        return user
    
    val_otp = validate_otp_and_update_verification_flag(db=session, user_id=user_id, otp=otp)
    if isinstance(val_otp, Error):
        return val_otp

    return "Email verified successfully"
