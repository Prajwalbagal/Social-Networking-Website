from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import UserPicture
# Create your views here.
from . import forms
from django.views.generic import CreateView
class ProfileView(generic.CreateView):
    form_class=forms.ProfilePicForm

    success_url = reverse_lazy('posts:all')
    template_name = 'propics/uploadpic.html'
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)
class ProfileList(generic.ListView):
    form_class=forms.ProfilePicForm

    template_name = 'propics/list.html'
    def get_queryset(self):
        return UserPicture.objects.all()
