from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied     

from main.forms import ExperienceForm, InterestForm, ProjectForm
from main.models import Experience, Interest, Project
import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Deodatus Kevin Sihaloho",
        "npm": "2506590920",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Fasilkom UI yang aktif dalam berorganisasi, memiliki ketertarikan dalam mengajar, meskipun untuk sekarang ketertarikan itu hanya ditujukan kepada adik kelas secara cuma-cuma."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experiences_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences]

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")


def get_experiences_json(request):
    experiences = Experience.objects.all()
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")


def is_editor_user(user):
    return user.is_authenticated and user.groups.filter(name='Editor').exists()


def show_interest(request):
    json_response = get_interests_json(request)
    interests = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    interests = [item.object for item in interests]

    is_editor = is_editor_user(request.user)
    can_edit = request.user.is_superuser or is_editor
    context = {
        "name": "Deodatus Kevin Sihaloho",
        "interest_list": interests,
        "is_editor": is_editor,
        "can_edit": can_edit,
    }
    return render(request, "interest.html", context)

@login_required(login_url="/login/")
def create_interest(request):
    if not request.user.is_superuser:
        raise PermissionDenied 
        
    form = InterestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Minat berhasil ditambahkan!")
        return redirect("main:show_interest")

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "form": form,
    }
    return render(request, "interest_form.html", context)

@login_required(login_url="/login/")
def edit_interest(request, interest_id):
    if not (request.user.is_superuser or is_editor_user(request.user)):
        raise PermissionDenied
    
    interest = get_object_or_404(Interest, pk=interest_id)
    form = InterestForm(request.POST or None, instance=interest)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Minat berhasil diperbarui!")
        return redirect("main:show_interest")

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "form": form,
        "interest": interest,
    }
    return render(request, "interest_form.html", context)

@login_required(login_url="/login/")
def delete_interest(request, interest_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    interest = get_object_or_404(Interest, pk=interest_id)
    if request.method == "POST":
        interest.delete()
        messages.success(request, "Minat berhasil dihapus!")
        return redirect("main:show_interest")
    return redirect("main:show_interest")


def get_interests_json(request):
    interests = Interest.objects.all()
    interests_json = serializers.serialize("json", interests, use_natural_foreign_keys=True)
    return HttpResponse(interests_json, content_type="application/json")


def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]

    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()

    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json", projects, use_natural_foreign_keys=True  
    )
    return HttpResponse(projects_json, content_type="application/json")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Deodatus Kevin Sihaloho",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_star_interest(request, interest_id):
    interest = get_object_or_404(Interest, pk=interest_id)
    if request.method == "POST":
        if request.user in interest.starred_by.all():
            interest.starred_by.remove(request.user)
        else:
            interest.starred_by.add(request.user)
    return redirect("main:show_interest")
