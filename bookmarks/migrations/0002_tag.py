# Generated by Django 3.0.6 on 2020-05-28 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('bookmarks', models.ManyToManyField(to='bookmarks.Bookmark')),
            ],
        ),
    ]