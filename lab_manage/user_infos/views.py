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
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        message = 'Please check input! '

        if login_form.is_valid():
            userid = login_form.cleaned_data.get('userid')
            password = login_form.cleaned_data.get('password')
            try:
                user = User.objects.get(userid=userid)
                if user.password == password:
                    return redirect(reverse('user_infos::index'))
                else:
                    message = 'Password invalid...'
            except:
                message = 'User not found...'
    else:
        login_form = UserLoginForm()
    return render(request, 'user_infos/login.html', locals())


def index(request):
    pass
    return render(request, 'user_infos/index.html')


def register(request):
    pass
    return render(request, 'user_infos/register.html')
#
#
# def logout(request):
#     pass
#     return redirect('/login/')
