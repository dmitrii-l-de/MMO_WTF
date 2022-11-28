from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import User, Ads, Feedback


@receiver(post_save, sender=Ads)
# Здесь реализация отправки письма при создании нового поста
def send_new_post_mail(sender, instance, **kwargs) -> None:
    print('test2')
    list_users = User.objects.all()
    print(list_users)
    for user in list_users:
        print(user.email)
        send_mail(
            subject=f"Новый пост от пользователя: {instance.pub_author}",
            message=f"Создан новый пост c заголовком:\n {instance.pub_title}",
            from_email='gbicfo@yandex.ru',
            recipient_list=[user.email],
        )


@receiver(post_save, sender=Feedback)
def send_feedback_to_author(sender, instance, **kwargs) -> None:
    to_post = instance.reaction_to_pub
    owner = Ads.objects.get(id=to_post.id).pub_author_id

    users = User.objects.all()
    for user in users:
        if user.id == owner:
            send_mail(
                subject=f"Пользователь: {instance.reaction_user} оставил коммент к вашей статье",
                message=f"Создан новый коммент:\n {instance.reaction_text}",
                from_email='gbicfo@yandex.ru',
                recipient_list=[user.email],
                )


@receiver(post_save, sender=Feedback)
def send_feedback_to_sender(sender, instance, **kwargs) -> None:
    print('test 4')
    to_post = instance.reaction_to_pub
    user_id = instance.reaction_user_id
    print(user_id)
    users = User.objects.all()
    for user in users:
        if user.id == user_id:
            send_mail(
                subject=f"Ваш комментарий от: {instance.reaction_pub_date} на проверке",
                message=f"Ваш комментарий:\n {instance.reaction_text} находится в статусе {instance.reaction_status}",
                from_email='gbicfo@yandex.ru',
                recipient_list=[user.email],
            )