# Generated by Django 5.0.4 on 2024-05-26 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Books', 'Books'), ('Authors', 'Authors'), ('Publishers', 'Publishers'), ('Other', 'Other')], max_length=30)),
                ('topic_creation_date_time', models.DateTimeField(auto_now_add=True)),
                ('posts_count', models.PositiveIntegerField(blank=True, null=True)),
                ('topic_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_of_post', models.TextField(max_length=333)),
                ('creation_date_time_of_post', models.DateTimeField(auto_now_add=True)),
                ('editing_date_time_of_post', models.DateTimeField(auto_now_add=True)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_to_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topics')),
            ],
        ),
    ]