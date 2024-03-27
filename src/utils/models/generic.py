"""
This module contains the basic models for the application
"""


class All_Exceptions(Exception):
    """Class for handling wrong input exceptions"""
    def __init__(self , message: str , status_code: int):
        self.message = message
        self.status_code = status_code
