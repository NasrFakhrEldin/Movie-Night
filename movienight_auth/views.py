from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile(request):
    return render(request, "movienight_auth/profile.html",{
        "page_group":"profile",
    })