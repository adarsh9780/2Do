from django.conf.urls import url
from .views import (About,)

app_name = 'about'

urlpatterns = [
    url(r'^$', About.as_view(), name="about"),
]