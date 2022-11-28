# Generated by Django 4.1.3 on 2022-11-24 10:38

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
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_field', models.CharField(choices=[('A', 'Объявление'), ('N', 'Новость')], default='N', max_length=2)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date')),
                ('pub_title', models.CharField(max_length=255, verbose_name='Post title')),
                ('pub_text', models.TextField(verbose_name='Post_text')),
                ('pub_content', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_text', models.TextField(default='Ваше сообщение')),
                ('reaction_pub_date', models.DateTimeField(auto_now_add=True)),
                ('reaction_status', models.CharField(choices=[('Р', 'На рассмотрении'), ('П', 'Принято'), ('О', 'Отклонено')], default='Р', max_length=2)),
                ('reaction_to_pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmo_app.ads')),
                ('reaction_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmo_app.category')),
                ('ac_publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmo_app.ads')),
            ],
        ),
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ManyToManyField(through='mmo_app.AdsCategory', to='mmo_app.category'),
        ),
        migrations.AddField(
            model_name='ads',
            name='pub_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
