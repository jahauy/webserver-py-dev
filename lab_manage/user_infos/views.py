from django.shortcuts import render, redirect, reverse

# Create your views here.
'''
实现了以下接口：
1. 登录：login
2. 首页：index
3. 注册：register
4. 登出：logout
'''


def login(request):
    pass
    return render(request, 'user_infos/login.html')

#
# def index(request):
#     pass
#     return render(request, '')
#
#
# def register(request):
#     pass
#     return render(request, '')
#
#
# def logout(request):
#     pass
#     return redirect('/login/')
