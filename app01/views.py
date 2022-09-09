from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def depart_list(request):
    """部门列表

    Args:
        request (_type_): _description_
    """

    return render(request,'depart_list.html')

