from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import Profile,Managers
from blog.models import vacancy
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import SelectDateWidget
# from django.forms.extras.widgets Django < 1.9
from django.utils import timezone


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    last_date=forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = vacancy
        fields = ('title', 'body', 'address', 'city','no_of_vacancies','last_date')
        

class UserFormlog(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name','about_yourself','age','contact_number','address','Education','Experience','skills','profile_photo','Work','resume')
        
class AdminForm(forms.Form):
    department_id= forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
    

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Managers
        fields = ('email','department_id','username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    email= forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    department_id= forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    username= forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model = Managers
        fields = ( 'email','password', 'active', 'admin','staff')
        

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
