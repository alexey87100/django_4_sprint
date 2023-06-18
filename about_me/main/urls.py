from django.urls import path

from .views import index, skill

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('skill/<int:skill_id>/', skill, name='skill')

]
