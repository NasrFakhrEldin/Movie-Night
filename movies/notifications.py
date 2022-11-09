from django.template.loader import render_to_string
from django.urls import reverse
from urllib.parse import urljoin
from django.conf import settings
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone
from movies.models import MovieNight




def send_invitation(movie_night_invitation):
    subject = render_to_string(
        "movies/notifications/invitation_subject.txt",
        {
            "movie_night": movie_night_invitation.movie_night,
        },
    )

    movie_night_path = reverse(
        "movie_night_detail_ui",
        args=(movie_night_invitation.movie_night.pk,)
    )

    body = render_to_string(
        "movies/notifications/invitation_body.txt",
        {
            "creator": movie_night_invitation.movie_night.creator,
            "movie_night": movie_night_invitation.movie_night,
            "movie_night_url": urljoin(settings.BASE_URL, movie_night_path),
        },
    )

    

    # subject, message, from_email, recipient_list
    send_mail(
        subject,
        body,
        None,
        [movie_night_invitation.invitee.email],
        fail_silently = False
    )


def send_attendance_change(movie_night_invitation, is_attending):
    subject = render_to_string(
        "movies/notifications/attendance_update_subject.txt",
        {
            "movie_night": movie_night_invitation.movie_night,
            "movie_night_invitation": movie_night_invitation,
        },
    )

    movie_night_path = reverse(
        "movie_night_detail_ui",
        args=(movie_night_invitation.movie_night.pk,)
    )

    body = render_to_string(
        "movies/notifications/attendance_update_body.txt",
        {   
            "is_attending": is_attending,
            "movie_night_invitation": movie_night_invitation,
            "creator": movie_night_invitation.movie_night.creator,
            "movie_night": movie_night_invitation.movie_night,
            "movie_night_url": urljoin(settings.BASE_URL, movie_night_path),
        },
    )

    send_mail(
        subject,
        body,
        None,
        [movie_night_invitation.movie_night.creator.email],
        fail_silently = False
    )


def send_starting_notification(movie_night):
    subject = render_to_string(
        "movies/notifications/starting_subject.txt",
        {
            "movie_night": movie_night,
        },
    )

    movie_night_path = reverse(
        "movie_night_detail_ui",
        args=(movie_night.pk,)
    )

    body = render_to_string(
        "movies/notifications/starting_body.txt",
        {
            "movie_night": movie_night,
            "movie_night_url": urljoin(settings.BASE_URL, movie_night_path),
        },
    )

    to_emails = [invite.invitee.email for invite in movie_night.invites.filter(is_attending=True)]
    to_emails.append(movie_night.creator.email)

    send_mail(
        subject,
        body,
        None,
        to_emails,
        fail_silently = False
    )

    movie_night.start_notification_sent = True
    movie_night.save()


def notify_of_starting_soon():
    # Find all that start in the next 30 minutes, or before, if we haven't notified
    start_berfore = timezone.now() + timedelta(minutes=30)

    movie_nights = MovieNight.objects.filter(
        start_time__lte = start_berfore,
        start_notification_sent=False
    )

    for movie_night in movie_nights:
        send_starting_notification(movie_night)
