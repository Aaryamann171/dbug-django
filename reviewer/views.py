from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def welcome_view(request, *args, **keywordargs):
    return render(request, 'welcome.html', {})


def home_view(request, *args, **keywordargs):
    return render(request, 'home.html', {})


def pending_view(request, *args, **keywordargs):
    return render(request, 'pending.html', {})


def request_new_view(request, *args, **keywordargs):
    username_list = [e.username for e in User.objects.all()]
    context = {
        "username_list": username_list
    }
    return render(request, 'review_request.html', context)


def reviewed_view(request, *args, **keywordargs):
    return render(request, 'reviewed.html', {})


def team_view(request, *args, **keywordargs):
    return render(request, 'team.html', {})


def about_view(request, *args, **keywordargs):
    return render(request, 'about.html', {})


def contact_view(request, *args, **keywordargs):
    return render(request, 'contact.html', {})
