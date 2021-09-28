from django.test import TestCase
from django.test import Client
from db_models.models import Show
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.user = User.objects.create_user('imdb', 'imdb@moviemad.com', 'imdb1234')

    def test_home_template_rendered(self):
        # Issue a GET request.
        response = self.client.get('')

        # Check that the response is 200 OK.
        self.assertTemplateUsed(response, 'homepage/homepage.html')

    def test_login_template_rendered(self):
        # Issue a GET request.
        response = self.client.get('/login')

        # Check that the response is 200 OK.
        self.assertTemplateUsed(response, 'user_page/login.html')

    def test_home_template_rendered_after_login(self):
        # Issue a GET request.
        response = self.client.post('/login',{'username' : 'imdb' , 'password' : 'imdb1234'})

        # Check that the response is 200 OK.
        self.assertTemplateUsed(response, 'homepage/homepage.html')

    def test_register_template_rendered(self):
        # Issue a GET request.
        response = self.client.get('/register')
	
        # Check that the response is 200 OK.
        self.assertTemplateUsed(response, 'user_page/register.html')

    def test_post_register_template_rendered(self):
        # Issue a GET request.
        response = self.client.post('/register',{'username' : 'chandru' , 'password1' : 'imdb1234', 'password2' : 'imdb1234', 'userGrp' : 'user', 'first_name' : 'Test', 'last_name': 'User', 'email' : 'test@mail.com'},follow=True)
        message = list(response.context.get('messages'))[0]
        # Check that the response is 200 OK.
        self.assertTemplateUsed(response, 'user_page/register.html')

    def test_post_register_message_rendered(self):
        # Issue a GET request.
        response = self.client.post('/register',{'username' : 'chandru' , 'password1' : 'imdb1234', 'password2' : 'imdb1234', 'userGrp' : 'user', 'first_name' : 'Test', 'last_name': 'User', 'email' : 'test@mail.com'},follow=True)
        message = list(response.context.get('messages'))[0]
        # Check that the response is 200 OK.
        self.assertEqual(message.message,'Account was created, successfully')