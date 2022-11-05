from django.shortcuts import render, redirect, reverse
from .models import User

# Create your views here.
'''
实现了以下接口：
1. 登录：login
2. 首页：index
3. 注册：register
4. 登出：logout
'''


# 输入参数的合法性校验，TODO
def _review_inputs(userid, password):
    print(f'[INFO] userid={userid}')
    if userid is None or password is None:
        return False
    return True


def login(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        message = 'Please check input! '

        if _review_inputs(userid.strip(), password):
            try:
                user = User.objects.get(userid=userid)
                if user.password == password:
                    return redirect(reverse('user_infos::index'))
                else:
                    message = 'Password invalid...'
            except:
                message = 'User not found...'

        return render(request, 'user_infos/login.html', {'message': message, })
    return render(request, 'user_infos/login.html')


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
