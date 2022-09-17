# Movie-Night
Movie Night Project aims to make it easier to organize times to watch movies with friends.

# High-level description of the site’s features:

*   Users can register with their email address and a password.

*   Users can log in with their email address.

*   Users can search for a movie by title.
    *   The movie data will be retrieved from **OMDb** if the term has not been searched in the past 24 hours.

*   Users can create a Movie Night for a movie, at a specific date and time.

*   Once a Movie Night is created, other users can be invited by the creator.
    *   Users will receive an invitation email when they’re invited.

*   Users can confirm their attendance or decline the invitation (as well as switch back and forth between these states).
    *   The creator of the Movie Night will receive an email when invitees change their attendance status.

*   Half an hour before a Movie Night is due to start, all the confirmed attendees, and the creator, are emailed a notification.

*   All emailing takes place through Celery. Celery Beat is used for scheduling.

*   A REST API is also implemented.

*   Django Configurations and logging are set up to work as a **12-Factor** app.
