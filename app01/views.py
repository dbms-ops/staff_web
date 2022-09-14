from http.client import HTTPResponse
from importlib.resources import path
from tkinter import Widget

from django import forms
from django.shortcuts import redirect, render

from app01 import models

# Create your views here.


def depart_list(request):
    """部门列表

    Args:
        request (_type_): _description_
    """
    # 在数据库中获取所有的部门列表
    #
    querySet = models.Department.objects.all()

    return render(request, 'depart_list.html', {"querySet": querySet})


def depart_add(request):
    """添加部门

    Args:
        request (_type_): _description_
    """
    if request.method == "GET":

        return render(request, 'depart_add.html')
    # 获取用户 post 提交的数据（title 为空）
    title = request.POST.get("title")
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向到部门列表

    return redirect("/depart/list")


def depart_delete(request):
    """删除部门名

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    # http://127.0.0.1:8080/depart/del/?nid=1101
    # 通过 GET 获取 nid
    nid = request.GET.get('nid')
    print(nid)
    # 删除对应的元素
    models.Department.objects.filter(id=nid).delete()

    return redirect("/depart/list/")


def depart_edit(request, nid):
    """修改部门信息

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    # 根据 nid 获取对应的数据
    if request.method == "GET":
        row_obj = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"row_obj": row_obj})

    # 处理 POST 请求
    new_title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=new_title)

    return redirect("/depart/list/")


def user_list(request):
    """用户列表

    Args:
        request (_type_): _description_
    """
    if request.method == "GET":
        querySet = models.UserInfo.objects.all()
        return render(request, 'user_list.html', {"querySet": querySet})


def user_add(request):
    """添加用户

    Args:
        request (_type_): _description_
    """
    if request.method == "GET":
        context = {
            "gender_choices": models.UserInfo.gender_choices,
            "depart_list": models.Department.objects.all(),
        }

        return render(request, "user_add.html", context)

    # 获取用户提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("account")
    ctime = request.POST.get("ctime")
    gender = request.POST.get("gender")
    depart_id = request.POST.get("department")

    # 添加到数据库中
    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime, gender=gender, depart_id=depart_id)

    # 返回到用户列表页面
    return redirect("/user/list/")


class UserModelForm(forms.ModelForm):

    # 用户名最小长度为 3
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age",
                  "account", "create_time", "gender", "depart"]
        # widgets = {
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),

        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环查找所有插件，并且添加样式 {"class": "form-control"}
        for name, field in self.fields.items():
            # if name == "password":
            #     continue
            field.widget.attrs = {
                "class": "form-control", "placeholder": field.label}


def user_model_form_add(request):
    """添加用户 基于 modelForm 版本

    Args:
        request (_type_): _description_
    """
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "user_model_form_add.html", {"form": form})
    # 对于 POST 提交的数据进行校验
    form = UserModelForm(data=request.POST)
    # 数据提交合法：保存导数据库
    if form.is_valid():
        print(form.cleaned_data)
        # 对于合法的数据自定进行保存，不需要 create
        form.save()
        return redirect('/user/list')
    # 校验失败，在页面上显示对应的错误信息
    # 错误信息在 form 中保存，再次返回该页面
    return render(request, "user_model_form_add.html", {"form": form})


def user_edit(request, nid):
    """编辑用户

    Args:
        request (_type_): _description_
    """
    # 获取 nid 对应行的数据
    row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(instance=row_object)
    
    return render(request, "user_edit.html", {"form": form})