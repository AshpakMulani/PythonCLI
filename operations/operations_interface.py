from abc import ABC, abstractmethod

class OperationsInerface(ABC):
    """
    A class to provide base interface for other classes whihc implements
    command processor using 'process' method.
    
    Attributes
    ----------
        None 
        
    Methods
    -------
        process():
            abstract method for child classes to implement.
        
    """

    @abstractmethod
    def process(self) -> None:
        pass