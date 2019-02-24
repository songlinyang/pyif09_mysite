"""
这个是用来写接口的

"""

from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import auth #后台认证
#验证登录的接口
def login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        if user_name == "" or pass_word == "":
            return JsonResponse({"success":"true","message":"用户名或密码为空"})
        user = auth.authenticate(username=user, password=pawd)
        if user is not None:
            # 用户认证通过，用于登录，和login_required装饰器一起用
            auth.login(request, user)
            # 重定向   --注意点：这里URL的起始位置加上/,防止重定向时拼接上一次URL
            return JsonResponse({"success":"true","message":"登录成功"})
        else:
            return JsonResponse({"success":"true","message":"用户名或者密码错误！"})
        # if user != "admin"  or pawd !="admin123":
        #     return render(request,"index.html",{
        #         "hint":"用户名或者密码错误！"
        #     })
        # else:
        #     return HttpResponse("登录成功")
    else:
        return JsonResponse({"success":"false","message":"请求方法不正确"})
