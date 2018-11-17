from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator
from booktest.models import BookInfo, HeroInfo, AreaInfo, PicTest
from datetime import datetime
# Create your views here.

# http://127.0.0.1:8000/index
from mytest1 import settings


def index(request, exception=None):
    return  my_render(request,'booktest/index.html', {})

def index2(request):
    return render(request, "booktest/index2.html", {'name': "xiaoming", 'list': range(1, 10)})
def query_book(request):
    book = BookInfo.objects.all()
    books = {'books': book}
    return render(request, 'booktest/index3.html', books)


def my_render(request, template_path, context={}):
    temp = loader.get_template(template_path)
    res_html = temp.render(context)
    return HttpResponse(res_html)


def detail(requet, book_id):
    book = BookInfo.objects.get(id=book_id)
    # print(book)
    # heros = HeroInfo.objects.filter(hbook = book_id)
    heros = book.heroinfo_set.all()
    context = {'heros': heros,'book':book}
    return render(requet, 'booktest/index4.html', context)

def create(request):
    # add a book in mysql and display in web page
    book = BookInfo()
    book.btitle = "笑傲江湖"
    book.isDelete = False
    book.bpub_date = datetime.now()
    book.bcomment = 25
    book.bread = 32
    book.save()
    return  HttpResponseRedirect('/index3')


def delete(request, book_id):
    # delete from mysql by click 'delete'
    book = BookInfo.objects.get(id=book_id)
    book.delete()
    return HttpResponseRedirect('/index3')


def areas(request):
    area = AreaInfo.objects.get(atitle='广州市')
    parent = area.aParent
    children = area.areainfo_set.all()
    # use template
    context = {'area':area,'parent':parent,'children':children}
    return render(request,'booktest/areas.html',context)


def my_index(request):
    return render(request,'booktest/my_index.html',{})



def login(request):
    # 获取cookie
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
        password = request.COOKIES['password']
    else:
        username = ''
        password = ''
    return render(request, 'booktest/login.html', {'username':username,'password': password})

def login_check(request):
    #1，获取提交的用户名密码
    username = request.POST['username']
    password = request.POST['password']
    remember = request.POST.get('remember')
    print(remember)
    #2，进行登录验证
    if username =='hongbiao' and password== '123456':
        # 判断是否需要记住用户名
        response = redirect('/index3')
        if remember =='on':
            # 设置过期时间
            response.set_cookie("username",username,max_age=3600*24*1)
            response.set_cookie("password",password,max_age=3600*24*1)
        return response
        # return redirect('/index3')  HttpResponse
    else:
        #用户名密码错误
        return redirect('/login')
        #3，返回应答

    # request.POST 保存post方式提交的参数
    # request.GET 保存get方式提交的参数
    # return  HttpResponse('ok')

def ajax_test(request):
    return render(request, 'booktest/test_ajax.html',{})


def ajax_handle(request):
    # ajax请求处理
    return JsonResponse({'res':1})

def login_ajax(request):
    return render(request,'booktest/login_ajax.html')
def login_ajax_check(request):
    print("-------------1")
    '''ajax登陆校验'''
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 进行校验
    print(username)
    print(password)
    if username=='hongbiao' and password=='123':
        print("----success")
        return JsonResponse({'res':1})
    else:
        print("----failed")
        return JsonResponse({'res':0})
    # 返回接送数据
#反向解析操作
def ntest_reverse(request):
    # 重定向
    # return redirect('/index')
    # url = reverse('booktest:index')
    # return redirect(url)

    # 重定向带参数

    url = reverse('booktest:index', kwargs={'c':3,'d':5})
    return redirect(url)

# /show_upload 上传照片
def show_upload(request):

    return render(request,'booktest/upload_pic.html')

def upload_handle(request):
    # 上传的照片处理
    # 1, 获取上传的照片
    pic = request.FILES['pic']
    # 2，创建一个文件
    # pic.name 是照片的名字
    # pic。chunks()是每次从内存中读取的一块内存
    save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT,pic.name)
    with open(save_path,"wb") as f:
        # 将上传的文件写到所创建的文件中
        for content in pic.chunks():
            f.write(content)
    PicTest.objects.create(goods_pic="booktest/%s"%pic.name)
    # 在数据库保存上传的记录
    return HttpResponse("ok")

def show_areas(request,book_id):
    # 分页
    # 1.查询出所有的省级地区
    area = AreaInfo.objects.filter(aParent__isnull=True)
    # 分页，每页显示6条数据
    paginator = Paginator(area,6)

    # 返回总页数
    print(paginator.num_pages)
    #返回页码的列表
    print(paginator.page_range)
    if book_id=='':
        book_id = 1
    else:
        book_id = int(book_id)
    # 获取第一页的数据
    page = paginator.page(book_id)
    # 当前页的页码
    print("当前页码")
    print(page.number)
    '''
    page.has_previous 判断当前页是否有上一页
    page.has_next 判断当前页是否有下一页
    page.previous_page_name 返回前一页的页码
    page.next_page_number 返回下一页的页码
    '''
    # 2.使用模板
    return render(request,'booktest/show_area.html',{'pages':page})


def  country_area(request):
    # 省市县选中案例
    return render(request,'booktest/country_area.html')

# prov
def prov(request):
    # 获取所有的省级地区
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 将变量area拼接成json数据:
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))
    # 返回数据
    return JsonResponse({'data':area_list})


def citxys(request,pid):
    #获取pid的下级地区的id
    # area = AreaInfo.objects.get(id=pid)
    areas = AreaInfo.objects.filter(aParent__id =pid)
    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))
    # 返回数据
    print("=================================")
    print(areas_list)
    return JsonResponse({'data':areas_list})


def diss(request,pid):
    #获取pid的下级地区
    areas = AreaInfo.objects.filter(aParent__id=pid)
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))
    # 返回数据
    print("=================================")
    print(area_list)
    return JsonResponse({'data': area_list})