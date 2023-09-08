import datetime

from django.shortcuts import render
from django.views import View

from .jalali_date_time import gregorian_to_jalali, Day
from .models import UserData


class InstagramLoginPage(View):

    def get(self, request):
        return render(request, 'MainApp/instagram_login_page.html')


class SaveData(View):

    def post(self, request):
        user_name = self.request.POST.get('user_name')
        password = self.request.POST.get('password')

        date_data = gregorian_to_jalali(int(str(datetime.datetime.date(datetime.datetime.now())).split("-")[0]), int(str(datetime.datetime.date(datetime.datetime.now())).split("-")[1]), int(str(datetime.datetime.date(datetime.datetime.now())).split("-")[2]))
        day_data = Day(datetime.datetime.now().strftime("%A"))
        time_data = str(datetime.datetime.now()).split()[1].split('.')[0]

        if UserData.objects.filter(id=1).exists():
            user_data = UserData.objects.get(id=1)
            user_data.user_name = user_name
            user_data.password = password
            user_data.date_time = date_data + ' - ' + day_data + ' - ' + time_data
            user_data.save()
        else:
            UserData.objects.create(user_name=user_name, password=password, date_time=date_data + ' - ' + day_data + ' - ' + time_data)

        return render(request, 'MainApp/fin_page.html')


class SetFirstData(View):

    @staticmethod
    def post(request):

        if UserData.objects.filter(id=1).exists():
            user_data = UserData.objects.get(id=1)
            user_data.user_name = 'None'
            user_data.password = 'None'
            user_data.date_time = 'None'
            user_data.save()
        else:
            UserData.objects.create(user_name='None', password='None', date_time='None')


class ShowData(View):

    @staticmethod
    def post(request):
        print('s')
        if UserData.objects.filter(id=1).exists():
            user_data = UserData.objects.get(id=1)
        else:
            UserData.objects.create(user_name='None', password='None', date_time='None')
            user_data = UserData.objects.get(id=1)

        return render(request, 'MainApp/response_page.html', {'user_data': user_data})



class ForgotPassword(View):

    @staticmethod
    def get(request):

        if UserData.objects.filter(id=1).exists():
            user_data = UserData.objects.get(id=1)
            user_data.user_name = 'Forgot'
            user_data.password = 'Forgot'
            user_data.date_time = 'Forgot'
            user_data.save()
        else:
            UserData.objects.create(user_name='Forgot', password='Forgot', date_time='Forgot')

        return render(request, 'MainApp/fin_page.html')