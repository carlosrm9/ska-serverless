import os

def main():
    file_list = os.listdir('/mnt')
    file_list_str = "\n".join(file_list)
    return file_list_str
