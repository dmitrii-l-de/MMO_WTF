from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)        #Категории новостей/статей темы, которые они отражают;

    def __str__(self):
        return f'{self.category_name}'


class Ads(models.Model):
    ads = 'A'
    news = 'N'
    CHOICES = [
        (ads, 'Объявление'),
        (news, 'Новость'),
    ]
    pub_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    choice_field = models.CharField(max_length=2, choices=CHOICES, default=news)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')
    pub_title = models.CharField(max_length=255, verbose_name='Post title')
    pub_text = models.TextField(verbose_name='Post_text')
    pub_content = models.ImageField(upload_to='images/')
    category = models.ManyToManyField(Category, through='AdsCategory')

    def get_absolute_url(self):
        return reverse('pub_list', args=[str(self.id)])


class AdsCategory(models.Model):
    ac_publication = models.ForeignKey(Ads, on_delete=models.CASCADE)           #связь «один ко многим» с моделью Ads;
    ac_category = models.ForeignKey(Category, on_delete=models.CASCADE)   #связь «один ко многим» с моделью Category;

    def __str__(self):
        return f'Публикация: {self.ac_publication}\nКатегория: {self.ac_category}'


class Feedback(models.Model):
    considered = 'Р'
    accept = 'П'
    rejected = 'О'
    CHOICE_REACTION = [
        (considered, 'На рассмотрении'),
        (accept, 'Принято'),
        (rejected, 'Отклонено'),
    ]
    reaction_to_pub = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name='comments')
    reaction_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction_text = models.TextField(default="Ваше сообщение")
    reaction_pub_date = models.DateTimeField(auto_now_add=True)
    reaction_status = models.CharField(max_length=2, choices=CHOICE_REACTION, default=considered)

