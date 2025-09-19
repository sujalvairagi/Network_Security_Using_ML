import sys
class NetworkSecurityException(Exception):
    """
    Custom exception class for network security related errors.
    """
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        self.error_details = error_details
        _,_,exc_tb = error_details.exc_info()

        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return "error occured in python script name [{0}] at line number [{1}] error message [{2}]".format(
            self.file_name,
            self.lineno,
            self.error_message
        )

