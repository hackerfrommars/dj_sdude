from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = 'questions'

    def ready(self):
        print("@@@questions ready@@@")
        import questions.signals