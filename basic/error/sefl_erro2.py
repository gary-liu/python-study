class Error(Exception):
    '''
    Base class for exceptions in this modules
    '''

class InputError(Error):
    """
    Exception raised for errors in the input
    Attrbutes:
    expression -- input expression in which the errror occurred
    message -- explanation of errro
    """

class TransitionErrro(Error):
    """Raised when an operation attempts a state transition that's not
       allowed.

       Attributes:
           previous -- state at beginning of transition
           next -- attempted new state
           message -- explanation of why the specific transition is not allowed
    """
    def __init__(self,previous,next,message):
        self.previous = previous
        self.next = next
        self.message = message

