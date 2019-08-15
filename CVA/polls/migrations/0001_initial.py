# Generated by Django 2.2.4 on 2019-08-15 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titolo')),
                ('bannerImage', models.ImageField(blank=True, upload_to='', verbose_name='Foto banner')),
                ('body_text_1', models.CharField(blank=True, max_length=10000, verbose_name='Testo 1')),
                ('body_text_2', models.CharField(blank=True, max_length=10000, verbose_name='Testo 2')),
                ('pub_date', models.DateTimeField(blank=True, verbose_name='Data di pubblicazione')),
            ],
        ),
        migrations.CreateModel(
            name='FrontPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titolo')),
                ('body_text', models.CharField(max_length=10000, verbose_name='Testo')),
            ],
        ),
        migrations.CreateModel(
            name='FrontPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titolo')),
                ('image', models.ImageField(upload_to='', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titolo')),
                ('body_text', models.CharField(max_length=10000, verbose_name='Testo')),
                ('pub_date', models.DateTimeField(verbose_name='Data di pubblicazione')),
                ('image', models.ImageField(upload_to='', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=100, verbose_name='Titolo')),
                ('image', models.ImageField(upload_to='', verbose_name='Foto')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Article')),
            ],
        ),
    ]
