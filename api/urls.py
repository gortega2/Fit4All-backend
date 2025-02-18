from django.urls import path
from api import views

urlpatterns = [
    path('tags/', view=views.TagsList.as_view()),
    path('equipment/', view=views.EquipmentList.as_view()),
    path('guides/', view=views.GuideList.as_view()),
    path('guides/<int:pk>/', view=views.GuideDetail.as_view()),
    path('exercises/', view=views.ExerciseList.as_view()),
    path('exercises/<int:pk>', view=views.ExerciseDetail.as_view())
]