from django.urls import path, include
from . import views
urlpatterns = [
   path('',views.home, name="home"),
   path('registration/',views.registration, name='registration'),
   path('verified/<str:token>',views.verified),
   path('login/', views.login, name='login'),
   path('create_event/', views.create_event, name='create_event'),
   path('view_event/', views.view_event, name='view_event'),
   path('profile/', views.profile, name='profile'),
   path('logout/',views.logout, name="logout"),
   path('approve_event/<int:id>/', views.approve_event, name='approve_event'),
   path('event/<int:id>/', views.event_details, name='event_details'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('edit/<int:id>', views.EditEvent, name="edit"),
   path('apply/<int:id>', views.apply_event, name='apply')
]