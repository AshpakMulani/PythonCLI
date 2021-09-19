from os.path import dirname, basename, isfile, join
import glob

# prepare list of all .py files present under current 'intent_processor' folder
# glob module helps finding pathnames of provided criteria
modules = glob.glob(join(dirname(__file__), "*.py"))

# adding all file names from 'intent_processor' folder to __all__ variable
# so that when we import this package from 'intent_processor' folder then
# by default it will import all the .py files from the folder 
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]


