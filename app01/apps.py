from django.apps import AppConfig


class App01Config(AppConfig):
    # 自动添加自增主键，不需要手动添加
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app01'
