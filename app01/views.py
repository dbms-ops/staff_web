import imp
from http.client import HTTPResponse

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

