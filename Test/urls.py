from django.conf.urls import url, include
from .views import Test

app_name = 'test'

urlpatterns = [
    # for testing purpose only
    url(r'^$', Test.as_view(), name='test')
]