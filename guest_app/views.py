from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth #后台认证
from django.contrib.auth.decorators import login_required
from guest_app.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    return render(request,"index.html")

def login_action(request):
   if request.method == "POST":
        user_name = request.POST.get("username","")
        pass_word = request.POST.get("password","")
        if user_name == "" or pass_word == "":
            return render(request,"index.html",{
                "hint":"用户名或者密码不能为空~"
            })
        user = auth.authenticate(username=user_name,password=pass_word)
        if user is not None:
            #用户认证通过，用于登录，和login_required装饰器一起用
            auth.login(request,user)
            #重定向   --注意点：这里URL的起始位置加上/,防止重定向时拼接上一次URL
            #向浏览器设置sessionId
            request.session['user'] = user
            return HttpResponseRedirect("/event_manage/")

        else:
            return render(request,"index.html",{
                "hint": "用户名或者密码错误~"
            })
        # if user != "admin"  or pawd !="admin123":
        #     return render(request,"index.html",{
        #         "hint":"用户名或者密码错误！"
        #     })
        # else:
        #     return HttpResponse("登录成功")
   else:
       return HttpResponse(404)

#TODO 添加关闭窗户，必须要登录成功后，才能使用event_manage请求

@login_required
def event_manage(request):
    event_list = Event.objects.all()
    user = request.COOKIES.get('user',"")
    pagintor = Paginator(event_list, 2)
    page = request.GET.get('page')
    try:
        contacts = pagintor.page(page)
    except PageNotAnInteger:
        contacts = pagintor.page(1)
    except EmptyPage:
        contacts = pagintor.page(pagintor.num_pages)
    print("分页器测试：",contacts.number)
    return render(request,"event_manage.html",{
        "user":user,
        "events":event_list,
        "events_page":contacts,
        "page_nums":pagintor.num_pages,
    })
def guest_manage(request):
    guest_list = Guest.objects.all()
    user = request.COOKIES.get('user', "")
    pagintor = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = pagintor.page(page)
    except PageNotAnInteger:
        contacts = pagintor.page(1)
    except EmptyPage:
        contacts = pagintor.page(pagintor.num_pages)
    print("分页器测试：", contacts.number)
    return render(request, "guest_manage.html", {
        "user": user,
        "guests": guest_list,
        "guests_page": contacts,
        "page_nums": pagintor.num_pages,

    })







def search_name(request):
    if request.method == "GET":
        name = request.GET.get("name","")
        print("搜索:",name)
        result = Event.objects.filter(name__contains=name)
        print("搜索结果:",result)
        return render(request,"event_manage.html",{
            "events":result
        })

    else:
        return render(request,"event_manage.html")

def sign_index(request,eid):
    print("签到的活动id", eid)
    event = get_object_or_404(Event,id=eid)

    guest_list = Guest.objects.filter(event_id=eid)
    guest_data = str(len(guest_list))  # 签到人数
    sign_data = 0  # 已签到人数
    for guest in guest_list:
        if guest.sign == True:
            sign_data += 1
    return render(request, 'sign_index.html', {'event': event,
                                               'guest': guest_data,
                                               'sign': sign_data})
def sign_action(request,eid):
    print("签到的活动id",eid)
    event = get_object_or_404(Event,id=eid)
    if request.method == "POST":
        phone = request.POST.get("phone","")
        print("签到的手机",phone)
        result = Guest.objects.filter(phone=phone)
        if not result:
            return render(request,"sign_index.html",{
                "event":event,
                "hit":"手机号不存在！"
            })
        #######注意 filter 与 get的区别
        result = Guest.objects.filter(event_id=eid, phone=phone)
        print("filter获取：",type(result))
        if not result:
            return render(request, "sign_index.html", {
                "event": event,
                "hit": "该手机不是本场发布会参与者"
            })
        result = Guest.objects.get(event_id=eid, phone=phone)
        print("filter获取：", type(result))
        if result.sign:
            return render(request, "sign_index.html", {
                "event": event,
                "hit": "该手机已经签到成功！"
            })
        else:
            result.sign = 1
            result.save()
            return render(request,"sign_index.html",{
                "event":event,
                "hit":"恭喜，签到成功~",
                "user":result
            })

    else:
        return render(request,"sign_index.html",{
            "event":event
        })
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')