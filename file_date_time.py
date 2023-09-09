from os import path
import time

print(f'Last Modification: {time.ctime(path.getmtime("file_date_time.py"))}')
print(f'Creation: {time.ctime(path.getctime("file_date_time.py"))}')
