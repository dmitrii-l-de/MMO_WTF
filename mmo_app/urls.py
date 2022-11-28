from django.contrib import admin
from django.urls import path, include

from .views import AdsList, CreateAdd, UpdateAdd, DetailAdd, DeleteAdd, FeedbackCreate, FeedbackDelete

urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('create/', CreateAdd.as_view(), name='create'),
    path('<int:pk>/update/', UpdateAdd.as_view(), name='update'),
    path('<int:pk>/detail', DetailAdd.as_view(), name='detail'),
    path('<int:pk>/delete/', DeleteAdd.as_view(), name='delete'),
    path('<int:pk>/send_feedback/', FeedbackCreate.as_view(), name='send_feedback'),
    path('<int:pk>', FeedbackDelete.as_view(), name='feedback_delete'),
]
