from django.shortcuts import render, HttpResponse, redirect
from .github_spider import git_spider
import xlwt
from io import BytesIO
from . import models
from .forms import UserForm, RegisterForm
import hashlib
import time
from django.http import JsonResponse
from .userid_spider import get_userinfo


# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/index/')


def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()




def spider_code(request):
    global user, ow_times
    if request.method == "POST":
        user = request.POST.get('github_name')
        github_url = 'https://api.github.com/users/' + user
        new_task = models.Tasks.objects.create()
        time_local = time.localtime()
        ow_times = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
        new_task.git_name = user + ow_times
        print(user, ow_times)
        new_task.save()

        tasks_lists = models.Tasks.objects.all()
        executing_task = 0
        for task in tasks_lists:
            if task.status == 0:
                executing_task += 1
                if executing_task >= 3:
                    message_executing = "当前已经有两个任务正在执行，请稍后"
                    return render(request,"page.html",{'response_executing':message_executing})

        parsedData, message = git_spider(github_url)
        models.Tasks.objects.filter(git_name=user + ow_times).update(status=1)
        print(parsedData)
        result_task = models.TeskResults.objects.create()
        result_task.name = parsedData[0]['name']
        result_task.blog = parsedData[0]['blog']
        result_task.public_repo_num = parsedData[0]["public_repos"]
        result_task.following_num = parsedData[0]["following"]
        result_task.follower_num = parsedData[0]["followers"]
        result_task.public_gists_num = parsedData[0]["public_gists"]
        result_task.task_id = user + ow_times
        result_task.save()

        return render(request, "page.html", {'data_github': parsedData, 'response_github': message})

    return render(request, "page.html")


def export_data(request):
    if request.method == "POST":
        task_create_time = user + ow_times
        results = models.TeskResults.objects.get(task_id = task_create_time)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=' + 'data.xls'
        ws = xlwt.Workbook(encoding='utf-8')
        # 添加第一页数据表
        w = ws.add_sheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
        # 写入表头
        w.write(0, 0, u'姓名')
        w.write(0, 1, u'博客链接')
        w.write(0, 2, u'公共gits')
        w.write(0, 3, u'粉丝数')
        w.write(0, 4, u'订阅数')
        w.write(0, 5, u'转载数')

        excel_row = 1
        w.write(excel_row, 0, results.name)
        w.write(excel_row, 1, results.blog)
        w.write(excel_row, 2, results.public_repo_num)
        w.write(excel_row, 3, results.following_num)
        w.write(excel_row, 4, results.follower_num)
        w.write(excel_row, 5, results.public_gists_num)

        output = BytesIO()
        ws.save(output)
        output.seek(0)
        response.write(output.getvalue())
        return response


    return render(request,"page.html")


def spider_userid(request):
    if request.method == "POST":
        userid = request.POST.get("userid")
        parsedData, message = get_userinfo(userid)
        print(parsedData)
        return render(request, "page.html", {'data_userid': parsedData, 'response_userid': message})


    return render(request, "page.html")

