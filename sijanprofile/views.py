from django.shortcuts import render

# Create your views here.


"""Views for the base app"""

from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'index.html')


class TestMath():

    def add_numbers(num1, num2):
        return num1 + num2
