from django.shortcuts import render
from .forms import AddrForm

# Create your views here.
import pymysql

class MySqlOp:
    def __init__(self,host,user,pwd,dbname):
        self.db = pymysql.connect(host,user,pwd,dbname)
        self.cursor = self.db.cursor()

    def select(self,sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone() 
        except Exception as e:
            print('select fail',e)
            return ''
    
    def is_exist(self,addr):
        try:
            sql = 'select * from blackIP where addr = \"'+addr+'\"'
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            if row is None:
                return False
            else:
                return True
        except Exception as e:
            print('select fail',e)

    def __del__(self):
        self.cursor.close()
        self.db.close()

def getStatus(request):
    opt = MySqlOp('127.0.0.1','root',',.klio89','fingerprint')
    if request.method == 'POST':
        form = AddrForm(request.POST)
        if form.is_valid():
            addr = form.cleaned_data['addr']
            
            if opt.is_exist(addr):
                sql = 'select * from blackIP where addr = \''+addr+'\''
                results = opt.select(sql)
                return render(request,'result.html',{'results':results})
            else:
                return render(request,'error.html')
    else:
        form = AddrForm()
    return render(request,'index.html',{'form':form})
