import os

os.chdir('/home/guertinu/Desktop')


with open(os.getcwd()+'/index.txt', 'w') as file:
    file.close()