from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from .models import Ads, Feedback


class PublicationForm(forms.ModelForm):
    class Meta:
       model = Ads
       fields = [
           'category',
           'choice_field',
           'pub_title',
           'pub_text',
           'pub_content'
       ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
                'reaction_text',
                'reaction_to_pub',
                # 'reaction_user'
                  ]


class UserForm(forms.ModelForm):
   class Meta:
       model = User
       fields = [
           'email',
           'username',
           'first_name',
           'last_name',
       ]


class CommonSignupForm(SignupForm):
    '''
    Здесь мы импортировали класс формы, который предоставляет allauth, а также
    модель групп. В кастомизированном классе формы, в котором мы хотим добавлять
    пользователя в группу, мы должны переопределить только метод save(), который
    выполняется при успешном заполнении формы регистрации
    '''
    def save(self, request):
        user = super(CommonSignupForm, self).save(request) #вызываем этот же метод
        # класса-родителя, чтобы необходимые проверки и сохранение в модель User
        # были выполнены
        common_group = Group.objects.get(name='common') #получаем объект модели группы common
        common_group.user_set.add(user) #через атрибут user_set, возвращающий список всех пользователей этой
        # группы, мы добавляем нового пользователя в эту группу.
        return user #Обязательным требованием метода save() является возвращение
        # объекта модели User по итогу выполнения функции



