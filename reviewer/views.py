from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Pending_Requests

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
    code_snippet = [e.code for e in Pending_Requests.objects.all()
                    if e.req_to == user]

    # cs = ''.join(code_snippet)
    req_from = [e.req_from for e in Pending_Requests.objects.all()
                if e.req_to == user]
    # rf = ''.join(req_from)
    req_id = [e.id for e in Pending_Requests.objects.all()
              if e.req_to == user]

    comments = [e.comments for e in Pending_Requests.objects.all()
                if e.req_to == user]
    data = zip(code_snippet, req_from, comments, req_id)
    # context = {"cs": code_snippet, "rf": req_from,
    #            "comments": comments, "id": req_id, "data": data}
    context = {"data": tuple(data)}
    return render(request, 'pending.html', context)


def request_new_view(request, *args, **keywordargs):
    username_list = [e.username for e in User.objects.all()]
    context = {
        "username_list": username_list
    }
    return render(request, 'review_request.html', context)


def reviewed_view(request, *args, **keywordargs):
    return render(request, 'reviewed.html', {})


def review(request, *args, **keywordargs):
    data = {
        'rid': request.POST.get('req_id'),
        'cs': request.POST.get('code_snippet'),
        'rf': request.POST.get('req_from'),
        'comment': request.POST.get('comment'),
    }
    context = data
    return render(request, 'review_page.html', context)


def team_view(request, *args, **keywordargs):
    return render(request, 'team.html', {})


def about_view(request, *args, **keywordargs):
    return render(request, 'about.html', {})


def contact_view(request, *args, **keywordargs):
    return render(request, 'contact.html', {})


def send_review_request_mail(code, email_id, username, comment):
    to_send = EmailMessage()

    msg = "Hi " + str(username) + "!\n\n" + \
        "This automated message was sent to you because you have a new review request!\n\n" + \
        "Details -\nCode: " + str(code) + "\nComments: \n" + str(comment) + "\n\n" + \
        "Have a nice day!\nTeam d.bug"

    to_send.set_content(msg)

    to_send['From'] = "reviewalert.dbug@gmail.com"
    to_send['To'] = str(email_id)
    to_send['Subject'] = "d.bug : New Review Request Recieved!"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("reviewalert.dbug@gmail.com", "CAPstonepelter@123")
    s.send_message(to_send)


def send_request(request):
    context = {}
    username = request.POST.get('reviewerInput')
    email_id = ""

    # send email notification to reviewer
    for i in User.objects.raw('SELECT * FROM auth_user WHERE username = %s', [username]):
        email_id = i.email

    if request.method == 'POST':
        data = {
            'codeInput': request.POST.get('codeInput'),
            'email_id': email_id,
            'username': username,
            'commentInput': request.POST.get('commentInput')
        }

        context = data

        send_review_request_mail(
            data['codeInput'],
            data['email_id'],
            data['username'],
            data['commentInput']
        )

    # add new request to pending db
    x = Pending_Requests(code=data['codeInput'], req_from=request.user.username,
                         req_to=data['username'], comments=data['commentInput'])
    x.save()

    return render(request, 'mail_sent.html', context)
