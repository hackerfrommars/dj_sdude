from .models import Exam, Feedback
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Feedback, dispatch_uid="create_feedback_item")
def exam_addition_trigger(instance, **kwargs):
    print("Feedback created and instance content is ", instance.content)