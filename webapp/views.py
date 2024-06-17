from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _


def home_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'home.html', context)

def schizophrenia_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'schizophrenia.html', context)

def schizophrenia_symptoms_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'schizophrenia-symptoms.html', context)

def schizophrenia_positive_symptoms_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'schizophrenia-positive-symptoms.html', context)

def schizophrenia_negative_symptoms_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'schizophrenia-negative-symptoms.html', context)
    
def schizophrenia_cognitive_symptoms_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'schizophrenia-cognitive-symptoms.html', context)

def schizophrenia_end_view(request):
    context = {
    }
    return render(request, 'schizophrenia-end.html', context)

def relapse_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'relapse.html', context)

def relapse_characteristics_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'relapse-char.html', context)

def relapse_triggers_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'relapse-triggers.html', context)

def relapse_warnings_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'relapse-warnings.html', context)

def relapse_management_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'relapse-management.html', context)

def relapse_end_view(request):
    context = {
        'incorrect_msg': _("<strong>Incorrect</strong><br>You have selected an incorrect option."),
        'correct_msg': _("<strong>Correct</strong><br>You have selected a correct option.")
    }
    return render(request, 'relapse-end.html', context)

def errors_view(request):
    context = {
    }
    return render(request, 'errors.html', context)

def course_end_view(request):
    context = {
    }
    return render(request, 'course-end.html', context)