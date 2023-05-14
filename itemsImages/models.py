from django.db import models
import PIL
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from io import BytesIO
import os
from django.core.files.base import ContentFile
# Create your models here.

class ContrastColors(models.Model):
    color_1 = models.CharField(max_length=30)
    color_2 = models.CharField(max_length=30)
    color_3 = models.CharField(max_length=30)
    def __str__(self):
        return {self.color_1, self.color_2, self.color_3}

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
        #remove background
        pil_img = PIL.Image.open(self.image)
        img = np.array(pil_img)
        segmentor = SelfiSegmentation()
        rmbg = segmentor.removeBG(img, (0,255,0), threshold=0.5)
        buffer = BytesIO()
        output_img = PIL.Image.fromarray(rmbg)
        output_img.save(buffer, format="png")
        val = buffer.getvalue()
        filename = os.path.basename(self.image.name)
        name, _ = filename.split(".")
        self.rmbg_image.save(f"bgrm_{name}.png", ContentFile(val), save=False)
        super().save(*args, **kwargs)

        #prepare picture for classification








