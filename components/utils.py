def read_copy(file_name):
    from os.path import join
    with open(join('./src/copys', file_name).replace('\\', '/'), encoding = 'utf-8') as f:
        file = f.read()
    return file

def open_file():
    from tkinter import filedialog
    return filedialog.askopenfilename()
