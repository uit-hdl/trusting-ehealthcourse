# webapp/urls.py
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import home_view, schizophrenia_view, schizophrenia_symptoms_view, schizophrenia_positive_symptoms_view, schizophrenia_negative_symptoms_view, schizophrenia_cognitive_symptoms_view, schizophrenia_end_view, relapse_view, relapse_characteristics_view, relapse_triggers_view, relapse_warnings_view, relapse_management_view, relapse_end_view, errors_view, course_end_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('schizophrenia/', schizophrenia_view, name='schizophrenia'),
    path('schizophrenia-symptoms/', schizophrenia_symptoms_view, name='schizophrenia-symptoms'),
    path('schizophrenia-positive-symptoms/', schizophrenia_positive_symptoms_view, name='schizophrenia-positive-symptoms'),
    path('schizophrenia-negative-symptoms/', schizophrenia_negative_symptoms_view, name='schizophrenia-negative-symptoms'),
    path('schizophrenia-cognitive-symptoms/', schizophrenia_cognitive_symptoms_view, name='schizophrenia-cognitive-symptoms'),
    path('schizophrenia-end/', schizophrenia_end_view, name='schizophrenia-end'),
    path('relapse/', relapse_view, name='relapse'),
    path('relapse-characteristics/', relapse_characteristics_view, name='relapse-characteristics'),
    path('relapse-triggers/', relapse_triggers_view, name='relapse-triggers'),
    path('relapse-warnings/', relapse_warnings_view, name='relapse-warnings'),
    path('relapse-management/', relapse_management_view, name='relapse-management'),
    path('relapse-end/', relapse_end_view, name='relapse-end'),
    path('errors/', errors_view, name='errors'),
    path('course-end/', course_end_view, name='course-end'),
]

urlpatterns += staticfiles_urlpatterns()