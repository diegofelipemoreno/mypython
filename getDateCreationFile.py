import pdb
from datetime import datetime
import os.path, time

today = datetime.today()
print(today)

print(time.ctime(os.path.getctime('/Users/diegomoreno/mypython/exceptions.py')))

actual_time = time.time()
old_file_time = os.path.getctime('/Users/diegomoreno/mypython/exceptions.py')


print(round(actual_time), 'actual time')
print(round(old_file_time))

print(time.strftime('%Y%m%d',time.localtime()))


try:
    os.chdir('assets')
except FileNotFoundError:
    print('No such file or directory')
finally:
    file_path = os.path.abspath('contact.js')
    file_datetime_creation = os.path.getctime(file_path)
    print('---------------------z')
    print(time.strftime('%Y-%m-%d', time.localtime(file_datetime_creation)))
    print(file_datetime_creation)

print('---------------------')
thisdir = os.getcwd()
for root, dirs, files in os.walk(thisdir):
    for file in files:
        if "infile-asset.txt" in file:
            file_path = os.path.join(root, file) 
            date_creation_file = os.path.getctime(file_path)
            date_format_file = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1575650844))
            date_format_file_number = time.strftime('%Y%m%d', time.localtime(1575650844))
            print(date_format_file_number)

print("------------------------xxxxx")
actual_time = time.strftime('%Y%m%d', time.localtime(time.time()))
print(actual_time)

print("------------------------")
myfile = '/Users/diegomoreno/androidp/content/pages/_docs/colors.md'
file_mod_time = os.stat(myfile).st_mtime

# Time in seconds since epoch for time, in which logfile can be unmodified.
should_time = time.time() - (30 * 60)

# Time in minutes since last modification of file
last_time = (time.time() - file_mod_time) / 60

print(should_time, time.strftime('%Y-%m-%d', time.localtime(should_time)), last_time, time.strftime('%Y%m%d', time.localtime(last_time)) )
print(file_mod_time - should_time)

print("------------------------")
created= os.stat(myfile).st_ctime
print(datetime.fromtimestamp(created))

print("------------------------")
import datetime
import glob
import smtplib
import string
 
now  = datetime.datetime.today() #Get current date
 
list_of_files = glob.glob(myfile) # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime) #get latest file created in folder
 
newestFileCreationDate = datetime.datetime.utcfromtimestamp(os.path.getctime(latest_file)) # get creation datetime of last file
 
dif = (now - newestFileCreationDate) #calculating days between actual date and last creation date
 
print(dif)
print(os.stat(myfile))