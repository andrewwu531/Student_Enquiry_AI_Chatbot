""" context processor for passing data to the base template """
from django.contrib.auth.decorators import login_required


def user_data(request):
    from .models import UserProfile

    if request.user.is_authenticated:
        return {'user_p': UserProfile.objects.get(user= request.user)}
    else:
        return {'user_p': UserProfile.objects.none()}