from django.apps import AppConfig


class MmoAppConfig(AppConfig):
    name = 'mmo_app'

    # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import mmo_app.signals