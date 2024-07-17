class OneDArrayError(Exception):
    """Exception raised for errors in the input when a 2D array is expected but a 1D array is provided."""
    def __init__(self, message="Array has a 1D array within it"):
        self.message = message
        super().__init__(self.message)

class MoreThanTwoDArrayError(Exception):
    """Exception raised for errors in the input when a 2D array is expected but a 3D or more array is provided."""
    def __init__(self, message="Array has a 3D or more array within it"):
        self.message = message
        super().__init__(self.message)