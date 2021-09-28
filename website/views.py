from django.shortcuts import render, redirect
from django.http import HttpResponse
from db_models.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages #import messages
from .forms import NewUserForm, ReviewForm
from datetime import date
from django.db import connection


# Create your views here.
def movie_details(request, show_id=None):
   
    #CREDIT ROLL
    credits = []
    for credit in CreditsRoll.objects.all():
        
        if int(credit.show.showid) == int(show_id):
            credits.append(credit)
        
        
    #RATINGS 
    total_ratings = 0
    reviews_count = 0
    reviews = []
    
    reviewers = []

    for review in UserReview.objects.all():
        if review.show_id == show_id:
            reviewers.append(review.name)
            reviews.append(review)
            total_ratings = total_ratings + review.rating
            reviews_count = reviews_count + 1
    if reviews_count == 0:
        show_rating = "No Ratings Yet"
    else:
        show_rating = total_ratings/reviews_count

    if request.method == 'POST':
            post = UserReview()

            try:
                ratingByUser = int(request.POST.get('rating'))
                if ratingByUser <= 5:
                    if str(post.name) not in reviewers:
                        post.rating = ratingByUser
                        post.review = request.POST.get('review')
                        post.show_id = show_id
                        post.name = request.user
                        post.user_id = request.user.id
                        post.date = date.today()
                        post.save()
                        messages.error(request, "Review Added!")
                    else:
                        messages.error(request, "Review already added")
                else:
                    messages.error(request, "Rating should be less than or equal to 5")
            except:
                messages.error(request, "Enter a valid number")

    context = {'show':Show.objects.get(showid=show_id),'reviews':reviews, 'show_rating':show_rating, 'credits':credits}
    return render(request, 'movie_details/movieDetails.html', context)


def register_request(request):
    form = NewUserForm()
    new_account = Account()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        usrGrp = request.POST.get('userGrp')

        if form.is_valid():
            user = form.save()
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()

            new_account.username = request.POST.get('username')
            new_account.password = request.POST.get('password')
            new_account.email = request.POST.get('email')
            new_account.country = request.POST.get('country')
            new_account.gender = request.POST.get('gender')
            new_account.first_name = request.POST.get('first_name')
            new_account.last_name = request.POST.get('last_name')
            new_account.save()

            #Check User Group
            if usrGrp != 'user':
                user.is_active = False
                user.save()                
            
            user_grp = UserGrp()
            user_grp.user = User.objects.all().last()

            if usrGrp == None:
                user_grp.user_type = 'user'
            else:
                user_grp.user_type = usrGrp

            user_grp.save()
            messages.success(request, 'Account was created, successfully')
       

    context = {'form':form}
    return render(request, 'user_page/register.html', context)

def login_request(request):
    print(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            if user.is_active == False:
                messages.info(request, 'Account not authorized yet')
            return redirect('http://127.0.0.1:8000/') ##HomePage LINK
        else:
            messages.info(request, 'Incorrect username or password')

    context = {}
    return render(request, 'user_page/login.html', context)

def logout_request(request):
    logout(request)
    return render(request=request,
                    template_name = "homepage/homepage.html",
                    context = {"persons":Person.objects.all,"shows":Show.objects.all})

def about(request):
    return render(request=request, template_name = "homepage/about.html", context = {})

def homepage(request):
    search_Result = []
    if request.method == 'POST':
        for i in Show.objects.all():
            print(request.POST.get('search_bar').strip().capitalize() + "-" + i.show_title.strip().capitalize())
            if request.POST.get('search_bar').strip().upper() in i.show_title.capitalize().strip().upper():
                search_Result.append(i)
            
        if len(search_Result) == 0:
            messages.error(request, "No Movie Found")

        return render(request=request,template_name = "homepage/homepage.html",
                      context = {"shows":search_Result})
    else:    
        return render(request=request,template_name = "homepage/homepage.html",
                      context = {"shows":Show.objects.all})

    
def add_review(request):

    if request.method == 'POST':
            post = UserReview()
            post.rating = 3
            post.review = "Good"
            post.show_id = 2
            post.user_id = int(3)
            post.date = date.today()
            post.save()

    context = {}
    return render(request, 'review_page/reviewPage.html', context)

def add_movie(request):
    if request.method == 'POST':
        show = Show()
        show.show_title = request.POST.get('title')
        show.genre = request.POST.get('genre')
        show.length = request.POST.get('length')
        show.year = request.POST.get('year')
        show.image_url = request.POST.get('image_url')
        
        if UserGrp.objects.get(user = request.user).user_type == 'pco' or UserGrp.objects.get(user = request.user).user_type == 'admin':
            show.status = 1
        else:
            show.status = 0
        
        if request.POST.get('proco_id') != "0":
            show.proco_id = request.POST.get('proco_id')
        else:
            show.proco_id = 1 ##PLACEHOLDER FOR

        if request.POST.get('showTypeGrp') == 'movie':
            show.movie = 1
            show.series = 0
        else:
            show.series = 1
            show.movie = 0
        
        try:
            show.save()
        except:
            print("Inavlid Input")

    context = {"pco":ProductionCompany.objects.all()}
    return render(request, 'add_movie/add_movie.html', context)
        

