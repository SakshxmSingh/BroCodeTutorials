# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

import messages as msg                          # to import the whole module and use as a different name
msg.hello()                                     #
msg.bye()                                       #

from messages import hello, bye                 # to import particular fncs from a module
hello()
bye()

# --------------to display all module names--------------- #
help("modules")
