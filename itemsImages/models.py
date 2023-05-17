from django.db import models
import PIL
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from io import BytesIO
import os
from django.core.files.base import ContentFile
from colorthief import ColorThief
import colorsys
from CNNCategorizeClothes.predict import predictImage
from services.getColorName import getHueColorName, getSaturationName, getLightnessName
# Create your models here.

class ContrastColors(models.Model):
    color_1 = models.CharField(max_length=30)
    color_2 = models.CharField(max_length=30)
    color_3 = models.CharField(max_length=30)
    def __str__(self):
        return {self.color_1, self.color_2, self.color_3}
    
    def save(self, *args, **kwargs):
        color = args
        self.color_1 = color
        self.color_2 = (color + 120) % 360
        self.color_3 = (self.color_2 + 120) % 360
        super().save(*args, **kwargs)


class AnalogueColors(models.Model):
    color_1 = models.CharField(max_length=30)
    color_2 = models.CharField(max_length=30)
    color_3 = models.CharField(max_length=30)
    def __str__(self):
        return {self.color_1, self.color_2, self.color_3}

class Items(models.Model):
    category = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to="images", default=None)
    rmbg_image = models.ImageField(upload_to="images_rmbg", default=None, blank=True)
    #contrast_palette_id = models.ForeignKey(ContrastColors, on_delete=models.CASCADE, blank=True)
    #analogue_palette_id = models.ForeignKey(AnalogueColors, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
       
        pil_img = PIL.Image.open(self.image)
        img = np.array(pil_img)

        #remove background
        segmentor = SelfiSegmentation()
        rmbg = segmentor.removeBG(img, (255,255,255), threshold=0.4)
        buffer = BytesIO()
        rmbg = PIL.Image.fromarray(rmbg)
        #prepare picture for classification
        classificate_img = rmbg

        x = np.asarray(rmbg.convert('RGBA')).copy()
        x[:, :, 3] = (255 * (x[:, :, :3] != 255).any(axis=2)).astype(np.uint8)
        img = PIL.Image.fromarray(x)
        
        
        self.category = predictImage(classificate_img)

        

        
        
        
        #этот код медленнее
        # img = output_img.convert("RGBA")
        # datas = img.getdata()

        # newData = []
        # for item in datas:
        #     if item[0] == 0 and item[1] == 255 and item[2] == 0:
        #         newData.append((255, 255, 255, 0))
        #     else:
        #         newData.append(item)

       #img.putdata(newData)
        img.save(buffer, format="png")
        #output_img.save(buffer, format="png")
        val = buffer.getvalue()
        filename = os.path.basename(self.image.name)
        name, _ = filename.split(".")
        self.rmbg_image.save(f"bgrm_{name}.png", ContentFile(val), save=False)
        
        #get color
        ct = ColorThief(self.rmbg_image)
        
        colors = colorsys.rgb_to_hls(*ct.get_color(5))
        
        self.color= getHueColorName(colors[0]) 


        #self.contrast_palette_id.save(getHueColorName(colors[0]))
        

        super().save(*args, **kwargs)

       

        
    
        

       








