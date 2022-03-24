from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account was successfully created!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'registration/register.html', context)