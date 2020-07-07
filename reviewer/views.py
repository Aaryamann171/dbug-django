from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import ReviewRequest

import smtplib
from email.message import EmailMessage


def welcome_view(request, *args, **keywordargs):
    return render(request, 'welcome.html', {})


def home_view(request, *args, **keywordargs):
    return render(request, 'home.html', {})


# def pending_view(request, *args, **keywordargs):
#     return render(request, 'pending.html', {})
def pending_view(request, *args, **keywordargs):
    user = request.user.username
    code_snippet = [e.code for e in ReviewRequest.objects.all()
                    if e.req_to == user]

    cs = ''.join(code_snippet)
    req_from = [e.req_from for e in ReviewRequest.objects.all()
                if e.req_to == user]
    rf = ''.join(req_from)

    # context = {"cs": cs, "rf": rf}
    context = {"cs": code_snippet, "rf": req_from}
    return render(request, 'pending.html', context)


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


def send_review_request_mail(code, reviewer_id, comment):
    to_send = EmailMessage()

    msg = "Hi " + str(reviewer_id) + "!\n\n" + \
        "This automated message was sent to you because you have a new Review Request!\n\n" + \
        "Details are as follows -\nCode: " + str(code) + "\nComments: \n" + str(comment) + "\n\n" + \
        "Have a nice day!\nTeam d.bug"

    to_send.set_content(msg)

    to_send['From'] = "reviewalert.dbug@gmail.com"
    to_send['To'] = "akshitsarin99@gmail.com, aaryamann171@gmail.com"
    to_send['Subject'] = "d.bug : New Review Request Recieved!"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("reviewalert.dbug@gmail.com", "CAPstonepelter@123")
    s.send_message(to_send)


def send_request(request):
    context = {}

    if request.method == 'POST':
        data = {
            'codeInput': request.POST.get('codeInput'),
            'reviewerInput': request.POST.get('reviewerInput'),
            'commentInput': request.POST.get('commentInput')
        }

        context = data

        send_review_request_mail(
            data['codeInput'],
            data['reviewerInput'],
            data['commentInput']
        )

    return render(request, 'mail_sent.html', context)
