from .models import Notification, Answer
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Answer, dispatch_uid="create_notification_item")
def exam_addition_trigger(instance, **kwargs):
    notification = Notification(question_id=instance.to_question, user_id=instance.to_question.created_by)
    notification.save()
    print("notification created")