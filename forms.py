from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError


class LoginForm(FlaskForm):
    email = StringField(label='电子邮箱',
                        validators=[
                            DataRequired(message='邮箱不能为空'),
                            Length(1,15, message='长度不符合条件'),
                            Email(message='请输入有效的邮箱地址,比如username@domain.com')
                        ])
    password = PasswordField(label='密码',
                             validators=[
                                 DataRequired(message='密码不能为空')])
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    name = StringField(
        label='用户名',
        validators=[DataRequired(message='用户名不能为空'),
                    Length(5,12,message='用户名长度必须在5-12之间')]
    )
    password = PasswordField(
        label='密码',
        validators=[DataRequired(),
                    Length(6,16,message='密码格式不正确')]
    )

    repassword = PasswordField(
        label='确认密码',
        validators=[DataRequired(),
                    # 验证当前表单输入密码和password表单输入密码是否一致,如果不一致,报错
                    EqualTo('password',message='密码不一致')]
    )
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired(),
            Email(message='邮箱格式错误')
        ]
    )
    phone = StringField(
        label='电话号码',
        validators=[
            DataRequired(),
            Regexp(r'1\d{10}',message='电话号码格式错误')
        ]
    )
    # 下拉单选框
    gender = SelectField(
        label='性别',
        # 填写的信息传入后台的类型
        coerce=int,
        # 下拉列表的选项
        choices=[(1,'男'),(2,'女')]
    )
    # # 下拉多选框
    tech = SelectMultipleField(
        label='擅长领域',
        coerce=int,
        choices=[(1,'python'),(2,'linux'),(3,'php'),(4,'java')]
    )
    def validate_name(self,field):
        # field.data是用户输入的数据
        if field.data == 'admin':
            # ValidationError用来向用户显示错误信息
            # 验证的函数的名称由validate_fieldname组成
            raise ValidationError('超级管理员已经被注册,换一个吧')
    submit = SubmitField(label='注册')

