# Generated by Django 3.2.3 on 2021-05-22 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('username', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('gender', models.CharField(blank=True, max_length=40, null=True)),
                ('first_name', models.CharField(blank=True, max_length=40, null=True)),
                ('last_name', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=40)),
                ('role', models.CharField(max_length=40)),
                ('birthdate', models.DateField()),
                ('bio', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='ProductionCompany',
            fields=[
                ('proco_id', models.AutoField(primary_key=True, serialize=False)),
                ('proco_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'production_company',
            },
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('reviewid', models.AutoField(db_column='reviewId', primary_key=True, serialize=False)),
                ('show_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=40)),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=40)),
                ('date', models.DateTimeField()),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'user_review',
            },
        ),
        migrations.CreateModel(
            name='UserGrp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_grp',
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('showid', models.AutoField(primary_key=True, serialize=False)),
                ('show_title', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=40)),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('movie', models.IntegerField()),
                ('series', models.IntegerField()),
                ('year', models.IntegerField()),
                ('image_url', models.CharField(max_length=1000)),
                ('status', models.BooleanField()),
                ('proco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.productioncompany')),
            ],
            options={
                'db_table': 'show',
            },
        ),
        migrations.CreateModel(
            name='CreditsRoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=45)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('character_name', models.CharField(blank=True, max_length=45, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.person')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_models.show')),
            ],
            options={
                'db_table': 'credits_roll',
            },
        ),
    ]
