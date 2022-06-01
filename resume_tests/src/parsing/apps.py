from django.apps import AppConfig


class ScrapingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parsing'
    verbose_name = 'Приложение по сбору резюме'

