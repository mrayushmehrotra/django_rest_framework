
# urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('report_spam/', views.SpamReportView.as_view(), name='report_spam'),
    path('search/', views.ContactSearchView.as_view(), name='contact_search'),
]
