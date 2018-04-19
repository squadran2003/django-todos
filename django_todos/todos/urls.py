
from django.urls import path
from .views import *

app_name = 'todos'

urlpatterns = [
    path('add/',TodoCreateView.as_view(),name='add'),
    path('completed/',TodoCompletedView.as_view(),name='completed'),
    path('edit/<int:pk>/',TodoUpdateView.as_view(),name='edit'),
    path('detail/<int:pk>/',TodoDetailView.as_view(),name='detail'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='delete'),
    path('change_status/<int:pk>/',TodoStatusView.as_view(),name='status'),
    path('signup/',RegisterView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',logoutView.as_view(),name='logout')
    
]

