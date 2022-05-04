import json
from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#使用ajax对jquery的支持，load方法把页面load_test的内容动态加载到load_test_server页面里面
def load_test(request):
    return render(request,'load_test.html')

def load_test_server(request):
    return render(request,'load_test_server.html')

def jquery_get(request):
    return render(request,'jquery_get.html')

def jquery_get_server(request):
    #获取get 请求传递过来的参数
    if request.method =='GET':
        uname = request.GET.get('uname','NO data')#这里的第二个参数表示获取传递过来的参数没有拿到时给的默认值
        age = request.GET.get('age','NO data')
        d = {"uname":uname,"age":age}
    if request.method == 'POST':
        d = {"uname":"defind_uname","age":"defind_age"}

    return HttpResponse(json.dumps(d), content_type='application/json')

def jquery_post(request):
    return render(request,'jquery_post.html')

def jquery_post_server(request):
    if int(request.POST.get('age',0)) > 100:
        d = {"msg": "your age is big ", "code": 201}
        return HttpResponse(json.dumps(d),content_type='application/json')
    d = {"msg":"post is ok ","code":200}
    return HttpResponse(json.dumps(d),content_type='application/json')

def jquery_ajax(request):
    return render(request,'jquery_ajax.html')

def jquery_ajax_server(request):
    sleep(3)#模拟取数据的时候阻塞状态
    d = {'name':'xiaowang','age':18}
    return HttpResponse(json.dumps(d),content_type='application/json')

def cross(request):
    return render(request,'cross.html')

def cross_server(request):

    func = request.GET.get('callback')
    return HttpResponse(func + "('wo kua chu lai le ')")#返回字符串回前端，这里返回的字符串的格式是 func('wo kua chu lai le ')这里返回的内容是前端加载script标签的结果，这个结果会被解析成调用func函数