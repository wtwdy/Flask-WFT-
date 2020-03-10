"""

File:app.py
Author:wangduoyu
Date:2020-03-04
Connect:854429157@qq.com
Description:

"""
from flask import Flask, render_template, flash

from forms import LoginForm,RegisterForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# 设置配置
app.config.from_pyfile('config.py')
# 实例化bootstrap对象
bootstrap = Bootstrap(app)

@app.route('/login/',methods=['GET','POST'])
def login():
    # 实例化表单对象
    form = LoginForm()
    # 1). 判断是否为post方法提交数据
    # 2). 是否通过验证函数
    if form.validate_on_submit():
        # 获取表单数据(内容)
        email = form.email.data
        password = form.password.data
        if email == 'westos@qq.com' and password == 'westos':
            flash("登录成功")
            return '登录成功'
        else:
            # flash('登录失败')
            # return render_template('login.html')
            return '登录失败'
    else:
        # 将form表单传递给html,按照表单的规则进行验证
        return render_template('bs_login.html',form=form)

@app.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return '获取性别%s' %(form.gender.data)
    else:
        return render_template('register.html',form=form)
# def register():
#         return '注册'

@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run()




