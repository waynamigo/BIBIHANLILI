#-*- coding: UTF-8 -*-
''' 
    @Time : 19-4-4 下午10:20 
    @Author : waynamigo 
'''

import requests
import time
import os
import pandas as pds
base_url = 'http://211.87.177.1/jwxt/uploadfile/studentphoto/pic/'
cat_url  = '.JPG'
filepath= './data.csv'
students = pds.read_csv('down_headpic/data.csv')
studentdf  = pds.DataFrame(students)
# class student:
#     def __init__(id,name,major_class):
def count():
    return int(studentdf['学号'].count())
# def names():
#     return studentdf['姓名']
def down_students_headpic():
    for i in range(1,count()):
        stri =  studentdf['学号'].iloc[i,]
        print stri
        time.sleep(0.2)
        name =  studentdf['姓名'].iloc[i,]
        try:
            img = requests.get(base_url +stri + cat_url)
            with open('down_headpic/students_headpics/%s.jpg'%stri,'wb') as f:
                if os.path.exists('down_headpic/students_headpics/%s.jpg'%stri):
                    continue
                else:
                    f.write(img.content)
        except:
            continue

if __name__ == '__main__':
    down_students_headpic()