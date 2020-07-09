from django.contrib import admin
from django.urls import path, include
from reviewer.views import home_view, pending_view, welcome_view, team_view, about_view, contact_view, reviewed_view, request_new_view, send_request, review, review_submitted, sent_pending_view, done_for_me_view
from register.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name='home'),
    path("register/", register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('', welcome_view, name='welcome'),
    path('pending', pending_view),
    path('reviewed', reviewed_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('team/', team_view),
    path('request_new/', request_new_view),
    path('sendRequest/', send_request),
    path('review/', review),
    path('review_submitted/', review_submitted),
    path('sent_pending/', sent_pending_view),
    path('done_for_me/', done_for_me_view)
]
