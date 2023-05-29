from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jmeno'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prijmeni'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Heslo musi obsahovat 150 znaku nebo mene. Pismena, cisla a @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Heslo nesmi byt podobne s prihlasovacimi udaje.</li><li>Heslo musi obsahovat nejmene 8 znaku.</li><li>Heslo nesmim byt mezi bezne pouzivanymi.</li><li>Heslo nemim byt pouze s cislic.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Zadejte sejtne heslo pro overeni.</small></span>'


#Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Jmeno", "class":"form-control"}), label="")
    last_name =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Prijmeni", "class":"form-control"}), label="")
    email =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefon", "class":"form-control"}), label="")
    address =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adresa", "class":"form-control"}), label="")
    city =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mesto", "class":"form-control"}), label="")
    state =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zeme", "class":"form-control"}), label="")
    zipcode =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"PSC", "class":"form-control"}), label="")


    class Meta:
        model = Record
        exclude = ("user",)

