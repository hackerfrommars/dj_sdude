from django.contrib import admin
from .models import Internship


class InternshipAdmin(admin.ModelAdmin):
    list_display = ["created_by", "title", "created_at", "content"]

    class Meta:
        model = Internship


admin.site.register(Internship, InternshipAdmin)
