"""
Schema Models for the User related operations
"""

from src.utils.base.libraries import BaseModel, Field, validator, datetime, EmailStr


class BaseUser(BaseModel):
    """
    User Base model
    """
    user_id: str = Field("", title="User ID", description="User ID")
    username: str = Field(..., title="Username", description="Username")
    password_hash: str = Field(..., title="Password Hash", description="Password Hash")
    password_salt: str = Field("", title="Password Salt", description="Password Salt")
    email: EmailStr = Field(..., title="Email", description="Email")
    phone_number: str = Field(..., title="Phone Number", description="Phone Number")
    profile_picture_url: str = Field("", title="Profile Picture URL", description="Profile Picture URL")
    is_active: bool = Field(False, title="Is Active", description="Is Active")  # By default, the user will be inactive till verified / activated

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
                "username": "neko_nik",
                "email": "nik@nekonik.com",
                "password_hash": "TmVrby1OaWs=",    # Base64 encoded password hash (Neko-Nik)
                "phone_number": "+91 1234567890",
                "profile_picture_url": "https://www.NekoNik.com"
            }
        }
