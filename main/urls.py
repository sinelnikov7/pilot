from django.urls import path, include

from .views import registration, main, login, log_out, CraeteStep

app_name = 'main'
urlpatterns = [

    path('registration/', registration, name='registration'),
    path('', main, name='main'),
    path('logout/', log_out, name="logout"),
    path('create_step/', CraeteStep.as_view(), name="create_step"),

]