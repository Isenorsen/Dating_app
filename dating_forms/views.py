from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import UserAccounts
from dating_forms.models import DatingForm
from django.core.paginator import Paginator
from .forms import AddForm
from django.contrib import messages

def my_forms(request):
    if request.user.is_authenticated:
        forms = DatingForm.objects.filter(user=UserAccounts.objects.get(user_account_id=request.user.id))
        name_nav = UserAccounts.objects.filter(user_account_id=request.user.id)
        context = {
            'name_nav': name_nav,
            'forms': forms,
        }
        return render(request, 'mpages/my_forms.html', context)
    else:
        return redirect('login')

def create_form(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = AddForm(request.POST, request.FILES)
            name_nav = UserAccounts.objects.filter(user_account_id=request.user.id)
            context = {
                'form': form,
                'name_nav': name_nav,
            }
            return render(request, 'mpages/create_form.html', context)
        else:
            form = AddForm(request.POST, request.FILES)
            if form.is_valid:
                title = request.POST['title']
                text = request.POST['text']
                image1 = request.FILES.get('image1')
                image2 = request.FILES.get('image2')
                image3 = request.FILES.get('image3')
                obj = DatingForm.objects.create(
                    user=UserAccounts.objects.get(user_account_id=request.user.id),
                    title=title, 
                    text=text, 
                    image1=image1, 
                    image2=image2, 
                    image3=image3
                    )
                obj.save()
                messages.add_message(request, messages.INFO, 'Анкета успешно создана')
                return redirect('forms')
            else:
                messages.add_message(request, messages.ERROR, 'Форма заполнена неправильно')
                return redirect('')
    else:
        return redirect('login')