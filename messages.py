
"""
set of dumb functions responsible for returning formatted messages
as per the requirement.

"""


def command_not_suported(command: str) -> str:
    """
    returns a formatted message for commands not supported by FooTools.
    """
    return (f"Command not supported : {command} \n" +
            "Please use 'footools --help' or 'footools -h' " +
            "to get details on the supported commands.")


def option_not_suported(option: str) -> str:
    """
    returns a formatted message for command options not supported by 
    FooTools command.
    """
    return (f"Command option not support : {option} \n" +
            "Please use 'footools --help' or 'footools -h' " +
            "to get details on the supported commands.")


def general(message: str) -> str:
    """
    returns a formatted message for general notificaitons.
    """
    return (f"{message}")


def get_help() -> str:
    """
    returns help mannual for commands supported by FooTools.
    """
    return (
            "\nUsage : footools [option] \n\n" +

            "General Options and arguments \n" +
            "\t--help : get command line option details \n" +
            "\t--exit : Exit Footools CLI " +
            "\n\nFile Operaiton options and arguments \n" +
            "\t--createfile [path]: create a new file on specified path\n"
            "\t\t Ex. footools --createfile c:\\footools\\footools_sample.txt\n"
            "\t--deletefile [path] : delete specified file\n"
            "\t\t Ex. footools --deletefile c:\\footools\\footools_sample.txt\n"
            "\t--renamefile [source_path] [target_path] : rename specified file\n"
            "\t\t Ex. footools --renamefile c:\\footools\\footools_sample.txt c:\\footools\\footools.txt"
            "\n\nFolder Operaiton options and arguments \n" +
            "\t--createfolder [path]: create a new folder on specified path\n"
            "\t\t Ex. footools --createfolder c:\\footools\\footools_sample\n"
            "\t--deletefolder [path] : delete specified folder\n"
            "\t\t Ex. footools --deletefolder c:\\footools\\footools\n"
            "\t--renamefolder [source_path] [target_path] : rename specified folder\n"
            "\t\t Ex. footools --renamefolder c:\\footools\\footools c:\\footools\\footools_new\n"
            "\t--zipfolder [folder_path] [zip_path] : zip specified folder\n"
            "\t\t Ex. footools --zipfolder c:\\footools\\footools c:\\footools\\footools.zip"
    )