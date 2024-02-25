from django.shortcuts import render
from django.http import HttpResponse
from .apps import GeneratorConfig
from PIL import Image



def Text2LogoGenerate(text='Nuclear explosion broccoli'):
    images = GeneratorConfig.MinDalleModel.generate_images(
        text=text,
        seed=-1,
        grid_size=3,
        is_seamless=False,
        temperature=1,
        top_k=256,
        supercondition_factor=16,
        is_verbose=False
    )
    
    images = images.to('cpu').numpy().astype("int8")
    imageList = []
    for i in range(len(images)):
        image = Image.fromarray(images[i],mode="RGB")
        imageList.append(image)
        image.save('image_{}.png'.format(i))
        
    return imageList
    
    
    
    
def home(request):
    
    return render(request,"index.html")
