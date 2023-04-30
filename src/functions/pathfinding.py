import os
def cur_dir():
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    return current_script_dir
def cur_script():
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.basename(__file__)
    loc = current_script_dir + "/" + filename
    return loc
