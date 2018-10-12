import selenium
from selenium import webdriver
import bs4
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

f=open('sis_data.txt','w')
driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver_win32\chromedriver")
#driver.implicitly_wait(30)
#driver.maximize_window()
driver.get("http://parents.msrit.edu")  #Open the website
usn=driver.find_element_by_id("username")
usn.clear()
usn.send_keys('1ms16ee032')   #input usn in the website
password=driver.find_element_by_id("password")
st=input("enter the dob")
password.clear()
password.send_keys(st)  #input password in the website
driver.find_element_by_name("submit").click()  #click submit

ele=driver.page_source
src=bs4.BeautifulSoup(ele,'lxml')
info=[]
for k in src.select('.tname2'):
    ele = driver.page_source
    src = bs4.BeautifulSoup(ele, 'lxml')
    st=k.text
    info.append(st)
info[2]=info[2].replace('Semester','')
info[3]=info[3].replace('Credits Earned :','')
info[4]=info[4].replace('Credits to Earn :','')
info.pop()
for i in info:
   i=i.strip()
   i=i+'\n'
   f.write(i)
info=[]
count=0
for k in src.select('.courseCode'):
    count+=1

for k in range(0,count):
    attendance = driver.find_elements_by_class_name("att_label")  # to go into attandance label
    attendance[k].click()
    attendance_ele = driver.page_source
    attendance_src = bs4.BeautifulSoup(attendance_ele, 'lxml')   #loading the attandance page
    code=attendance_src.select('.courseCode')
    code = code[0].text
    code=code+'|'
    f.write(code)

    name=attendance_src.select('.coursename')
    name=name[0].text
    name=name+'|'
    f.write(name)

    lect=[]
    lecturer=''
    for j in attendance_src.select('.tname'):
        lect.append(j.text)
    for m in range(0,len(lect)):
        if(m!=len(lect)-1):
            lecturer=lecturer+lect[m]+','
        else:
            lecturer=lecturer+lect[m]
    lecturer=lecturer+'|'
    f.write(lecturer)


    perc=attendance_src.select(".att")
    perc=perc[0].text
    perc=perc.replace("\nAttendance",'')
    perc=perc+'|'
    f.write(perc)

    attended=driver.find_element_by_xpath('//*[@id="sub-container"]/div/div[3]/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/div[1]').text
    if attended=='':
        attended='0'
    attended=attended+'|'
    f.write(attended)

    absent=driver.find_element_by_xpath('//*[@id="sub-container"]/div/div[3]/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/div[2]').text
    if absent=='':
        absent='0'
    absent=absent+'|'
    f.write(absent)

    total_classes=attendance_src.select('.emptydiv')
    total_classes=total_classes[0].text
    total_classes=total_classes+'\n'
    f.write(total_classes)

    driver.back()

    #cie = driver.find_elements_by_class_name("cie_label") #get into cie page
    #cie[k].click()
    #cie_ele = driver.page_source
    #attendance_src = bs4.BeautifulSoup(cie_ele, 'lxml')  # loading the cie page
    





f.close()
driver.close()