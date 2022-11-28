from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from .forms import PublicationForm, FeedbackForm
from .models import Ads, Feedback


class BaseView(TemplateView):
    template_name = 'default.html'


class AdsList(ListView):
    model = Ads
    ordering = '-pub_date'
    template_name = 'main.html'
    context_object_name = 'add'


class DetailAdd(DetailView):
    model = Ads
    form_class = FeedbackForm
    template_name = 'detail.html'
    context_object_name = 'add'


class DeleteAdd(LoginRequiredMixin, DeleteView):
    model = Ads
    template_name = 'delete.html'
    context_object_name = 'add'
    success_url = reverse_lazy('ads_list')


class CreateAdd(LoginRequiredMixin, CreateView):
    model = Ads
    form_class = PublicationForm
    template_name = 'create.html'
    success_url = reverse_lazy('ads_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.pub_author = self.request.user
        obj.save()
        return super().form_valid(form)


class UpdateAdd(LoginRequiredMixin, UpdateView):
    form_class = PublicationForm
    model = Ads
    template_name = 'add_update.html'
    context_object_name = 'add'
    success_url = reverse_lazy('ads_list')


class FeedbackCreate(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    # context_object_name = 'feedback'
    success_url = reverse_lazy('ads_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.reaction_user = self.request.user
        reaction_to_pub = form.cleaned_data['reaction_to_pub']
        # reaction_user = form.cleaned_data['reaction_user']
        reaction_text = form.cleaned_data['reaction_text']
        obj.save()
        return super().form_valid(form)


class PrivatePage(LoginRequiredMixin, ListView):
    template_name = 'private.html'
    model = Ads
    context_object_name = 'fb'

    def __str__(self):
        return f'Публикация: {self.reaction_to_pub}\nКто написал: {self.reaction_user}'


class FeedbackDelete(LoginRequiredMixin, DeleteView):
    model = Feedback
    template_name = 'delete.html'
    success_url = reverse_lazy('private')




