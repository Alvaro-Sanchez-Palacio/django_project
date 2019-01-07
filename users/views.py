from django.shortcuts import render, redirect
# Messages : messages.debug, messages.info, messages.success, messages.warning, messages.error
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created! Please, log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')
