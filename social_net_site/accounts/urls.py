from django.conf.urls import url
#Django ce umesto nas uraditi login i logout, ova klasa ce to sama uraditi :)
from django.contrib.auth import views as auth_views
from . import views

#Kada ovo definisem, onda u templejtima referisem na ovaj url fajl npr: accounts:index
app_name = 'accounts'



urlpatterns = [
    #Obrati paznju ovo je dozvoljeno direktno da se odradi u najnovijoj verziji Djanga
    #Ne moras cak ni da kreiras klasu u Views.py
    url(r'^login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),
                                                name='login'),
    #Za logut view vec postoji default logout adresa, ali mozes uraditi isto kao i iznad
    url(r'^logout/$',auth_views.LogoutView.as_view(),
                                                name='logout'),
    #Sign up vec imamo povezane, u accounts/views.py --> pogledaj tamo
    url(r'^signup/$',views.SignUp.as_view(),
                                                name='signup'),
]
