from django.forms import DateInput, ModelForm, Select, TextInput, Textarea, URLInput
from main.models import Experience, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "organization",
            "category",
            "description",
            "photo",
            "ended_at",
        ]
        labels = {
            "title": "Posisi / Role",
            "organization": "Nama Organisasi / Perusahaan",
            "category": "Kategori Pengalaman",
            "description": "Deskripsi Pekerjaan / Pengalaman",
            "photo": "URL Foto / Logo Organisasi",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "organization": TextInput(
                attrs={
                    "placeholder": "Contoh: PT Teknologi Maju Bersama",
                    "maxlength": 255,
                }
            ),
            "category": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Jelaskan peran dan tanggung jawab yang kamu jalankan...",
                    "rows": 4,
                }
            ),
            "photo": URLInput(
                attrs={
                    "placeholder": "https://example.com/logo.png",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }
