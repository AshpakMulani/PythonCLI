from typing import List
import messages
import os
import logging
import logging.config
import zipfile
from zipfile import ZipFile
from operations.operations_interface import OperationsInerface

# create logger
logging.config.fileConfig('logging.conf')
logger: logging.Logger = logging.getLogger('FooTools')


class FolderOps(OperationsInerface):

    """
    A class to provide methods to handle FooTool commands which
    are specific to folder operations
    
    Attributes
    ----------
        command : str
            command entered by user in console 
        
    Methods
    -------
        process():
            abstract method implementation from interface class
            whihc maps individual handler funciton for commands
        
        create_folder():
            create a new folder (no override) at specified path 
        
        delete_folder():
            delets a folder from specified path 

        rename_folder():
            rename a folder from specified path and move it to
            new mentioned path after rename

        zip_folder():
            zip contents of a specific folder and move zip file
            to specified target location
        
    """



    supported_commands: List[str] = [
        "createfolder",
        "deletefolder",
        "renamefolder",
        "zipfolder",      
    ]

    def __init__(self, command: str) -> None:
        self.command: str = command

    
    def process(self) -> None:
        """
        maps individual handler funciton with specified command
        """

        if self.command[1] == "--createfolder":
            # check if folder path is provided and only required params are present
            if (len(self.command) == 3 and len(self.command[2]) > 0):
                return self.create_folder()
            else:
                logger.error(messages.general("Incorrect folder path"))
        if self.command[1] == "--deletefolder":
            # check if folder path is provided and only required params are present
            if (len(self.command) == 3  and len(self.command[2]) > 0):
                return self.delete_folder()
            else:
                logger.error(messages.general("Incorrect folder path")) 
        if self.command[1] == "--renamefolder":
            # check if folder path and target folder path is provided
            # and only required params are present
            if (len(self.command) == 4 and len(self.command[2]) > 0  and 
                len(self.command[3]) > 0):
                return self.rename_folder()
            else:
                logger.error(messages.general("Incorrect parameters"))  
        if self.command[1] == "--zipfolder":
            # check if folder path and zip folder path is provided
            # and only required params are present
            if (len(self.command) == 4 and len(self.command[2]) > 0  and 
                len(self.command[3]) > 0):
                return self.zip_folder()
            else:
                logger.error(messages.general("Incorrect parameters"))  
                
    
    def create_folder(self) -> None:
        """
        create a new folder (no override) at specified path 
        """
        try:
            # get folder path from command line
            path = self.command[2] 
            os.mkdir(path)
            logger.info(messages.general("Folder created : " + path))
        except Exception as e:
            logger.error(e)

    
    def delete_folder(self) -> None:
        """
        delets a folder from specified path
        """
        try:
            # get folder path from command line
            path: str = self.command[2]            
            os.remove(path)
            logger.info(messages.general("Folder deleted : " + path))
        except Exception as e:
            logger.error(e)        
        

    def rename_folder(self) -> None:
        """
        rename a folder from specified path and move it to
        new mentioned path after rename
        """
        try:  
            source_path: str = self.command[2]
            target_path: str = self.command[3]
            os.rename(source_path, target_path)
            logger.info(messages.general("Folder renamed : " + target_path))
        except Exception as e:
            logger.error(e)


    def zip_folder(self) -> None:
        """
        zip contents of a specific folder and move zip file
        to specified target location
        """
        source_path: str = self.command[2]
        
        # check source directory is present before starting zip process
        if os.path.isdir(source_path):        
            zip_path: str = self.command[3]
            zipf: ZipFile = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)

            # write individual file from source locaiton to a zip file
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    zipf.write(os.path.join(root, file), \
                    os.path.relpath(os.path.join(root, file), \
                    os.path.join(source_path, '..')))

            zipf.close()
            logger.info(messages.general("zip created : " + zip_path))
        else:
            logger.error(messages.general("source folder does not exist."))