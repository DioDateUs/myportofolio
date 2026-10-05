from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from main.forms import InterestForm
from main.models import Experience, Interest


class MainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="regularuser", password="password123")
        self.superuser = User.objects.create_superuser(username="adminuser", password="password123")

        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            organization="Universitas Indonesia",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.interest = Interest.objects.create(
            title="Backend Development",
            skill="Django, SpringBoot, Node.js",
            image="https://example.com/icon.png",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.organization)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sekarang")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))
        self.assertFalse(self.experience.is_ongoing)
        self.assertNotContains(response, "Sekarang")

    def test_interest_model(self):
        self.assertEqual(str(self.interest), "Backend Development")
        self.assertEqual(self.interest.skill, "Django, SpringBoot, Node.js")

    def test_interest_page_loads_clean_shell(self):
        response = self.client.get(reverse("main:show_interest"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interest.html")
        self.assertContains(response, 'id="interest-search-form"')
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, 'id="loading"')
        self.assertContains(response, 'id="empty"')

    def test_get_interests_json(self):
        response = self.client.get(reverse("main:get_interests_json"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data) >= 1)
        self.assertEqual(data[0]["fields"]["title"], "Backend Development")
        self.assertEqual(data[0]["fields"]["skill"], "Django, SpringBoot, Node.js")

    def test_get_interests_json_search_filter(self):
        response = self.client.get(reverse("main:get_interests_json") + "?title=Backend")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)

        empty_search = self.client.get(reverse("main:get_interests_json") + "?title=NonExistentKeyword")
        self.assertEqual(empty_search.status_code, 200)
        self.assertEqual(len(empty_search.json()), 0)

    def test_create_interest_ajax_unauthorized(self):
        # Anonymous user cannot create interest via AJAX
        response = self.client.post(
            reverse("main:create_interest_ajax"),
            {"title": "DevOps", "skill": "Docker, Kubernetes", "image": ""},
        )
        self.assertEqual(response.status_code, 403)

        # Regular user cannot create interest via AJAX
        self.client.login(username="regularuser", password="password123")
        response = self.client.post(
            reverse("main:create_interest_ajax"),
            {"title": "DevOps", "skill": "Docker, Kubernetes", "image": ""},
        )
        self.assertEqual(response.status_code, 403)

    def test_create_interest_ajax_success(self):
        self.client.login(username="adminuser", password="password123")
        response = self.client.post(
            reverse("main:create_interest_ajax"),
            {"title": "Cloud Computing", "skill": "AWS, GCP", "image": "https://example.com/cloud.png"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Interest.objects.filter(title="Cloud Computing").exists())

    def test_interest_form_sanitization(self):
        form_data = {
            "title": "<script>alert('xss')</script>Mobile Development",
            "skill": "<b>Flutter, Swift</b>",
            "image": "https://example.com/icon.png",
        }
        form = InterestForm(data=form_data)
        self.assertTrue(form.is_valid())
        interest = form.save()
        self.assertEqual(interest.title, "Mobile Development")
        self.assertEqual(interest.skill, "Flutter, Swift")
