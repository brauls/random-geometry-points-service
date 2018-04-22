"""Register error handlers to an api
"""

def register_error_handler(api):
    """Register error handlers to the passed api.

    Args:
        api (flask_restplus.Namespace): The namespace to which the error handlers
          shall be registered
    """

    @api.errorhandler(ValueError)
    def _handle_value_error(error):
        """Error handler for ValueError errors.

        Args:
            error (ValueError): The error object

        Returns:
            tuple: An error message along with the Http status code
        """
        return {"message": str(error)}, 400

    @api.errorhandler(TypeError)
    def _handle_type_error(error):
        """Error handler for TypeError errors.

        Args:
            error (TypeError): The error object

        Returns:
            tuple: An error message along with the Http status code
        """
        return {"message": str(error)}, 400
