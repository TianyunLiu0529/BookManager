from django.shortcuts import render

"""
所谓的视图 就是python函数
视图函数有2个要求：
    1. 视图函数的底一个参数是接受请请求，这个请求其实就是HttpRequest的类对象
    2. 必须返回一个响应
"""
# Create your views here.
# request
from django.http import HttpRequest
from django.http import HttpResponse


# 我们希望用户输入http://127.0.0.1:8000/index/
# 来访问视图函数
def index(request):
    # return HttpResponse("ok")
    # 渲染 render(request, template name, context=None)
    # request
    # template name
    # context=None
    context = {
        'name': "70% discount, seize the chance!!!"
    }
    return render(request, 'book/index.html', context=context)
