
# urls.py
from django.urls import path
from myapp import views
from django.contrib import admin
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('report_spam/', views.SpamReportView.as_view(), name='report_spam'),
    path('search/', views.ContactSearchView.as_view(), name='contact_search'),
      path('login/', views.LoginView.as_view(), name='login'),
       path('logout/', views.LogoutView.as_view(), name='logout'),
         path('admin/', admin.site.urls),
]
