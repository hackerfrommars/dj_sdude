from django.contrib import admin

from .models import Course, Professor, Exam

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

admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Exam, ExamAdmin)