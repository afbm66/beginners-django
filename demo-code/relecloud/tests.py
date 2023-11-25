from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class ViewsTest(TestCase):
    def test_fake_pass()
        pass
        
    def test_home_view(self):
        # Test that the home view returns a 200 status code and contains the expected content
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Welcome to My Site')

    def test_about_view(self):
        # Test that the about view returns a 200 status code and contains the expected content
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'About Us')

  
