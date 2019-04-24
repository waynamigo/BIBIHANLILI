#-*- coding: UTF-8 -*-
''' 
    @Time : 19-4-4 下午10:20 
    @Author : waynamigo 
'''
import re
language = '''<tr><th>床前明月光</th><td>忧思独伤心</td></tr><tr>'''
# 正则表达式获取<tr></tr>之间内容
#res_tr = r"<tr>(.*?)</tr>"
#m_tr = re.findall(res_tr,language,re.S|re.M).__str__()
#print (unicode(m_tr,"utf-8"))
#for line in m_tr:
#    print line
#res_th = r"<th>(.*?)</th>"
#m_th = re.findall(res_th,line,re.S|re.M)
#for mm in m_th:
#    print (unicode(mm,"utf-8"))
#res_td = r"<td>(.*?)</td>"
#m_td = re.findall(res_td,line,re.S|re.M)
#for nn in m_td:
#    print (unicode(nn,"utf-8"))
import requests
base_url = 'http://211.87.177.1/jwxt/uploadfile/studentphoto/pic/'
cat_url  = '.JPG'
filepath= ''
def testfile():
def down_students_headpic():
    for i in range(1,30):
            if i<10:
                stri = '160702020'+str(i)
            else :
                stri = '16070202'+str(i)
            img = requests.get(base_url + stri + cat_url)
            with open('./students_headpics/%s.jpg'%stri,'wb') as f:
                f.write(img.content)
if __name__ == '__main__':
    down_students_headpic()