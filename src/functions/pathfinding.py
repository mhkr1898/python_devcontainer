import os
def cur_dir() -> str:
    return os.getcwd() + '/'
def cur_script() -> str:
    current_script_dir: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.basename(__file__)
    loc: str = current_script_dir + "/" + filename
    return loc
