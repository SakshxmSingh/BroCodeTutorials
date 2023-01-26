# *********************************
# if __name__ == '__main__'
# *********************************

# module with this statement can be
# 1. Run as a standalone program
# 2. Imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will assign the __name__ variable a value of '__main__' if it's the initial module being run

import module62                                       # module62.py used

print(__name__)                                       # gives '__main__' if the current module is being run
print(module62.__name__)                              # gives the name of the module used, in this case 'module62'

if __name__ == '__main__':
    print("running current module directly")
else:
    print("running other module indirectly")




