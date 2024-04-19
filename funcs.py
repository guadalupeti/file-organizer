import os

def options():
    print('What do you want to do?')
    print('[ 1 ] ORGANIZE BY FILE EXTENSION')
    print('[ 2 ] ORGANIZE BY FIRST LETTER')
    print('[ 3 ] ORGANIZE BY CREATION DATE')
    print('[ 4 ] ORGANIZE BY SIZE')
    print('[ 5 ] CHANGE PATH')
    print('[ 6 ] EXIT ')

def folder_conditionals_for_4(path, folder):
    if not os.path.exists(path+'/'+folder):
        os.makedirs(path+'/'+ folder)
    else:
        pass