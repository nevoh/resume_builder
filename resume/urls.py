from django.urls import path
from . import views

urlpatterns = [
    path('resume-builder', views.resume_builder, name='resume-builder'),

    path('educations', views.educations_view, name='educations'),
    path('update_education/<str:pk>',
         views.update_education, name='update_education'),
    path('delete_education/<str:pk>',
         views.delete_education, name='delete_education'),

    path('experiences', views.experiences_view, name='experiences'),
    path('update_experience/<str:pk>',
         views.update_experience, name='update_experience'),
    path('delete_experience/<str:pk>',
         views.delete_experience, name='delete_experience'),

    path('achievements', views.achievements_view, name='achievements'),
    path('update_achievement/<str:pk>',
         views.update_achievement, name='update_achievement'),
    path('delete_achievement/<str:pk>',
         views.delete_achievement, name='delete_achievement'),

    path('languages', views.languages_view, name='languages'),
    path('update_language/<str:pk>',
         views.update_language, name='update_language'),
    path('delete_language/<str:pk>',
         views.delete_language, name='delete_language'),

    path('skills', views.skills_view, name='skills'),
    path('update_skill/<str:pk>',
         views.update_skill, name='update_skill'),
    path('delete_skill/<str:pk>',
         views.delete_skill, name='delete_skill'),
]
