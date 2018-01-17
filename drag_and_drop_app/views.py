from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'POST' and request.FILES['the_file']:
        print("It's a POST")
        the_file = request.FILES['the_file']
        fs = FileSystemStorage()
        filename = fs.save(the_file.name, the_file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home.html')

