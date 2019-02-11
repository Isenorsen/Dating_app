from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import UserAccounts
from dating_forms.models import DatingForm
from django.core.paginator import Paginator


def index(request):
    if request.user.is_authenticated:
        forms = DatingForm.objects.all()
        paginator = Paginator(forms, 5)
        page = request.GET.get('page')
        form_page = paginator.get_page(page)
        name_nav = UserAccounts.objects.filter(user_account_id=request.user.id)
        context = {
            'name_nav': name_nav,
            'forms': forms,
            'form_page': form_page
        }
        return render(request, 'mpages/index.html', context)
    else:
        return redirect('login')

def search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            queryset_forms = DatingForm.objects.order_by('-date')
            name_nav = UserAccounts.objects.filter(user_account_id=request.user.id)
            context = {
                'name_nav': name_nav,
            }
            return render(request, 'mpages/search.html', context)
        else:
            queryset_forms = DatingForm.objects.order_by('-date')
            
            if 'key' in request.POST:
                key = request.POST['key']
                if key:
                    queryset_forms = DatingForm.objects.filter(text__contains=key)

            if 'name' in request.POST:
                name = request.POST['name']
                if name:
                    users_by_name = UserAccounts.objects.filter(name=name)
                    queryset_forms = DatingForm.objects.filter(user__in=users_by_name)

            if 'age' in request.POST:
                age = request.POST['age']
                if age:
                    users_by_age = UserAccounts.objects.filter(age=age)
                    queryset_forms = DatingForm.objects.filter(user__in=users_by_age)

            if 'city' in request.POST:
                city = request.POST['city']
                if city:
                    users_by_city = UserAccounts.objects.filter(city=city)
                    queryset_forms = DatingForm.objects.filter(user__in=users_by_city)

            context = {
                'queryset_forms': queryset_forms
            }
            return render(request, 'mpages/search_results.html', context)
