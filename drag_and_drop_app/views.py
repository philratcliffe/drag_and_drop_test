from django.shortcuts import render

def home(request):
    if request.method == 'POST' and request.FILES['the_file']:
        print("It's a POST")
        print(request.FILES)
    return render(request, 'home.html')
