from django.shortcuts import render
from accounts.models import UserAccounts
import pika
import redis

def chat(request):
    name_nav = UserAccounts.objects.filter(user_account_id=request.user.id)
    context = {
        'name_nav': name_nav
    }
    return render(request, 'mpages/chat.html', context)