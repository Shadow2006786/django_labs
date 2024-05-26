from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def secure(request):
    return render(request, 'secure.html')