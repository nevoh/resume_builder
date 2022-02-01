from django.shortcuts import (
    get_object_or_404, render, HttpResponseRedirect, redirect)

from .models import (Education, Experience, Resume,
                     Achievement, Language, Skill)
from .forms import (EducationForm, ExperienceForm,
                    AchievementForm, LanguageForm, SkillForm)


def resume_builder(request):
    resume = get_object_or_404(Resume, user=request.user)
    print(resume)
    context = {
        'resume': resume,
        'experiences': resume.experiences.all(),
        'skills': resume.skills.all(),
        'educations': resume.educations.all(),
        'languages': resume.languages.all(),
        'achievements': resume.achievements.all(),
    }
    return render(request, 'resume/resume_builder.html', context)


def educations_view(request):
    resume = get_object_or_404(Resume, user=request.user)
    form = EducationForm(request.POST or None,)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.resume = resume
            new.save()
            return HttpResponseRedirect("/educations")

    context = {
        "educations": resume.educations.all(),
        'form': form,
    }
    return render(request, 'resume/educations.html', context)


def update_education(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    education = get_object_or_404(Education, resume=resume, pk=pk)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/educations")
    context = {
        'resume': resume,
        'form': form,
    }
    return render(request, "resume/update_education.html", context)


def delete_education(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    education = Education.objects.get(pk=pk, resume=resume)
    education.delete()
    return HttpResponseRedirect('/educations')


def experiences_view(request):
    resume = get_object_or_404(Resume, user=request.user)
    form = ExperienceForm(request.POST or None,)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.resume = resume
            new.save()
            return HttpResponseRedirect("/experiences")
    context = {
        "experiences": resume.experiences.all(),
        'form': form,
    }
    return render(request, 'resume/experiences.html', context)


def update_experience(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    experience = get_object_or_404(Experience, resume=resume, pk=pk)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/experiences")
    context = {
        'resume': resume,
        'form': form,
    }
    return render(request, "resume/update_experience.html", context)


def delete_experience(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    experience = Experience.objects.get(pk=pk, resume=resume)
    experience.delete()
    return HttpResponseRedirect('/experiences')


def achievements_view(request):
    resume = get_object_or_404(Resume, user=request.user)
    form = AchievementForm(request.POST or None,)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.resume = resume
            new.save()
            return HttpResponseRedirect("/achievements")
    context = {
        "achievements": resume.achievements.all(),
        'form': form,
    }
    return render(request, 'resume/achievements.html', context)


def update_achievement(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    achievement = get_object_or_404(Achievement, resume=resume, pk=pk)
    form = AchievementForm(request.POST or None, instance=achievement)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/achievements")
    context = {
        'resume': resume,
        'form': form,
    }
    return render(request, "resume/update_achievement.html", context)


def delete_achievement(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    achievement = Achievement.objects.get(pk=pk, resume=resume)
    achievement.delete()
    return HttpResponseRedirect('/achievements')


def languages_view(request):
    resume = get_object_or_404(Resume, user=request.user)
    form = LanguageForm(request.POST or None,)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.resume = resume
            new.save()
            return HttpResponseRedirect("/languages")
    context = {
        "languages": resume.languages.all(),
        'form': form,
    }
    return render(request, 'resume/languages.html', context)


def update_language(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    language = get_object_or_404(Language, resume=resume, pk=pk)
    form = LanguageForm(request.POST or None, instance=language)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/languages")
    context = {
        'resume': resume,
        'form': form,
    }
    return render(request, "resume/update_language.html", context)


def delete_language(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    language = Language.objects.get(pk=pk, resume=resume)
    language.delete()
    return HttpResponseRedirect('/languages')


def skills_view(request):
    resume = get_object_or_404(Resume, user=request.user)
    form = SkillForm(request.POST or None,)
    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            new.resume = resume
            new.save()
            return HttpResponseRedirect("/skills")
    context = {
        "skills": resume.skills.all(),
        'form': form,
    }
    return render(request, 'resume/skills.html', context)


def update_skill(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    skill = get_object_or_404(Skill, resume=resume, pk=pk)
    form = SkillForm(request.POST or None, instance=skill)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/skills")
    context = {
        'resume': resume,
        'form': form,
    }
    return render(request, "resume/update_skill.html", context)


def delete_skill(request, pk):
    resume = get_object_or_404(Resume, user=request.user)
    skill = Skill.objects.get(pk=pk, resume=resume)
    skill.delete()
    return HttpResponseRedirect('/skills')
