from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=50)

    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(self,cls):
        self.name= cls
        self.save()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(self,cls):
        self.name= cls
        self.save()

    def __str__(self):
        return self.name

class Images(models.Model):
    # title field
    name = models.CharField(max_length=100)
    # image field
    image=CloudinaryField('image')
    # description
    description=models.TextField(null=True,blank=True)
    # relations
    location= models.ForeignKey(Location,null=True,on_delete=models.CASCADE)
    category= models.ForeignKey(Category,null=True, on_delete=models.CASCADE)

    # methods
    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,name,description,location,category):
        update = cls.objects.filter(id=id).update(name=name,description=description,location=location,category=category)
    
    @classmethod
    def get_all_images(cls):
        images=cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls,category):
        images = Images.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__id=location)
        return images

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
