from django.shortcuts import render, redirect
# from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})
class Login(LoginView):
    template_name = 'user/login.html'
class Logout(LogoutView):
    template_name = 'user/logout.html'