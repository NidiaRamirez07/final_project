from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Video, HashTag
from .forms import VideoForm

class VideoFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Hashtag object for testing
        content_type = ContentType.objects.get_for_model(Video)  # Adjust the model name
        permission = Permission.objects.get(content_type=content_type, codename='add_video')
        cls.user = User.objects.create_user('testuser', password='testpassword')
        cls.user.user_permissions.add(permission)
        cls.hashtag = HashTag.objects.create(name='TestHashtag')

    def test_valid_form_submission(self):
        self.client.login(username='testuser', password='testpassword')
        video_content = b'Video content'
        video_file = SimpleUploadedFile("video.mp4", video_content)

        form_data = {
            'name': 'Sample Video',
            'video_file': video_file,
            'description': 'Test video description',
            'hashtags': [self.hashtag.id],
        }
        response = self.client.post(reverse('add_new_video'), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Video.objects.filter(name='Sample Video').exists())

    def test_blank_form(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {}
        response = self.client.post(reverse('add_new_video'), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200) 

    def test_missing_video_file(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'name': 'Sample Video No File',
            'description': 'Test video description',
            'hashtags': [self.hashtag.id],
        }
        response = self.client.post(reverse('add_new_video'), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(Video.objects.filter(name='Sample Video No File').exists())
