from django.shortcuts import render
from django.http import Http404

from .data import EMPLOYEES, SKILLS


def index(request):
    """Главная страница проекта."""
    new_employees = []
    for employee in EMPLOYEES:
        employee_skills = employee['skills']
        for skill_id in employee_skills:
            ...

    context = {
        'employees': EMPLOYEES,
    }
    return render(request, 'index.html', context=context)


def skill(request, skill_id):
    skill_to_show = None
    for skill in SKILLS:
        if skill_id == skill['id']:
            skill_to_show = skill
    if skill_to_show is None:
        raise Http404("Скила с таким ID не существует")
    
    employees = []
    for employee in EMPLOYEES:
        if skill_id in employee['skills']:
            employees.append(employee)

    context = {
        'skill': skill_to_show,
        'employees': employees,
    }
    return render(request, 'skill.html', context=context)