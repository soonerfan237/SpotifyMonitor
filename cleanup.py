import os

def remove_result_file(result_file_name):
    os.remove(result_file_name)
    return True