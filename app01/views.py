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
    context = {
        "gender_choices":models.UserInfo.gender_choices,
        "depart_list":models.Department.objects.all(),
    }

    return render(request,"user_add.html",context)
