import sys  # a module that provides various functions and variables that are used to manipulate different oarts of the python runtime environment.
import logging


def error_message_details(error, error_detail:sys): #whenever there's an exception, you want to customize your own error details. The error details here s contained in the sys module.
    _,_,exc_tb = error_detail.exc_info() #this line returns three information to you but we are dealing only with the last information, which returns the error of that exception i.e the file or line number the exce[ption has occured.
    file_name = exc_tb.tb_frame.f_code.co_filename # this gets the filename.
    error_message = "Error occured in python script name [{0}] line number [{1}] , error message:[{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    '''
    This class inherits a function that defines a global error message 
    of the filename, lin number and the error message.
    '''
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #since we are inheriting from the exception, we do super.__init__ to inherit the init function.
        self.error_message = error_message_details(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message
    




