"""
This module contains all the API objects used in the application
"""

from src.utils.base.libraries import BaseModel, Field, validator, datetime


class DigestEmailData(BaseModel):
    """
    Digest Email data model, used for storing email data
    url_hash: Hash of the URL of the email encoded data, used as primary key (will be generated later, so optional)
    euid: Email unique id
    from_: Email from address
    to_recipients: List of email to addresses
    date: Date of the email object
    subject: Email subject
    spam_reason: Spam reason of the email
    release_history: Release history of the email (will be added later, so optional)
    is_digested: Is digested or not (will be added later, so optional)
    """
    url_hash: str = Field("/", title="URL Hash", description="Hash of the URL of the email encoded data, used as primary key (will be generated later, so optional)")
    euid: str = Field(..., title="Email Unique ID", description="Email unique id")
    from_: str = Field(..., title="Email From Address", description="Email from address")
    to_recipients: list = Field(..., title="Email To Addresses", description="List of email to addresses")
    date: datetime = Field(..., title="Email Date", description="Date of the email")
    subject: str = Field(..., title="Email Subject", description="Email subject")
    spam_reason: str = Field(..., title="Email Spam Reason", description="Email spam reason")
    release_history: str = Field('None', title="Email Release History", description="Email release history (will be added later, so optional)")
    is_digested: bool = Field(False, title="Is Digested", description="Is digested or not (will be added later, so optional)")

    class Config:
        """
        Configuration for the model
        """
        schema_extra = {
            "example": {
                "url_hash": "https://example.com",
                "euid": "123456789",
                "from_": "test@test.com",
                "to_recipients": ["test@test.com"],
                "date": "2021-01-01:00:00:00",
                "subject": "Test Subject",
                "spam_reason": "Test Spam Reason",
                "release_history": '{"ip": "192.168.1.1", "date": "2021-01-02:10:10:10"}',
                "is_digested": False
            }
        }


class Error(BaseModel):
    """
    Error model for API, if any error occurs, this model is returned
    Error message and status code is returned
    message: Error message
    status_code: Error status code
    """
    message: str = Field(..., title="Message", description="Error message")
    status_code: int = Field(..., title="Status Code", description="Error status code")

    @validator('status_code')
    def status_code_must_be_in_range(cls, v):
        """
        Status code must be in range 100 to 599
        """
        if v < 100 or v > 599:
            raise ValueError('status code must be in range 100 to 599')
        return v

    class Config:
        """
        Configuration for the model
        """
        schema_extra = {
            "example": {
                "message": "Error message",
                "status_code": 400
            }
        }
