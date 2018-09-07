from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.views.generic import View
from demo.forms import LoginForm
# Create your views here.


def hello(request):

    return render(request, "hello/hello.html", {})


def viewArticle(request, id):

    text = "ur id is : %s" %id

    return HttpResponse(text)


def viewArticles(request, month, year):

    text = "month is : %s and Year  is : %s" %(month,year)
    return HttpResponse(text)


def date(request, x):

    today = datetime.date.today()
    return render(request, "hello/date.html", {"today": today})


def dayWeek(request):

    today = datetime.date.today()

    dayofweek = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    return render(request, "hello/dayWeek.html", {"today": today, "dayofweek": dayofweek})


# Create your views here.
def hello1(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    return redirect("https://www.djangoproject.com")


class DayList(View):

    def get(self, request, *var, **kwargs ):

        today = datetime.datetime.now().date()
        daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        return render(request, "hello/dayWeek.html", {'today': today, 'dayofweek': daysOfWeek})


def login(request):
    username = "not logged in"

    if request.method == 'POST':
        MYLoginForm = LoginForm(request.POST)
       #print(MYLoginForm)

        if MYLoginForm.is_valid():
            print("hiiiiii")
            username = MYLoginForm.cleaned_data['username']

    else:
        MYLoginForm = LoginForm()

    return render(request, 'hello/loggedin.html', {'username': username})
