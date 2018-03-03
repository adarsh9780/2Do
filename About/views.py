from django.shortcuts import render
from django.views import View
# Create your views here.

class About(View):
    def get(self, request, *args, **kwargs):
        signup_form = UserCreationForm()
        context = {
        "signup_form":signup_form,
        }
        return render(request, 'about.html', context)

    def post(self, request, *args, **kwargs):
        signup_form = UserCreationForm(request.POST or None)
        
        if signup_form.is_valid():
            instance = signup_form.save()
            auth_login(request, instance)
            return HttpResponseRedirect('/')

        context = {
        'signup_form':signup_form,
        }

        return render(request, 'about.html', context)