from django.urls import path
from . import views
from .views import userreqCreateView
from .views import (
    userreqListView,
    userreqDetailView,
    userreqUpdateView,
    userreqDeleteView,
)

urlpatterns = [
    path('', userreqListView.as_view(), name='userreq'),

    path('userreq/new', userreqCreateView.as_view(), name='userreq-create'),
    path('userreq/<str:pk>/', userreqDetailView.as_view(), name='userreq-detail'),
    path('userreq/<str:pk>/update/', userreqUpdateView.as_view(), name='userreq-update'),
    path('userreq/<str:pk>/delete/', userreqDeleteView.as_view(), name='userreq-delete'),

]