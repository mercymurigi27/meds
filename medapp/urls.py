from django.urls import path, include
from . import views
from .views import *




urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-records/', views.Record, name='record'),
    path('profile/<username>', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search_record , name='search'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('single_record<record_id>', views.single_record, name='single-record'),
    path('new-record/', views.create_record, name='new-record'), 




]    