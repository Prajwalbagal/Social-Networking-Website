from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import forms, models
from django.contrib import messages

from friends.models import Friend
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()
# Create your views here.


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')

class SearchView(generic.ListView):
    model = User
    template_name = 'posts/list_of_users.html'
    context_object_name = 'all_search_results'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user_name = self.request.GET.get('search', '')
        try:
            friendobj=Friend.objects.get(current_user=self.request.user)

        except ObjectDoesNotExist:
            friends=None
        else:
            friends=friendobj.users.all()
        if user_name:
            context['all_search_results'] = User.objects.filter(username__icontains=user_name )
            context['friends']=friends
            return context



class UserPost(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(
                username__iexact=self.kwargs.get('username')
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group','image')
    model = models.Post
    success_url=reverse_lazy('posts:all')
    def form_valid(self, form):


        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
