from django import forms

from .models import Professor, Exam, Feedback

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('exam_type', 'course', 'professor', 'file')


