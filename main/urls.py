from django.urls import path

from main.views import (
    create_experience,
    create_interest,
    create_project,
    delete_experience,
    delete_interest,
    delete_project,
    edit_experience,
    edit_interest,
    get_experiences_json,
    get_interests_json,
    get_projects_json,
    show_experience,
    show_interest,
    show_main,
    show_projects,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experiences_json, name="get_experiences_json"),
    path("interest/", show_interest, name="show_interest"),
    path("interest/add/", create_interest, name="create_interest"),
    path("interest/<uuid:interest_id>/edit/", edit_interest, name="edit_interest"),
    path("interest/<uuid:interest_id>/delete/", delete_interest, name="delete_interest"),
    path("api/interest/", get_interests_json, name="get_interests_json"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
]
