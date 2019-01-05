from django.shortcuts import render,redirect
from .models import Jotunts
from django.db.models import Q
from django.contrib.auth import logout
from django.http import HttpResponse
import os
from django.conf import settings
from django.core.paginator import Paginator
# Create your views here.
# 引入验证码模块，自己写的放在项目目录里面
from jotun.verifycode import verifycode
def tsview(request,page):
    page=int(page)
    studentsList=Jotunts.objects.all()[(page-1)*10:page*10]
    return render(request,'jotun/tssearch.html',{'students':studentsList})
def index(request):
    username = request.session.get('name')
    if Jotunts.objects.filter(chinname=username):
        return redirect('tsinfo/search/')
    else:
        return render(request,'jotun/index1.html',{'username':username})
def search(request):
    keyword = request.POST.get('keyword','')
    username=request.session.get('name','游客')
    pageid=1
    error_msg = ''
    if not keyword:
        error_msg = '请输入关键词'
        return render(request, 'jotun/page.html', {'error_msg': error_msg,'username':username})
    if Jotunts.objects.filter(chinname=username):
        request.session['keyword']=keyword
        studentsList = Jotunts.objects.filter(Q(chinname__contains=keyword)|Q(engname__icontains=keyword)|Q(shipyard__icontains=keyword)|
                                              Q(tel__icontains=keyword)|Q(email__icontains=keyword))
        # 写分页显示
        paginator=Paginator(studentsList,10)
        page=paginator.page(pageid)
        return render(request,'jotun/page.html',
                      {'students':page,'username':username,'keyword':keyword})
    else:
        return redirect('/')
def searchpage(request,pageid):
    keyword = request.session.get('keyword',"")
    username=request.session.get('name','游客')
    error_msg = ''
    if not keyword:
        error_msg = '请输入关键词'
        return render(request, 'jotun/page.html', {'error_msg': error_msg,'username':username})
    if Jotunts.objects.filter(chinname=username):
        studentsList = Jotunts.objects.filter(Q(chinname__contains=keyword)|Q(engname__icontains=keyword)|Q(shipyard__icontains=keyword)|
                                              Q(tel__icontains=keyword)|Q(email__icontains=keyword))
        # 写分页显示
        paginator=Paginator(studentsList,10)
        page=paginator.page(pageid)
        return render(request,'jotun/page.html',
                      {'students':page,'username':username,'keyword':keyword})
    else:
        return redirect('/')
def login(request):
    username=request.POST.get('username')
    inputcode=request.POST.get('verify')
    code=request.session['verifycode']
    flag=''
    if Jotunts.objects.filter(chinname=username) and inputcode==code:
        request.session['name']=username
        # request.sesson['flag']=True
        request.session.set_expiry(0)
        return redirect('/tsinfo/search/')
    else:
        if inputcode!=code:
            flag='验证码错误请重试！'
            # request.session['flag']=False
            return render(request, 'jotun/index1.html', {'flag': flag})
        flag='请正确输入你的姓名！'
        return render(request, 'jotun/index1.html', {'flag': flag})
def quit(request):
    logout(request)
    return redirect('/')
# def main(request):
#     return render(request,'jotun/main.html')

def upfiles(request):
    return render(request,'jotun/uploads.html')
def savefile(request):
    if request.method=='POST':
        f=request.FILES['file']
        filepath=os.path.join(settings.MDEIA_ROOT,f.name)
        with open(filepath,'wb') as file:
            for info in f.chunks():
                file.write(info)
        return HttpResponse('上传成功！')
    else:
        return HttpResponse('上传失败！')
