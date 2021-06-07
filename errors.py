



"""
Base class for other exceptions
"""
class Error(Exception):
    pass

"""
Error raised when more bombs than possible spaces on board
"""
class TooManyBombsException(Error):
    pass

"""
Error raised when initializing board with zero space or bombs
"""
class ZeroException(Error):
    pass
