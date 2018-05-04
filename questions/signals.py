from .models import Notification, Answer, Question, Log
from courses.models import Exam, Feedback
from internship.models import Internship
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Answer, dispatch_uid="create_notification_item")
def exam_addition_trigger(instance, **kwargs):
    notification = Notification(question_id=instance.to_question, user_id=instance.to_question.created_by)
    notification.save()
    print("notification created")


@receiver(post_save, sender=Question, dispatch_uid="create_question_item")
def question_addition_trigger(instance, **kwargs):
    log = Log(log_type=Log.QUESTION, log_ref=instance.pk)
    log.save()
    print("Question created")


@receiver(post_save, sender=Exam, dispatch_uid="create_exam_item")
def assignment_addition_trigger(instance, **kwargs):
    log = Log(log_type=Log.EXAM, log_ref=instance.course.pk)
    log.save()
    print("Exam created")


@receiver(post_save, sender=Feedback, dispatch_uid="create_feedback_item")
def feedback_addition_trigger(instance, **kwargs):
    log = Log(log_type=Log.FEEDBACK, log_ref=instance.course.pk)
    log.save()
    print("Feedback created")


@receiver(post_save, sender=Internship, dispatch_uid="create_feedback_item")
def internship_addition_trigger(instance, **kwargs):
    log = Log(log_type=Log.INTERNSHIP, log_ref=instance.pk)
    log.save()
    print("Internship created")
