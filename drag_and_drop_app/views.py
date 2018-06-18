from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'POST' and request.FILES['file']:
        #import pdb;
        #pdb.set_trace()
        the_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(the_file.name, the_file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'result.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home.html')

