from django.shortcuts import render, redirect
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from .models import Game
from .serializers import GameSerializer

from rest_framework.authtoken.models import Token


def registration(request):

    form = RegistrationForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():
            value = form.cleaned_data
            user = User(username=value['username'])
            user.set_password(value['password'])
            user.save()  # - лучше делать так
            response = redirect('/accounts/login')
            return response

        else:
            request.session['status'] = 'Прошлая попытка регистрации была не удачной'
            status = request.session.get('status')
            context = {
                'form': form,
                'status': status,
            }
            return render(request, 'registration.html', context)
    else:
        print('hello')

    return render(request, 'registration.html', context)

def main(request):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    if request.user.is_superuser:
        games = Game.objects.all().order_by('player', 'step')
        context = {
            "games": games
        }
    else:
        games = Game.objects.filter(player=request.user).order_by('player', 'step')
        context = {
            "games": games
        }
    return render(request, "main.html", context)

def login(request):
    form = LoginForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = LoginForm(request.POST)
        print('Зашло')
        if form.is_valid():
            value = form.cleaned_data
            try:

                user = User.objects.get(username=value.get('username'))
                password = user.password
                print(password)
                print(make_password(value.get('password')))
                qqq = check_password(password, int(make_password(value.get('password'))))
                print(qqq)
                # print(check_password(user.password, hash user.password))

                if user.password == value.get('password'):
                    return redirect("/")
                else:
                    context = {
                        'form': form,
                        'error': 'Неверный логин или пароль'
                    }
                    return render(request, 'registration/login.html', context)
            except:
                context = {
                    'form': form,
                    'error': 'Неверный логин или пароль'
                }
                return render(request, 'registration/login.html', context)
        else:
            context = {
                'form': form,
                'error': form.errors
            }
            return render(request, 'registration/login.html', context)
    return render(request, 'registration/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/accounts/login')

class CraeteStep(APIView):

    model = Game
    serializer = GameSerializer
    queryset = Game.objects.all()
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            user = Token.objects.get(key=request.data.get("token")).user
            print(user)
            steps = Game.objects.filter(player__username=user).order_by('step').last()
            print(Game.objects.filter(player__username=user).order_by('step').last())

            if steps == None:
                step = 1
            else:
                step = steps.step + 1
            print(step)
            Game.objects.create(player=user, step=step, x=request.data.get("x"),
                                y=request.data.get("y"), time=serializer.validated_data.get('time'))

            return Response({"Status": 200})
        else:
            return Response({"error": serializer.errors})

