from django.contrib import admin

# Register your models here.
from . import models

# 注册进管理员界面
admin.site.register(models.User)
