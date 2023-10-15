import os, sys

# Define a custom exception class
class CustomException(Exception):
    # Initialize the custom exception
    def __init__(self, error_message: Exception, error_details: sys):
        # Generate a detailed error message and store it
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,
                                                                       error_details=error_details)
        
    # Static method to generate a detailed error message
    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys) -> str:
        # Get information about the exception's traceback
        _, _, exce_tb = error_details.exc_info()

        # Extract line numbers and file name
        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        # Create the error message string
        error_message = f"""
        Error occurred in the execution of:
        [{file_name}] at
        try block line number: [{try_block_line_number}]
        and exception block line number: [{exception_block_line_number}]
        error message: [{error_message}]
        """
        return error_message
    
    # Define how the exception should be represented as a string
    def __str__(self):
        return self.error_message
    
    # Define how the exception should be represented as a string when using repr()
    def __repr__(self):
        return f"{CustomException.__name__}('{self.error_message}')"
