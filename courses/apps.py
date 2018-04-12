from __future__ import unicode_literals
from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'courses'

    def ready(self):
        print("@@@ready@@@")
        import courses.signals