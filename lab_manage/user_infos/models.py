from django.db import models


# Create your models here.
class User(models.Model):
    userid = models.CharField(verbose_name='用户id', max_length=32, unique=True)
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['ctime']
        verbose_name = '用户'
        verbose_name_plural = '用户'
