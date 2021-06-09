"""
Date: 06/06/2021
Name: Rio Weil
Title: errors.py
Description: Custom errors for project.
"""

"""
Base class for other exceptions
"""
class Error(Exception):
    pass

"""
Error raised when initializing board with zero space or bombs
"""
class ZeroException(Error):
    pass

"""
Error raised when more bombs than possible spaces on board
"""
class TooManyBombsException(Error):
    pass

"""
Error raised when invalid command is given
"""
class InValidInputException(Error):
    pass