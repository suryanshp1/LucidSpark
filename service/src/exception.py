import sys


def error_message_detail(message, errors: sys):
    _, _, exc_tb = errors.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occured in python script name {file_name} line number {exc_tb.tb_lineno} | Error Message : {str(message)}"

    return error_message


class CustomException(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = error_message_detail(message=message, errors=errors)
