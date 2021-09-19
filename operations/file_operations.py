from typing import List
import messages
import logging
import logging.config
from operations.operations_interface import OperationsInerface
import os
from typing import TextIO


# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('FooTools')


class FileOps(OperationsInerface):
    """
    A class to provide methods to handle FooTool commands which
    are specific to file operations
    
    Attributes
    ----------
        command : str
            command entered by user in console 
        
    Methods
    -------
        process():
            abstract method implementation from interface class
            whihc maps individual handler funciton for commands
        
        create_file():
            create a new file (no override) at specified path 
        
        delete_file():
            delets a file from specified path 

        rename_file():
            rename a file from specified path and move it to
            new mentioned path after rename

    """


    supported_commands: List[str] = [
        "createfile",
        "deletefile",
        "renamefile",     
    ]

    
    def __init__(self, command) -> None:
        self.command: str = command

    
    def process(self) -> None:
        """
        maps individual handler funciton with specified command
        """
        
        if self.command[1] == "--createfile":
            # check if file path is provided and only required params are present
            if (len(self.command) == 3 and len(self.command[2]) > 0):
                return self.create_file()
            else:
                logger.error(messages.general("Incorrect file path"))
        if self.command[1] == "--deletefile":
            # check if file path is provided and only required params are present
            if (len(self.command) == 3 and len(self.command[2]) > 0):
                return self.delete_file()
            else:
                logger.error(messages.general("Incorrect file path"))               
        if self.command[1] == "--renamefile":
            # check if file path and target file path is provided 
            # and only required params are present
            if (len(self.command) == 4 and len(self.command[2]) > 0  and 
                len(self.command[3]) > 0):
                return self.rename_file()
            else:
                logger.error(messages.general("Incorrect parameters"))  

    
    def create_file(self) -> None:
        """
        create a new file (no override) at specified path 
        """
        try:
            # get file path from command line
            path: str = self.command[2]            
            f: TextIO = open(path, "x")
            f.close()
            logger.info(messages.general("File created at : " + path))
        except Exception as e:
            logger.error(e)

    
    def delete_file(self) -> None:
        """
        delets a file from specified path 
        """
        try:
            # get file path from command line
            path: str = self.command[2]            
            os.remove(path)
            logger.info(messages.general("File deleted : " + path))
        except Exception as e:
            logger.error(e)
        
    
    def rename_file(self) -> None:
        """
        rename a file from specified path and move it to
        new mentioned path after rename
        """
        try:  
            source_path: str = self.command[2]
            target_path: str = self.command[3]
            os.rename(source_path, target_path)
            logger.info(messages.general("File renamed : " + target_path))
        except Exception as e:
            logger.error(e)