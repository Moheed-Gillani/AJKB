# Generated by Django 3.1.2 on 2020-10-11 10:51

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('on', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=10)),
                ('Image', models.ImageField(null=True, upload_to='')),
                ('User', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reply', models.TextField()),
                ('on', models.DateField(auto_now=True, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profiles')),
                ('on_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('headline', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profiles'),
        ),
        migrations.AddField(
            model_name='comment',
            name='on_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post'),
        ),
    ]
