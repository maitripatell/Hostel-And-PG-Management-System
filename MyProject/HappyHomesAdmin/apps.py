from django.apps import AppConfig


class HappyhomesadminConfig(AppConfig):
    name = 'HappyHomesAdmin'


    def ready(self):
        import 'HappyHomesAdmin'.signals
