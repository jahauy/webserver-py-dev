# django projects
## 目录
### 1. lab_manage
实验室系统管理程序
#### 登录界面
![image](https://user-images.githubusercontent.com/91482240/200115257-048f84c6-56d5-4901-ae2a-ddfe38dfb3e8.png)

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
