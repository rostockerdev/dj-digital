from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def registration_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "User name already exists")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email already used")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    messages.success(request, "Successfully registered")
                    return redirect("login")
        else:
            messages.error(request, "Password do not match")
            return redirect("register")

    else:
        return render(request, "accounts/register.html")
