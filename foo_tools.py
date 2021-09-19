from pyfiglet import Figlet  # type: ignore
import os
from os import path
import random
import messages
import logging
import logging.config
from command_mapper import CommandMapper


"""
Main entry point for the utility.
Keeps running in a loop to accept user input for 
commands to be executed.

Parameters
    ----------
    None

Returns
    ----------
    None
"""


# create logger with settings mentioned in logging.conf file
logging.config.fileConfig('logging.conf')
logger: logging.Logger = logging.getLogger('FooTools')



def process_command(command) -> None:
    """
    Initiates CommandMapper class and dispatch user entered
    command to process 
    
    Parameters
        ----------
        command : str
            command entered by user
    Returns
        ----------
        None
    """
    cmapper: CommandMapper = CommandMapper()
    cmapper.process_command(command)
    

def main() -> None:
    #Figlet library is used for ASCI art font
    f: Figlet = Figlet(font='slant')
    print(f.renderText('FOO Tools'))

    #keep running in a loop to process user commands
    while(1):
        command: str = input("_>> ")
        process_command(command)


if __name__ == "__main__":
    main()