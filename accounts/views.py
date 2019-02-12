from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages, auth 
from django.contrib.auth.models import User
from .models import UserAccounts
from .forms import AccountInfo

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "GET":
            return render(request, 'mpages/login.html')
        else:
            email = request.POST['email']
            password = request.POST['password']
            log_user = auth.authenticate(username=email, password=password)
            if log_user is not None:
                auth.login(request, log_user)
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'Логин или пароль введены неверно')
                return redirect('login')

def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            name = request.POST['name']
            city = request.POST['city']
            age = request.POST['age']
            password = request.POST['password1']
            password2 = request.POST['password2']
            
            # Проверка на совпадение паролей и уникальность email

            if password == password2:
                if User.objects.filter(username=email).exists():
                    messages.add_message(request, messages.ERROR, 'На этот email уже зарегистрирован аккаунт')
                    return redirect('registration')
                else:
                    
                    # Юзернейм берется из имейла

                    new_user = User.objects.create_user(username=email, password=password)
                    new_user.save()
                    auth.login(request, new_user)
                    new_account = UserAccounts.objects.create(user_account_id=new_user.id, name=name, age=age, email=email, city=city)
                    new_account.save()
                    return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'Пароли не совпадают')
                return redirect('registration')
        else:
            return render(request, 'mpages/registration.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def user_account(request, user_id):
    if request.user.is_authenticated:
        name_nav = UserAccounts.objects.filter(user_account_id=request.user.id)
        user_info = get_object_or_404(UserAccounts, user_account_id=user_id)
        user = UserAccounts.objects.filter(user_account_id=user_id)
        content = {
            'user_info': user_info,
            'name_nav': name_nav,
            'user': user
        }
        return render(request, 'mpages/user_account.html', content)
    else:
        return redirect('login')

def my_profile(request):
    profile_info = UserAccounts.objects.filter(user_account_id=request.user.id)
    if request.user.is_authenticated:
        if request.method == "GET":
            form = AccountInfo(request.POST, request.FILES)
            name_nav = UserAccounts.objects.filter(user_account_id=request.user.id)
            context = {
                'form': form,
                'profile_info': profile_info,
                'name_nav': name_nav
            }
            return render(request, 'mpages/my_profile.html', context)
        else:
            form = AccountInfo(request.POST, request.FILES)
            if form.is_valid:
                name = request.POST['name']
                age = request.POST['age']
                city = request.POST['city']
                about = request.POST['about']
                avatar = request.FILES.get('avatar')
                if avatar is None:

                    # Если юзер не хочет обновлять фотографию профиля

                    obj = UserAccounts.objects.filter(user_account_id=request.user.id)
                    for field in obj:
                        avatar = field.avatar
                        UserAccounts.objects.filter(user_account_id=request.user.id).update(
                            user_account_id=User.objects.get(id=request.user.id), 
                            name=name, 
                            age=age, 
                            city=city, 
                            about=about, 
                            avatar=avatar
                    )
                    messages.add_message(request, messages.INFO, 'Информация сохранена')
                    return redirect('profile')
                else:

                    # Новая фотография профиля

                    UserAccounts.objects.filter(user_account_id=request.user.id).update(
                    user_account_id=User.objects.get(id=request.user.id), name=name, age=age, city=city, about=about, avatar=avatar
                    )
                    messages.add_message(request, messages.INFO, 'Информация сохранена')
                    return redirect('profile')
    else:
        return redirect('login')        


