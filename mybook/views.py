import random

from PIL import Image, ImageDraw, ImageFont
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from io import StringIO, BytesIO

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def success(request):
    # 用户已经登录
    if request.session.get('islogin'):
        return render(request, 'mybook/success.html')
    else:
        return redirect('/login_ajax/')


def login_ajax(request):
    # 用模板
    response = render_to_response('mybook/login_ajax.html', {})
    response.set_cookie('name', 'hongbiao')
    return response


# ajax的登陆校验视图函数
@csrf_exempt
def login_ajax_checks(request):
    uname = request.POST.get('uname')
    password = request.POST.get('password')
    vcode = request.POST.get('vcode')
    # 获取用户输入的校验码
    vcode_session = request.session.get('verifycode')
    print(uname)
    print(password)
    print(vcode_session)
    # 用户名、密码校验
    if uname == 'hongbiao' and password == '123456' and vcode == vcode_session:
        # 保存用户登录的状态
        request.session['islogin'] = True
        request.session['uname'] = uname
        # request.session['password'] = password
        print("都满足")
        return JsonResponse({'msg': 'ok'})
    elif uname != 'hongbiao' or password != '123456':
        print("新用户，通过验证")
        return JsonResponse({'msg': 'fail_user'})
    elif vcode != vcode_session:
        print("新用户，没有通过验证")
        return JsonResponse({'msg': 'fail_verify'})


# 验证码

def verify_code(request):
    # 定义变量，用于绘制背景色的宽高
    # random.randrange(20,100)意思是在20到100之间随机找一个数
    bgColor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 30
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgColor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点，防止攻击
    for i in range(0, 100):
        # 噪点的绘制范围
        xy = (random.randrange(0, width), random.randrange(0, height))
        # 噪点的随机颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 绘制噪点
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取6个字母作为验证码
    rand_str = ''

    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象

    font = ImageFont.truetype('/static/res/Monaco.ttf', 23)

    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # ,绘制
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)

    # 用完画笔,释放
    del draw
    # 存入session 用作进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端， MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def post_article(request):
    # 获取登录名的用户名
    uname = request.session.get('uname')
    # 获取帖子的标题
    title = request.POST.get('title')
    content = request.POST.get('content')
    return HttpResponse('%s发了一篇名为%s的帖子：%s' % (uname.encode('utf-8').decode('utf-8'),
                                              title.encode('utf-8').decode('utf-8'),
                                              content.encode('utf-8').decode('utf-8')))


def myfilter(request):
    context = {"values":[1,2,3,4,5,6,7,8,9,10,11,12]}
    return render(request,'mybook/myfilter.html', context)