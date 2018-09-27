from django import forms
from django.db.transaction import on_commit 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email',)#'full_name'
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self,commit=True):
        user = super(UserAdminCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ('email','password','active','staff','admin')#'full_name',
        
    def clean_password(self):
        return self.initial['password']

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model = User
        fields =('email',)
        widgets = {
                    'email'   : forms.EmailInput(attrs={'class':'form-control','autofocus':'autofocus'})
                   }
    
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active =False
        
        if on_commit:
            print(user)
            user.active =True
            user.save()
            
        return user
    
class LoginForm(forms.Form):
    email    = forms.EmailField(label='Email', widget  = forms.TextInput(attrs={'class':'form-control','autofocus':'autofocus'}))
    password = forms.CharField(label='Password' ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    
    