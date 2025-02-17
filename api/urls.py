from django.urls import path
from api import views

urlpatterns = [
    path('tags/', view=views.TagsList.as_view()),
    path('equipment/', view=views.EquipmentList.as_view()),
]