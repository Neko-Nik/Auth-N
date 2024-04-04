"""
The Email module should be used to send the password reset link or any other email related tasks
Should have the following functions:
    - send_email: Send an email to the list of recipients with the subject and body (Use this as internal function for other email functions)
    - send_password_reset_email: Send a password reset email to the user
    - send_verification_email: Send a verification email to the user
    - send_welcome_email: Send a welcome email to the user
    - send_notification_email: Send a notification email to the user
    - send_error_email: Send an error email to the admin
"""

from .email_verification import send_verification_email, verify_otp_for_user_email


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "send_verification_email": "Send a verification email to the user",
    "verify_otp_for_user_email": "Verify the OTP for the user email"
}


__all__ = [
    "send_verification_email",
    "verify_otp_for_user_email"
]
