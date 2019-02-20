from django.shortcuts import render

# Create your views here.
def home(request):

    num4 = 10
    context = {
        'nums': [9,17,27],
        "nums2": {
            'num1':2,
            'num2':3,
            'num3':4,
        }
    }

    return render(request, "shop/home.html", context, num4)
