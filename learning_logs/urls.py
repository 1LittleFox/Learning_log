""" Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # path that shows all topics
    path('topics/', views.topics, name='topics'),

    # detail page for a single topic based on id
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),

    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Страница для редактирования записей
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]