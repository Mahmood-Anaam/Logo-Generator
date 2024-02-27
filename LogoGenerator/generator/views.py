from django.shortcuts import render
from PIL import Image
import base64
from io import BytesIO
import os
from .apps import GeneratorConfig



def Text2LogoGenerate(request):
    
    prompt = request.GET.get("prompt")
    if prompt is None:
        prompt='logo generator'
        
    prompt = "Generate logo images for "+prompt
    images =  GeneratorConfig.MinDalleModel.generate_images(
        text=prompt,
        seed=-1,
        grid_size=2,
        is_seamless=False,
        temperature=1,
        top_k=128,
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
    folder = os.path.join("static","images")
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