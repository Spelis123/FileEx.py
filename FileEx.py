from os import listdir, path, getcwd # import
from sys import argv, exit           # modules

files = listdir(getcwd())

def is_even(x):         # check if x is a multiple of two
    return x % 2 == 0   # (how does this even work?)

if "-h" in argv:
    print("""
-----------------  FileEx.py Help  -----------------
    '-hn ' - hide number/file-index
    '-h  ' - shows this help message
    '-g  ' - go to the github page
    '-lf ' - load a config file (params)
    '-nc ' - removes all color. :(
    '-nnf' - removes icons (nerd fonts)
    '-la ' - prints number of files and directories
----------------------------------------------------
""")

    exit()

if "-g" in argv:
    from webbrowser import open_new_tab
    open_new_tab("https://github.com/Spelis123/FileEx.py")
    exit()

if "-lf" in argv:
    file = open(argv[argv.index("-lf") + 1])
    lines = file.readlines()
    argv = []
    for line in lines:
        line = line.replace("\n","")
        argv.append(line)

def cs(text,color):
    if color == "blue":
        colors = '\033[94m' # colored strings
    elif color == "green":
        colors = '\033[92m'
    elif color == "yellow":
        colors = '\033[93m'
    _END = '\033[0m'
    
    if "-nc" in argv:
        colors = ""

    return colors + text + _END

dirsnum:int = 0
filesnum:int = 0
for i in range(len(files)):
    if "-la" in argv:
        if path.isdir(files[i]):
            dirsnum+=1
        elif path.isfile(files[i]):
            filesnum+=1

    flen = len(str(files[i])) # define whether or not a "..." should
    if flen >= 24:#             be at the end of the filename.
        dot = "..."#            only occurs if the filename's length is
    else:#                      equal to or longer than 24 characters.
        dot = ""

    ilen = len(str(i))
    if ilen == 1:
        num = cs("  " + str(i) + " ","yellow") #  define how many spaces should be before
    elif ilen == 2:#                              the file index (i). also one space after
        num = cs(" " + str(i) + " ","yellow") #   and color it yellow (#ffff00).
    elif ilen == 3:
        num = cs("" + str(i) + " ","yellow")

    if not "-nnf" in argv:
        icon = cs("\uf15b ","blue") if path.isfile(files[i]) else cs("\uf07b ","green")     # defines the icon               \ and colors it
    else:                                                                                 # if its a file or a directory.  \ blue or green
        icon = ""

    name = (
            str(files[i])[:21]) + (" " * (24 - len(str(files[i])[:24]) + len(str(i)) # define variable for file name.
 - ilen))

                #     hn = hide number
                # check if "-hn" is in the cmd args
    print((num if not "-hn" in argv else "") + icon + name + dot,end="              ") # print the filename on the screen.
    if not "-oc" in argv:
        print("",end="") if is_even(i) else print("") # check whether or not i is a multiple of two.
    else:
        print("")
print("")
if "-la" in argv:
    print( cs( str(filesnum) + " files and " + str(dirsnum) + " directories" , "yellow" ) )
