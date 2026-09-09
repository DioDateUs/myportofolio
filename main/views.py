from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Deodatus Kevin Sihaloho",
        "npm": "2506590920",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Fasilkom UI yang aktif dalam berorganisasi, memiliki ketertarikan dalam mengajar, meskipun untuk sekarang ketertarikan itu hanya ditujukan kepada adik kelas secara cuma-cuma."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Deodatus Kevin Sihaloho",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)