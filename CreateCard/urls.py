from django.conf.urls import url, include
from .views import (Index,
                    ViewCard)

app_name = 'create-card'

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^view-card$', ViewCard.as_view(), name="view"),
]
