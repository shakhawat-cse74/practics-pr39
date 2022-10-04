from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField( error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(error_messages={'required':'Enter Your Email'}, max_length=50 , min_length=5)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Your Password'},max_length=50 , min_length=5)
   
