from django.shortcuts import render
from django.http import HttpResponse


def welcome_view(request, *args, **keywordargs):
    return render(request, 'welcome.html', {})


def login_view(request, *args, **keywordargs):
    return render(request, 'login.html', {})


def home_view(request, *args, **keywordargs):
    return render(request, 'home.html', {})


def pending_view(request, *args, **keywordargs):
    return render(request, 'pending.html', {})


def reviewed_view(request, *args, **keywordargs):
    return render(request, 'reviewed.html', {})


def team_view(request, *args, **keywordargs):
    return render(request, 'team.html', {})


def about_view(request, *args, **keywordargs):
    return render(request, 'about.html', {})


def contact_view(request, *args, **keywordargs):
    return render(request, 'contact.html', {})


def verify(request):
    user_name = (request.POST['n1'])
    password = (request.POST['p1'])
    if user_name == password:
        return render(request, "home.html", {'loggedin': 1})
    else:
        return render(request, "error.html", {'loggedin': 0})
