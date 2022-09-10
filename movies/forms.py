from django import forms
from django.contrib.auth import get_user_model
from movies.models import MovieNight


UserModel = get_user_model()

class SearchForm(forms.Form):
    term = forms.CharField(required=False)

class MovieNightForm(forms.ModelForm):
    class  Meta:
        model = MovieNight
        fields = ["start_time"]