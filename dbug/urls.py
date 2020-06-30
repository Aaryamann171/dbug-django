from django.contrib import admin
from django.urls import path
from reviewer.views import home_view, login_view, pending_view, verify, welcome_view, team_view, about_view, contact_view, reviewed_view, request_new_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name='home'),
    path('login', login_view, name='login'),
    path('', welcome_view, name='welcome'),
    path('verify', verify, name="verify"),
    path('pending', pending_view),
    path('reviewed', reviewed_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('team/', team_view),
    path('request_new/', request_new_view),
]
