from stringcolor import cs           # import
from os import listdir, path, getcwd # modules
from sys import argv

files = listdir(getcwd())

def is_even(x):         # check if x is a multiple of two
    return x % 2 == 0   # (how does this even work?)

if "-h" in argv:
    print("""
----------  FileEx.py Help  ----------
    '-hn'  - hide number/file-index
    '-h '  - shows this help message
    '-g '  - go to the github page
--------------------------------------
""")
    quit()

if "-g" in argv:
    from webbrowser import open_new_tab
    open_new_tab("https://github.com/Spelis123/FileEx.py")

for i in range(len(files)):
    flen = len(str(files[i])) # define whether or not a "..." should
    if flen >= 24:#             be at the end of the filename.
        dot = "..."#            only occurs if the filename's length is
    else:#                      equal to or longer than 24 characters.
        dot = ""

    ilen = len(str(i))
    if ilen == 1:
        num = cs("  " + str(i) + " ","#ffff00") # define how many spaces should be before
    elif ilen == 2:#                              the file index (i). also one space after
        num = cs(" " + str(i) + " ","#ffff00")#   and color it yellow (#ffff00).
    elif ilen == 3:
        num = cs("" + str(i) + " ","#ffff00")


    icon = cs("\uf15b","#0000ff") if path.isfile(files[i]) else cs("\uf07b","#00ff00") # defines the icon               \ and colors it
                                                                                          # if its a file or a directory.  \ blue or green

    name = (
            str(files[i])[:21]) + (" " * (24 - len(str(files[i])[:24]) + len(str(i)) # define variable for file name.
 - ilen))
                #     hn = hide number
                # check if "-hn" is in the cmd args
    print((num if not "-hn" in argv else "") + icon + " "+ name + dot,end="              ") # print the filename on the screen.
    print("",end="") if is_even(i) else print("") # check whether or not i is a multiple of two.
