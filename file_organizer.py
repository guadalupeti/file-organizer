import os
import shutil
from funcs import options, folder_conditionals_for_4
from datetime import datetime

path = input('\033[32mEnter path: \033[m')

files = os.listdir(path)



while True:

    options()

    choice = int(input('\033[1;34mYour choice: \033[m'))
    
    match choice:
        case 1:
            for file in files:
                filename, extension = os.path.splitext(file)
                extension = extension[1:]

                if not os.path.exists(path+'/'+extension):
                    os.makedirs(path+'/'+extension)

                shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
            print('\033[1;34mDone!\033[m')
        
        case 2:
            for file in files:
                initial = file[0].upper().strip()
                if not os.path.exists(path+'/'+ initial):
                    os.makedirs(path+'/'+ initial)

                shutil.move(path+'/'+file, path+'/'+initial+'/'+file)
            print('\033[1;34mDone!\033[m')

        case 3:
            for file in files:
                full_path = os.path.join(path, file)
                if os.path.isfile(full_path):
                    date = os.stat(full_path).st_ctime
                    timestamp = date
                    date_hour = datetime.fromtimestamp(timestamp)
                    day= str(date_hour.day)
                    month = str(date_hour.month)
                    year = str(date_hour.year)
                    date_print = month+'-'+day+'-'+year
                    
                    if not os.path.exists(path+'/'+date_print):
                        os.makedirs(path+'/'+ date_print)

                    shutil.move(path+'/'+file, path+'/'+date_print+'/'+file)
            print('\033[1;34mDone!\033[m')
        
        case 4:
            for file in files:
                full_path = os.path.join(path, file)
                if os.path.isfile(full_path):
                    size = os.path.getsize(full_path)
                    size_mb = size/(1024**2)

                    if size_mb >= 0 and size_mb < 1:
                        folder_conditionals_for_4(path,'small')
                        shutil.move(path+'/'+file, path+'/small')
                    elif size_mb >= 1 and size_mb < 1000:
                        folder_conditionals_for_4(path,'medium')
                        shutil.move(path+'/'+file, path+'/medium')
                    elif size_mb >= 1000 and size_mb < 1000:
                        folder_conditionals_for_4(path,'big')
                        shutil.move(path+'/'+file, path+'/big')
            print('\033[1;34mDone!\033[m')
        
        case 5:
             path = input('\033[32mEnter path: \033[m')

        case 6:
            break
                        

    
    
