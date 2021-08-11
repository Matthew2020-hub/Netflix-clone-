from django.shortcuts import render, redirect
from django.views.generic import View
from authentication.forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
     PasswordResetView, 
     PasswordResetConfirmView,
     PasswordResetCompleteView,
     PasswordResetDoneView,
)
# Create your views here.

def home(request):
    return HttpResponse('home')
# @login_required
class SignInView(View):
    template_name = 'authentication/signin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username
        
        user = authenticate(request, email=email, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="error")
            return render(request, self.template_name)
        
        login(request, user)
        messages.success(request, 'Thanks for Login, Welcome to Insta clone.', extra_tags='success')
        return redirect('home_feed')
        
        # return render(request, self.template_name)


class SignUpView(View):
    template_name = 'authentication/signup.html'
    from_class = UserForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_view')

        context = {'form': form}

        return render(request, self.template_name, context)
        
class SignOutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('signin_view')

class PRView(PasswordResetView):
    template_name = 'authentication/password_reset.html'

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'


class PRconfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'

class PRComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'