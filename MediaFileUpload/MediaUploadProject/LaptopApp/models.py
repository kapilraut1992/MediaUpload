from django.db import models

# Create your models here.
class Laptop(models.Model):
    comapny=models.CharField(max_length=50)
    model_name=models.CharField(max_length=50)
    ram=models.IntegerField()
    rom=models.IntegerField()
    processor=models.CharField(max_length=40)
    weight=models.IntegerField()
    product_image=models.ImageField(upload_to='Images/')
    product_pdf=models.FileField(upload_to='Files/')
    price=models.IntegerField()

    def __str__(self):
        return f"{self.company},{self.model_name},{self.ram},{self.rom},{self.processor},{self.price},{self.weight}"

