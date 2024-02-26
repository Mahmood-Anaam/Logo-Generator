from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from .apps import GeneratorConfig
import torch
from min_dalle import MinDalle
import base64
from io import BytesIO
import os




def Text2LogoGenerate(request):
    images_uri = readImages()
    # sleep(10)
    prompt = request.POST.get("prompt")
    if prompt is None:
        prompt='logo generator'
        
    if 1==1:
        return render(request,"index.html",{'images_uri': images_uri,'prompt':prompt})
        
    MinDalleModel = MinDalle(
        models_root='./generator/pretrained',
        dtype=torch.float16,
        device='cuda',
        is_mega=True, 
        is_reusable=True
        )
    
    images =  MinDalleModel.generate_images(
        text=prompt,
        seed=-1,
        grid_size=3,
        is_seamless=False,
        temperature=1,
        top_k=256,
        supercondition_factor=16,
        is_verbose=False
    )
    
    images = images.to('cpu').numpy().astype("int8")
    images_uri = []
    for i in range(len(images)):
        image = Image.fromarray(images[i],mode="RGB")
        images_uri.append(logo_to_uri(image))
        
    return render(request,"index.html",{'images_uri': images_uri,'prompt':prompt})

#.................................... 

def readImages():
    listurl=[]
    folder = r".\static\images"
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        listurl.append(logo_to_uri(img))
    
    return listurl

def logo_to_uri(pil_img):
    data = BytesIO()
    pil_img.save(data, "png")
    data64 = base64.b64encode(data.getvalue())
    return u'data:image/png;base64,'+data64.decode('utf-8')  
  
#....................................    
    
def home(request):
    images_uri = readImages()
    return render(request,"index.html",{'images_uri': images_uri})

#.................................... 
