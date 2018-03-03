from django.shortcuts import render
from django.views import View
# Create your views here.

class Test(View):
    def get(Self, request, *args, **kwargs):
        b = PD.objects.filter(user_id=request.user)
        for a in b:
            print(a.number)
            phone_number = a.number
        context = {
            'phone_number':phone_number,
        }
        
        return render(request, 'test.html', context)