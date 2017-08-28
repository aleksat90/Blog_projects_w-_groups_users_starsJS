from django.contrib.auth import get_user_model
#get sadasnjeg user-a u modelu
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        #ovde sam bio poslao self, medjutim vratio je gresku
        #jer je u pozadini pozvao UserCreateForm.get koji ne postoji
        super().__init__(*args,**kwargs)
        #isto kao i da smo setovali label za Display Name za label
        #isto moze da se uradi iz HTML-a
        self.fields['username'].label = 'Display Name'
        self.fields['email'].lable = 'Email address'
