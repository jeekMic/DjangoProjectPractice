from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from booktest.models import BookInfo,HeroInfo,AreaInfo
from datetime import datetime
# Create your views here.

# http://127.0.0.1:8000/index
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

