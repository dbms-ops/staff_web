import imp
from http.client import HTTPResponse

from django.shortcuts import render

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

    return render(request,'depart_add.html')
