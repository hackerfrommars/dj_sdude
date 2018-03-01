from django import forms

from .models import Professor, Exam, Feedback, Course

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('exam_type', 'professor', 'file')


