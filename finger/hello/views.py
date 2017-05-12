from django.shortcuts import render
from django.http import HttpResponse
from .forms import FingerForm
import os
import pymysql
# Create your views here.

def is_exist(fingerprint):
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password=',.klio89',db='fingerprint')
    try:
        with conn.cursor() as cursor:
            sql = 'select * from finger where finger = '+fingerprint
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                return False
            else:
                sql = 'update finger set countNum = %s where finger = '+fingerprint
                cursor.execute(sql,row[6]+1)
                conn.commit()
                return True
    finally:
        conn.close()


def insert(str1,str2,str3,str4,str5):
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password=',.klio89',db='fingerprint')
    try:
        with conn.cursor() as cursor:
            sql = 'insert into finger(finger,os,os_ver,browser,browser_ver,countNum) values(%s,%s,%s,%s,%s,%s);'
            cursor.execute(sql,(str1,str2,str3,str4,str5,1))
            conn.commit()
    finally:
        conn.close()

def hello(request):
    if request.method == 'POST':
        form = FingerForm(request.POST)
        if form.is_valid():
            finger = form.cleaned_data['finger']
            os = form.cleaned_data['os']
            os_ver = form.cleaned_data['os_ver']
            browser = form.cleaned_data['browser']
            browser_ver = form.cleaned_data['browser_ver']

            if is_exist(str(finger)):
                return render(request,"exist.html")
            else:
                insert(str(finger),os,str(os_ver),browser,str(browser_ver))
                return render(request,"bye.html")
    else:
        form = FingerForm()
    return render(request,'hello.html',{'form':form})

