from django.test import TestCase
from django.test import Client
from db_models.models import Show,ProductionCompany
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class UserReviewTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.user = User.objects.create_user('imdb', 'imdb@moviemad.com', 'imdb1234')
        proco = ProductionCompany()
        proco.proco_id = 1
        proco.proco_name = 'Demo Company'
        proco.save()
        show = Show()
        show.show_title = 'Demo title'
        show.genre = 'Action'
        show.length = 2.4
        show.movie = 1
        show.series = 0
        show.proco_id = '1'
        show.year = 2020
        show.image_url = ''
        show.status = 1
        show.save()

    def test_review_template_rendered(self):
        # Issue a GET request.
        response = self.client.get('/add_review')

        # Check that the response is 200 OK.
        self.assertTemplateUsed(response, 'review_page/reviewPage.html')

    def test_add_valid_review(self):
        # Issue a GET request.
        self.client.post('/login',{'username' : 'imdb' , 'password' : 'imdb1234'})
        response = self.client.post('/movie_details/1', {
            'rating' : '3',
            'review' : 'Good'
            },follow=True)
        getResponse = self.client.get('/movie_details/1')
        reviewCount = list(getResponse.context.get('reviews'))
        # Check that the response is 200 OK.
        self.assertEqual(len(reviewCount), 1)

    def test_add_multiple_review_by_user(self):
        # Issue a GET request.
        self.client.post('/login',{'username' : 'imdb' , 'password' : 'imdb1234'})
        response1 = self.client.post('/movie_details/1', {
            'rating' : '3',
            'review' : 'Good'
            })
        response2 = self.client.post('/movie_details/1', {
            'rating' : '3',
            'review' : 'Good'
            })
        getResponse = self.client.get('/movie_details/1')
        reviewCount = list(getResponse.context.get('reviews'))
        # Check that the response is 200 OK.
        self.assertEqual(len(reviewCount), 1)

    def test_add_invalid_review(self):
        with self.assertRaises(ValueError):
         # Issue a GET request.
         self.client.post('/login',{'username' : 'imdb' , 'password' : 'imdb1234'})
         # Check that the response is 200 OK.
         self.client.post('/movie_details/1', {
            'rating' : 'a',
            'review' : 'Good'
            },follow=True)