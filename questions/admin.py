from django.contrib import admin
from .models import Question, Answer, Notification


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["created_by", "content", "created_at"]

    class Meta:
        model = Question


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["created_by", "content", "to_question", "created_at"]

    class Meta:
        model = Answer


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["question_id", "is_active", "user_id"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Notification, NotificationAdmin)