from django.urls import path
from . import views
from .views import bankreqCreateView
from .views import (
    bankreqListView,
    bankreqDetailView,
    bankreqUpdateView,
    bankreqDeleteView,
)

urlpatterns = [
    path('', views.bank, name='bank'),

    path('bank/new', bankreqCreateView.as_view(), name='bank-create'),
    path('bank/<str:pk>/', bankreqDetailView.as_view(), name='bank-detail'),
    path('bank/<str:pk>/update/', bankreqUpdateView.as_view(), name='bank-update'),
    path('bank/<str:pk>/delete/', bankreqDeleteView.as_view(), name='bank-delete'),

]