from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form.save()
        return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'accounts:signup')