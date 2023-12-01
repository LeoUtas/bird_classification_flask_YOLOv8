import sys


# ________________ DEF THE ERROR MESSAGE ________________ #
def error_message_detail(error, error_detail: sys):
    """

    This function is to return a message regarding error details occuring in the execution of the code

    Parameters:
    - error (Exception): The error that occurred.
    - error_detail (sys): A reference to the sys module, which is used to obtain traceback information.

    Returns:
    - str: A string containing detailed information about the location and nature of the error that occurred. The string is formatted as follows:
        "Error occurred in the script, name: [{script_name}], line number: [{line_number}] error message: [{error_message}]".

    Note:
        This function uses `sys.exc_info()` to obtain traceback information about the error. The traceback object is used to extract the name of the script and the line number where the error occurred.

    """

    # no interest in the 1st and 2nd items in the return of the exc_info()
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in the script, name: [{0}], line number: [{1}] error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


# ________________ MAKE ERROR CAPTURE HANDLER ________________ #
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
