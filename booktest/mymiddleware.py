from django.http import HttpResponse
from django.utils import deprecation

class BlockIPSMiddleware(deprecation.MiddlewareMixin):
    '''中间件'''
    EXCLUDE_IPS = ['192.168.60.26']
    # 服务器响应第一个请求的时候调用
    # def __init__(self):
    #     pass
    # 本次将要执行的view函数被调用前调用本函数
    def process_view(self, request, view_func, *view_args, **view_kwargvs):
        print("-------------------------process_view")
        '''在调用试图之前会调用这个函数'''
        user_ip = request.META['REMOTE_ADDR']  # 获取请求的IP地址
        print(user_ip)
        if user_ip in self.EXCLUDE_IPS:
            return HttpResponse('<h1>你被禁止访问了</h1>')

    # 请求到来的时候调用
    def process_request(self, request):
        print("-------------------------process_request")
    # 在执行完本view函数准备将响应发到客户端前被执行
    def process_response(self,request,response):
        print("-------------------------process_response")
        return response
    #view函数在抛出异常的死后该函数被调用，得到的exception参数是实际上抛出的异常实例
    def process_exception(self,request,exception):
        print("-------------------------process_exception")
        return exception