from django.shortcuts import render, redirect, reverse
from .models import User
from .forms import *

# Create your views here.
'''
实现了以下接口：
1. 登录：login
2. 首页：index
3. 注册：register
4. 登出：logout
'''


# 输入参数的合法性校验，TODO
# def _review_inputs(userid, password):
#     print(f'[INFO] userid={userid}')
#     if userid is None or password is None:
#         return False
#     return True


def login(request):
    if request.session.get('is_login', None):
        return redirect(reverse('user_infos:index'))

    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        message = ''
        print(login_form.errors)

        if login_form.is_valid():
            userid = login_form.cleaned_data.get('userid')
            password = login_form.cleaned_data.get('password')

            try:
                user = User.objects.get(userid=userid)
            except:
                message = 'User not found...'
                return render(request, 'user_infos/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['userid'] = userid
                request.session['password'] = password
                return redirect(reverse('user_infos:index'))
            else:
                message = 'Password invalid...'
                return render(request, 'user_infos/login.html', locals())

        else:
            print('missing')
            return render(request, 'user_infos/login.html', locals())

    login_form = UserLoginForm()
    message = 'Please check input! '
    return render(request, 'user_infos/login.html', locals())


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'user_infos/index.html')


def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        message = ''
        if register_form.is_valid():
            userid = register_form.cleaned_data.get('userid')
            password = register_form.cleaned_data.get('password')
            password_confirm = register_form.cleaned_data.get('password_confirm')

            if password_confirm != password:
                message = 'Please input your password again! '
                return render(request, 'user_infos/register.html', locals())
            else:
                same_id = User.objects.filter(userid=userid)
                if same_id:
                    message = 'Userid already exists! '
                    return render(request, 'user_infos/register.html', locals())
                else:
                    user = User()
                    user.userid = userid
                    user.password = password
                    user.name = register_form.cleaned_data.get('name')
                    user.email = register_form.cleaned_data.get('email')
                    user.save()
                    return redirect('/login/')
        else:
            return render(request, 'user_infos/register.html', locals())
    register_form = UserRegisterForm()
    message = 'Please check input! '
    return render(request, 'user_infos/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush() # 也可以用python内置的del方法
    return redirect('/login/')
