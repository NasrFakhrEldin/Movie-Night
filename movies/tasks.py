from celery import shared_task
from movies import notifications
from movies.models import MovieNightInvitaion


@shared_task
def send_invitaion(mni_pk):
    notifications.send_invitation(
        MovieNightInvitaion.objects.get(pk=mni_pk)
    )


@shared_task
def send_attendance_change(mni_pk, is_attending):
    notifications.send_attendance_change(
        MovieNightInvitaion.objects.get(pk=mni_pk),
        is_attending
    )


@shared_task
def notify_of_starting_soon():
    notifications.notify_of_starting_soon()