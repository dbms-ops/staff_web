from operator import mod

from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表
        title
    Args:
        models (_type_): _description_
    """
    # id = models.BigAutoField(primary_key=True, verbose_name="ID 自增主键")
    title = models.CharField(max_length=32, verbose_name="部门名称")


class UserInfo(models.Model):
    """员工表

    Args:
        models (_type_): _description_
    """
    name = models.CharField(max_length=32, verbose_name="员工姓名")
    password = models.CharField(max_length=64, verbose_name="用户登录密码")
    age = models.SmallIntegerField(verbose_name="员工年龄")
    account = models.DecimalField(
        verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 1. 创建外键约束
    # - to：与某张表进行关联
    # - to_field：与表中的某些列进行关联
    # 2. django 自动
    # - 定义的是 depart
    #  - MySQL 生成的数据列为 depart_id
    # 3. 如果部门表的某行被删除，用于列如何处理：
    #   级联删除：depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    #   设置为空：depart = models.ForeignKey(
    #   to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    depart = models.ForeignKey(
        to="Department", to_field="id", on_delete=models.CASCADE)
    