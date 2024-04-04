"""
Handles all the database operations related to users
"""

from src.utils.base.libraries import Session, datetime, uuid, timezone
from src.utils.base.constants import EMAIL_RELATED_ERROR_MESSAGES
from src.utils.models import User, Error, OTPToken


def add_new_otp_to_user(db: Session, user_id: str, otp: str, expiration_time: datetime) -> None:
    """
    Add a new OTP to the user
    param: db: Session: Database session
    param: user_id: str: User ID
    param: otp: str: OTP
    param: expiration_time: datetime: Expiration time of the OTP
    return: None
    """
    # Create a new OTP token
    new_otp = OTPToken(
        token_id=uuid.uuid4().hex,
        user_id=user_id,
        token=otp,
        expiration_time=expiration_time
    )

    # Add the new OTP token to the database
    db.add(new_otp)
    db.commit()
    db.refresh(new_otp)
    return None


def validate_otp_and_update_verification_flag(db: Session, user_id: str, otp: str) -> None | Error:
    """
    Validate the OTP entered by the user and update the email_verified flag
    param: db: Session: Database session
    param: user_id: str: User ID
    param: otp: str: OTP entered by the user
    return: None | Error (Error object)
    """
    # Get the OTP token
    otp_token = db.query(OTPToken).filter(OTPToken.user_id == user_id, OTPToken.token == otp).first()

    # Check if the OTP token exists
    if not otp_token:
        return Error(**EMAIL_RELATED_ERROR_MESSAGES["otp_not_found"])

    # Check if the OTP token has expired (compare with offset-naive datetime object)
    expiration_time = otp_token.expiration_time
    current_time = datetime.now(timezone.utc).replace(tzinfo=None)
    if current_time > expiration_time:
        return Error(**EMAIL_RELATED_ERROR_MESSAGES["otp_expired"])

    # TODO: Delete all the OTP tokens for the user instead of just the current one
    db.query(OTPToken).filter(OTPToken.user_id == user_id).delete()

    # Set the is_email_verified flag to True
    db.query(User).filter(User.user_id == user_id).update({"is_email_verified": True})
    db.commit()
    return None
