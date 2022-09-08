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
