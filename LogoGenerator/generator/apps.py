from django.apps import AppConfig
import torch
from min_dalle import MinDalle
import os
class GeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'generator'
    
    MinDalleModel = MinDalle(
        models_root= os.path.join('generator','pretrained'),
        dtype=torch.float16,
        device='cuda',
        is_mega=True, 
        is_reusable=True
        )
    
   
    
    
