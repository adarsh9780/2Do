from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from .models import ToDoModel as TDM
from twilio.rest import Client
from django.contrib import messages
from datetime import datetime as dt
from threading import Timer
from django.conf import settings
from twilio.rest import Client

# Create your views here.

class Index(View):
    def create_and_send_msg(self, to_do, number):
        # Find these values at https://twilio.com/user/account
        account_sid = settings.TWILIO_ACCOUNT_SID
        # print(settings.TWILIO_ACCOUNT_SID)
        auth_token = settings.TWILIO_AUTH_TOKEN
        # print(settings.TWILIO_AUTH_TOKEN)
        message = to_do

        client = Client(account_sid, auth_token)

        client.api.account.messages.create(
            to=number,
            from_=settings.TWILIO_CALLER_ID,
            body=message)

    def get(self, request, *args, **kwargs):
        now = dt.now()
        context = {
            'min_date':now.date(),
        }

        return render(request, 'create_card.html', context)

    def post(self, request, *args, **kwargs):
        to_do = request.POST.get("to_do")
        time = request.POST.get("time")
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")

        number = "+91" + phone_number

        test_date = time[:10] # extract date from string
        test_time = time[11:] # extract time from string

        test_date = dt.strptime(test_date, "%Y-%m-%d") # convert string date in date object in given format
        test_time = dt.strptime(test_time, "%H:%M") # convert string time in time object in given format

        now = dt.now()
        now = dt.strptime(str(now), '%Y-%m-%d %H:%M:%S.%f')
        time = dt.strptime(time.replace('T', " "), '%Y-%m-%d %H:%M')
        delay = (time - now).total_seconds()

        now = now.replace(microsecond=0)
        #only save in database if created today
        if test_date.date() < now.date():
            messages.error(request, "You can't create cards with date in past.")

        elif test_date.date() == now.date():

            if test_time.time() < now.time():
                messages.error(request, "You must provide time greater than current time.")

            else:
                a = TDM(name=name, time=time, to_do=to_do, phone_number=number)
                a.save()
                messages.success(request, "Card is created successfully")
                # print("delay: ", delay)
                Timer(delay, self.create_and_send_msg, [to_do, number]).start()

        else:
            a = TDM(name=name, time=time, to_do=to_do, phone_number=number)
            a.save()
            messages.success(request, "Card is created successfully")
            Timer(delay, self.create_and_send_msg, [to_do, number]).start()

        return render(request, 'create_card.html', {})

class ViewCard(View):
    def get(self, request, *args, **kwargs):
        cardsObj = TDM.objects.all()
        context = {
            'cardsObj' : cardsObj,
        }
        return render(request, 'view_card.html', context)
