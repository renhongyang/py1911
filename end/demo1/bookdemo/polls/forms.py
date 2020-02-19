from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3,max_length=12, label="用户名",help_text="用户名最小3位，最大12位")
    password = forms.CharField(min_length=6,max_length=15, label="密码",help_text="用户密码最小6位，最大15位",
                               widget=forms.PasswordInput)


class RegistForm(forms.ModelForm):
    password1 = forms.CharField(label="重复密码",help_text="6-15位",widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["username","password"]
        labels = {"username":"用户名", "password":"密码",}
        help_texts = {
            "username":"3-12位",
            "password":"6-15位",
        }
        widgets = {
            "password":forms.PasswordInput()
        }
