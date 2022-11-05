# Django projects
## 目录
### 1. lab_manage
实验室系统管理程序
#### 登录界面
![image](https://user-images.githubusercontent.com/91482240/200118512-5890e233-742b-4d10-bf3a-d882bf29c511.png)

##### 最初的写法
如果用原始的`html`写界面，可以参考：
```html
<div>
<label for="id_userid">用户名：</label><br>
<input type="text" id="id_userid" name="userid" placeholder="请输入用户名" autofocus required/>
</div>
<div>
<label for="id_password">密码：</label><br>
<input type="password" id="id_password" name="password" placeholder="密码不低于6位" required>
</div>
```
在视图里获取表单：
```python
userid = request.POST.get('userid')
password = request.POST.get('password')
```
##### 使用表单的写法
```html
<div>
{{ login_form.as_p }}
</div>
```

```python
login_form = UserLoginForm(request.POST)
...
userid = login_form.cleaned_data.get('userid')
password = login_form.cleaned_data.get('password')
```
