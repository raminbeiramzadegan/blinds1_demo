from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from accounts.backends import CustomUserModelBackend
from accounts.forms import  SignInForm,SignUpForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.contrib.auth.views import LoginView


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request,*args,**kwargs)
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name ,{'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['user_signup_form'] = {

                'first_name':cd['first_name'],
                'last_name':cd['last_name'],
                'email':cd['email'],
                'password':cd['password'],
                'gender':cd['gender'],
                'birthdate_year':cd['birthdate_year'],
                'birthdate_month':cd['birthdate_month'],
                'birthdate_day':cd['birthdate_day'],

            }
            user_session = request.session['user_signup_form']
            User.objects.create_user(first_name = user_session['first_name'],last_name = user_session['last_name'], email = user_session['email'], password= user_session['password'],gender = user_session['gender'],birthdate_year = user_session['birthdate_year'],birthdate_month=user_session['birthdate_month'],birthdate_day=user_session['birthdate_day'])
            # messages.success(request,'Registered Successfully','success')
            return redirect('accounts:sign_in')
        return render(request, self.template_name, {'form': form})











# class SignInView(View):
#     form_class = SignInForm
#     template_name = 'accounts/signin.html'

#     def setup(self, request, *args, **kwargs):
#         self.next = request.GET.get('next')
#         return super().setup(request, *args, **kwargs)

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('home:home')
#         return super().dispatch(request, *args, **kwargs)

#     def get(self, request):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = CustomUserModelBackend().authenticate(request, email=email, password=password)

#             if user is not None:
#                 user.backend = 'accounts.backends.CustomUserModelBackend'
#                 # Use Django's login function to set the user as authenticated
#                 login(request, user)
              
#                 if self.next:
#                     return redirect(self.next)
#                 return redirect('dashboard:dashboard', user.id)
#             else:
#                 form.add_error(None, "Invalid email or password.") 

#         return render(request, self.template_name, {'form': form, 'user': request.user})

class SignInView(View):
    template_name = 'accounts/signin.html'
    form_class = SignInForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard', user.id)
        form.add_error(None, "Invalid email or password.")
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        # messages.success(request, 'you logged out successfully', 'success')
        return redirect('home:home')
    






    