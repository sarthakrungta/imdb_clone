from django.db import models
from django.contrib.auth.models import User

 # Create your models here.

class UserGrp(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    user_type = models.TextField()

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'user_grp'


class Account(models.Model):
    username = models.CharField(primary_key=True, max_length = 40)
    password = models.CharField(max_length = 40, blank=True, null=True)
    email = models.CharField(max_length = 40, blank=True, null=True)
    country = models.CharField(max_length = 40, blank=True, null=True)
    gender = models.CharField(max_length = 40, blank=True, null=True)
    first_name = models.CharField(max_length = 40, blank=True, null=True)
    last_name = models.CharField(max_length = 40, blank=True, null=True)

    class Meta:
        db_table = 'account'

class CreditsRoll(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING)
    role = models.CharField(max_length=45)
    show = models.ForeignKey('Show', models.DO_NOTHING)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    character_name = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.show.show_title + " :: " + self.role

    class Meta:
        db_table = 'credits_roll'


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length = 40)
    role = models.CharField(max_length = 40)
    birthdate = models.DateField()
    bio = models.CharField(max_length = 40)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'person'


class ProductionCompany(models.Model):
    proco_id = models.AutoField(primary_key=True)
    proco_name = models.CharField(max_length = 40)

    def __str__(self):
        return self.proco_name
    
    class Meta:
        db_table = 'production_company'


class Show(models.Model):
    showid = models.AutoField(primary_key=True)
    show_title = models.CharField(max_length = 40)
    genre = models.CharField(max_length = 40)
    length = models.DecimalField(max_digits=5, decimal_places=2)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    movie = models.IntegerField()
    series = models.IntegerField()
    proco = models.ForeignKey(ProductionCompany, models.DO_NOTHING, null=True)
    year = models.IntegerField()
    image_url = models.CharField(max_length = 1000)
    status = models.BooleanField()
    def __str__(self):
        return self.show_title

    class Meta:
        db_table = 'show'


class UserReview(models.Model):
    reviewid = models.AutoField(db_column='reviewId', primary_key=True)  # Field name made lowercase.
    show_id = models.IntegerField()
    user_id = models.CharField(max_length = 40)
    rating = models.IntegerField()
    review = models.CharField(max_length = 40)
    date = models.DateTimeField()
    name = models.TextField()
    
    def __str__(self):
        return str(self.reviewid)
    
    class Meta:
        db_table = 'user_review'