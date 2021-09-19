from operations import *
from operations import operations_interface
import messages
import logging
import logging.config
from typing import Optional, List

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('FooTools')


class CommandMapper:
        
    """
    A class to dynamically instanciate suitable command handler class
    (from operations folder) if command is present under list of 
    supported commands handled by the respective class. 
    
    Attributes
    ----------
        None
    Methods
    -------
        process_command(command: str):
            initiates object for the class whihc supports provided intent handler
            by matching input intent name with the suported intent list present 
            under individual intent handler classe.
    """
    
    def __init__(self) -> None:
        pass

    def process_command(self, command: str) -> None:
        """
        initiates object for the class whihc supports provided intent handler
        by matching input intent name with the suported intent list present 
        under individual intent handler classe.
        """

        command_list: List[str] = command.split(" ")

        if command_list[0] == "footools" :
            command_verb: str = command_list[1]
            
            for cls in operations_interface.OperationsInerface.__subclasses__():

                if (command_verb.replace("--","") in cls.supported_commands):
                    return cls(command_list).process()
                
            logger.error(messages.option_not_suported(command_verb))

        elif len(command_list) == 0:
            return None
        else :
            logger.error(messages.command_not_suported(command_list[0]))