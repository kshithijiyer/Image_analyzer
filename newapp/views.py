import io
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.shortcuts import render
from google.cloud import vision
from newapp.models import history

# Create your views here.
def index(request):
    return render(request,'index.html')

def info(request):
    #vision api code which also saves data to db.
    vision_client = vision.Client()
    myfile = request.FILES["pic"]
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    file_name = fs.url(filename)
    with io.open(file_name, "rb") as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)
    labels = image.detect_labels()
    label_data=""
    for label in labels:
        label_data=label_data+label.description+"="+str(label.score)+","
    record=history(url=file_name,data=label_data)
    record.save()
    return render(request,'results.html',{"labels":labels,'image':file_name})

def getHistory(request):
    #Getting history from db.
    previous_searches=history.objects.all()
    return render(request,'history.html',{"data":previous_searches})
