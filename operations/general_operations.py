from typing import List
import messages
import logging
import logging.config
from operations.operations_interface import OperationsInerface

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('FooTools')


class GeneralOps(OperationsInerface):
    """
    A class to provide methods to handle general commands which
    are not specific to file or folders
    
    Attributes
    ----------
        command : str
            command entered by user in console 
        
    Methods
    -------
        process():
            abstract method implementation from interface class
            whihc maps individual handelr funciton for commands
        
        get_help():
            returns help manual for commands supported by FooTool
        
        exit():
            stops execution of FooTool CLI
        
    """

    supported_commands: List[str] = [
        "help",
        "exit",      
    ]

    def __init__(self, command: str) -> None:
        self.command: str = command

    def process(self) -> None:
        """
        maps individual handler funciton with specified command
        """
        
        if self.command[1] == "--help":
            return self.get_help()
        if self.command[1] == "--exit":
            return self.exit()      

    def get_help(self) -> None:    
        """
        print help manual for commands supported by FooTool
        """    
        print(messages.get_help())
      

    def exit(self) -> None:
        """
        stops execution of FooTool CLI
        """
        logger.info(messages.general("Thank You for using FooTools.\n"))
        exit()