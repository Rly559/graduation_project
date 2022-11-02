# _*_ coding :utf-8 _*_
# @Time :2022/3/8 14:41
# @Author :河北地质大学 李林逸
# @File : 前程无忧
# @Project :爬虫


import re
import requests
import csv


f = open('前程无忧1.csv','a')
csvwriter = csv.writer(f)

url_base = 'https://search.51job.com/list/000000,000000,0100%252c7700%252c7200%252c7300%252c7800,00,9,99,+,2,'
url_rear = '.html?lang=c'

headers ={
    'cookie': '_uab_collina=164672175158504436797079; guid=2b1b1c8fc5193af7a34127a956339e01; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; _ujz=MTY5NTYzMzg3MA%3D%3D; ps=needv%3D0; partner=sem_pcbaidubd_250; privacy=1648711163; acw_sc__v2=624555fd10d33adfe2b1765f64a949899093c003; 51job=cuid%3D169563387%26%7C%26cusername%3D9WKRlfr8Tz8IBFUAukT1qbxWkMSlOZcS9HJNUTZizqc%253D%26%7C%26cpassword%3D%26%7C%26cname%3DQpgtMoEmOTkIFM8HAbc%252BCw%253D%253D%26%7C%26cemail%3DsTCcceCD4r%252B6SL3RdoLyg5G97DWoFxf8VT5wrFbXp78%253D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0KqczAMceV3A%26%7C%26cconfirmkey%3D27UuOcDrEejyc%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D27rdK.mPpRogI%26%7C%26to%3Da5bb00767590841376eb7e2577042a0362455cb2%26%7C%26; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20220331%26%7C%26securetime%3DBztQZVAyA29QNQA%252FCzIMbwc9Cj4%253D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0100%2C7700%2C7200%2C7300%2C7800%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA4400%2C4300%2C4200%2C4500%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA4400%2C4300%2C4200%2C4500%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0600%2C2300%2C0700%2C7400%2C0900%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21; ssxmod_itna=eqUxgQKiqDqWuDYq0dc7tD9ADBimKr3KQW5t7Dl=G4A5D8D6DQeGTT21QTrptQzbZq0Q7Y0G03KObtAiRQtCm+qwW+WWO4GLDmKDyKbrueDxaq0rD74irDDxD3cD7PGmDiWZRUrqAQDKx0kDY5DwcvkDYPDWxDFU=ebQBI8DeKD0xD1xzosDDPDag911=7sPIgiygmkD75Dux0HteMmH3d6QDi3EGFGx40OD0K+cZahDB4N3CaFMex5aCpTK0e5tiinQPP5Q=4NHuDdQGnPHGRPQBgD+Lci4D===; ssxmod_itna2=eqUxgQKiqDqWuDYq0dc7tD9ADBimKr3KQW5tD6hS00x0yilD03CrtutDujOgfeOKGFBauptqqcrdurC4wmOIevqwemGLYeKF7FuA1c=uGFE4wZPFihBz22SWK0I27FF89dBRtSEeIwKhGqXhbRx6K45fee50KbhM/r2EKBY3kSjY5i5Hz3RQwqrUG8fYChnG84Ub2utM8b+SmmuOwxIYhPIP=1yOWPI278=kN==GgbHCjdLCoMbM3wIhuuYnmRUYQYqdhSaohRgkqs9IG4tZSe3zrmAX=HvXgnPydvz1KTH+7P7+tdAHYeGDogiNPeox4UqfeLgD9eERnKFx5ugDF6EToeU=e3bNdRrPb3EmPxtKh0pDzqKKrriob+=LPh/0px0h9PKnQKbfqebuU=09AI97b4gr+FoNIennXtnPZmrmGEMr3Cib6=e8I2YYYirXxG0U3epfTSZXEnteKmkKvIn580RUDt9nXNZLY4Fh8RYhF4UTKKiTtKBbeLoY8mPy/5/eHmivbo6BWAbZ+eV4qTKWDG230qt+1BGK/p4m4vrnbfrAPxEOivKGzCGqVb892tnhpvKjaa8DeDFqD+=v5GmQmxEoTxD=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/103'
}

for x in range(25,30):
    url=url_base + str(x) + url_rear
    response = requests.get(url = url,headers = headers).text
    obj = re.compile(r'job_name":"(?P<job_name>.*?)",.*?"company_name":"(?P<company_name>.*?)","providesalary_text":"(?P<salary>.*?)",.*?workarea_text":"(?P<work_area>.*?)",.*?"companytype_text":"(?P<company_type>.*?)",.*?jobwelf_list":(?P<job_welfare>.*?),"isdiffcity":"","attribute_text":.*?","(?P<work_experience>.*?)","(?P<education>.*?)","(?P<admission_number>.*?)"],"companysize_text":"(?P<company_size>.*?)","companyind_text":"(?P<companyind_text>.*?)","adid":',re.S)
    result = obj.finditer(response)
    for i in result:
        dic = i.group('job_name','company_name','salary','work_area','company_type','job_welfare','work_experience','education','admission_number','company_size','companyind_text')
        csvwriter.writerow(dic)
        print(dic)

f.close()
print('over!')