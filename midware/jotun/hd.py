from django.utils.deprecation import MiddlewareMixin

class Mymiddle(MiddlewareMixin):
    def process_request(self,request):
        print('get 参数为：',request.GET.get('a'))