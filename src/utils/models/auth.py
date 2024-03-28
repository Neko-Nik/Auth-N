"""
Schema Models for the User related operations
"""

from src.utils.base.libraries import BaseModel, Field, validator, datetime, EmailStr


class BaseUser(BaseModel):
    """
    User Base model
    """
    user_id: str = Field(..., title="User ID", description="User ID")
    username: str = Field(..., title="Username", description="Username")
    password_hash: str = Field(..., title="Password Hash", description="Password Hash")
    password_salt: str = Field("", title="Password Salt", description="Password Salt")
    email: EmailStr = Field(..., title="Email", description="Email")
    phone_number: str = Field(..., title="Phone Number", description="Phone Number")
    profile_picture_url: str = Field("", title="Profile Picture URL", description="Profile Picture URL")
    last_login: datetime = Field(datetime.now(), title="Last Login", description="Last Login")
    is_active: bool = Field(True, title="Is Active", description="Is Active")
    is_locked: bool = Field(False, title="Is Locked", description="Is Locked")
    lockout_time: datetime = Field(None, title="Lockout Time", description="Lockout Time")
    created_at: datetime = Field(datetime.now(), title="Created At", description="Created At")
    updated_at: datetime = Field(datetime.now(), title="Updated At", description="Updated At")
    password_last_changed: datetime = Field(datetime.now(), title="Password Last Changed", description="Password Last Changed")
    failed_login_attempts: int = Field(0, title="Failed Login Attempts", description="Failed Login Attempts")

    @validator('phone_number')
    def phone_number_validator(cls, phone_number: str):
        """
        Phone number validator
        Example: The phone number should be of country code + phone number
            -> +91 1234567890 | +1 1234567 | +44 123456789
        """
        # Check for country code, if not present, raise an error
        if not phone_number.startswith("+"):
            raise ValueError("Phone number should start with country code indicator (+)")

        country_code, phone_digits = phone_number[1:].split(" ", 1)

        if not country_code.isdigit():
            raise ValueError("Country code should be numeric")

        if len(country_code) < 1 or len(country_code) > 3:
            raise ValueError("Country code should be 1-3 digits long")

        if not phone_digits.isdigit():
            raise ValueError("Phone number should contain only numeric digits")

        # Count the number of appropriate digits
        if len(phone_digits) < 6 or len(phone_digits) > 10:
            raise ValueError("Phone number should be 6-10 digits long")

        return phone_number

    class Config:
        """
        Configuration for the model
        """
        from_attributes = True
        json_schema_extra = {
            "title": "User Model",
            "description": "User model for storing user information",
            "type": "object",
            "example": {
                "user_id": "user_id_has21",
                "username": "username11",
                "email": "nik@nekonik.com",
                "password_hash": "TmVrby1OaWs=",    # Base64 encoded password hash (Neko-Nik)
                "phone_number": "+91 1234567890",
                "profile_picture_url": "https://NekoNik.com",
            }
        }
