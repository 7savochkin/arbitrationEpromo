from django.urls import path

from pages.views import IndexView, ContactUsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us')
]
