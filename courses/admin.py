from django.contrib import admin

from .models import Course, Professor, Exam, Feedback

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = Course

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = Professor

class ExamAdmin(admin.ModelAdmin):
    list_display = ["exam_type", "created_at"]
    list_filter = ["course", "professor"]

    class Meta:
        model = Exam

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["content", "course", "grade", "professor", "created_by"]

    class Meta:
        model = Feedback


admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Feedback, FeedbackAdmin)