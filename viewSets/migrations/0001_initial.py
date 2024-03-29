# Generated by Django 4.1.6 on 2024-02-28 11:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='author1', max_length=200)),
                ('age', models.PositiveIntegerField(default=99)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('biography', models.TextField(default='defaut_biography', max_length=1000)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='defaut_title', max_length=200)),
                ('publication_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='defaut_description', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=6)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_author', to='viewSets.author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
