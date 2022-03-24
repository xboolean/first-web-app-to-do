from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account was successfully created!')
            login(request, user)
            return redirect('index')
        else:
            username = form.data['username']
            password1 = form.data['password1']
            password2 = form.data['password2']
            for msg in form.errors.as_data():
                if msg == 'username':
                    messages.error(request, f"{username} was taken already.")
                if msg == 'password1' and password1 != password2:
                    messages.error(request, f"Passwords do not match.")
                if msg == 'password2' and password1 != password2:
                    messages.error(request, f"Passwords do not match.")
            form = CustomUserCreationForm()
            return render(request, 'registration/register.html', {'form': form})

    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'registration/register.html', context)