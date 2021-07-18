from django.shortcuts import render
from tensorflow import keras
from keras.preprocessing.image import load_img,img_to_array
import matplotlib.pyplot as plt
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from django.http import HttpResponse, JsonResponse
from myapp.models import SearchResults
from django.core import serializers
from pathlib import Path
import os 
import wikipedia
from django.db.models import Q

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = os.path.join(BASE_DIR, "media")

modl = keras.models.load_model('mymodel.h5')

# Create your views here.
def index(request):
    context = {}
    recent_search_data = SearchResults.objects.filter(~Q(title="")).order_by("-id")
   
    if request.method == "POST":
        if "img" in request.FILES:
            img = request.FILES.get("img")
            obj = SearchResults(image=img)
            obj.save()
            #serialize data to json
            d = serializers.serialize('json',[obj])
            context.update({"status":True,"message":"Image Uploaded Successfully!", "data":d})
            return JsonResponse(context)
        else:
            d.delete()
            context.update({"status":False, "message":"Could Not Update Image"})
            return JsonResponse(context)    
    return render(request,'index.html',{"recent_search_data":recent_search_data})


def predict_func(request):
    if request.method=="POST":
        id = request.POST.get("id")
        obj = SearchResults.objects.get(id=id)
    
        path = MEDIA_DIR+"/{}".format(obj.image)
        img = load_img(path,target_size=(224,224))
        img1 = img_to_array(img)
        image = img1.reshape((1,224,224,3))
        image=preprocess_input(image)
        y = modl.predict(image)
        pred = decode_predictions(y,top=1000)
        p=pred[0][0][1].replace("_"," ")
        try:
            summary = wikipedia.summary(p)
            page_obj = wikipedia.page(p)
            images = page_obj.images[:-3]
            links = page_obj.links
            title = page_obj.original_title
            url = page_obj.url

            # Check if it exist in database or not
            check=SearchResults.objects.filter(title=title)
            if len(check)<1:
                # Save data to database
                obj.title=title
                obj.url=url
                obj.text=summary
                obj.save() 
            else:
                obj.delete()
            response_obj = {
                "title":title,"url":url,"text":summary,"images":images,"links":links
            }
            return JsonResponse({"status":True,"message":"Search Results Found!","data":response_obj})
        except:
            return JsonResponse({"status":False,"message":"Sorry Could not found more details about this", "data":p})
    return JsonResponse({"status":"error"})