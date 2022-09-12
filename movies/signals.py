from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from movies.models import MovieNightInvitaion
from movies.tasks import send_invitaion, send_attendance_change

USE_CELERY = True

@receiver(post_save, sender=MovieNightInvitaion, dispatch_uid="invitation_create")
def invitation_create(sender, created, instance, **kwargs):
    if created:
        if USE_CELERY:
            send_invitaion.delay(instance.pk)
        else:
            send_invitaion(instance.pk)


@receiver(pre_save, sender=MovieNightInvitaion, dispatch_uid="invitation_update")
def invitation_update(sender, instance, **kwargs):
    if not instance.pk:
        # is a new one
        return

    previous_invitation = MovieNightInvitaion.objects.get(pk=instance.pk)
    instance.attendance_confirmed = True

    # only notify if there is a change in attendance
    if previous_invitation.is_attending != instance.is_attending:
        if USE_CELERY:
            send_attendance_change.delay(instance.pk, instance.is_attending)
        else:
            send_attendance_change(instance.pk, instance.is_attending)