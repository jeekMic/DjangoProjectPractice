from django.urls import path
from . import views

urlpatterns = [
    # 登陆成功
    path('success/', views.success),
    # ajax登陆
    path('login_ajax/', views.login_ajax),
    # ajax登陆校验
    path('login_ajax_checks/', views.login_ajax_checks),
    # 生产校验码url
    path('verify_code/',views.verify_code),
    # fatie的页面
    path('post_article/', views.post_article),
    path('myfilter/', views.myfilter),
    path('htmlescape/', views.htmlescape),
    path('staticfile/', views.staticfile),


]