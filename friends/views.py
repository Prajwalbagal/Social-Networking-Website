from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect# Create your views here.
from django.contrib.auth import get_user_model
from friends.models import Friend
from django.core.exceptions import ObjectDoesNotExist
User=get_user_model()
def friendoperation(request,operation,pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.makefriend(request.user, new_friend)
    elif operation == 'remove':
        Friend.losefriend(request.user, new_friend)
    return redirect('friends:listfriends')

def listfriends(request):

    try:
        friendobj=Friend.objects.get(current_user=request.user)

    except ObjectDoesNotExist:
        friends=None
    else:
        friends=friendobj.users.all()
    if friends:
        args={'friends':friends,'exist':True}
    else:
        args={'friends':'No Friends','exist':False}
    return render(request,'friends/listfriends.html',args)
