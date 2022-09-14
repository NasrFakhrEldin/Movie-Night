from django_celery_beat.models import IntervalSchedule, PeriodicTask


# this will be run from management command to execute this function
def schedule_setup():
    interval_schedule = IntervalSchedule.objects.create(
        every=1, period=IntervalSchedule.MINUTES
    )

    PeriodicTask.objects.create(
        task="movies.tasks.notify_of_starting_soon",
        interval=interval_schedule
    )

    # or add it from DJANGO ADMIN