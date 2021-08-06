from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    Brand_MAX_LENGTH = 128;
    brandname = models.CharField(max_length=Brand_MAX_LENGTH)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brandname)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'brands'

    def __str__(self): # display string representation of the object
        return self.brandname

class Page(models.Model):
    MAX_LENGTH = 256
    URL_MAX_LENGTH = 256

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    clothname = models.CharField(max_length=MAX_LENGTH, unique=True)
    description = models.CharField(max_length=MAX_LENGTH, null=True)
    url = models.URLField(max_length=URL_MAX_LENGTH)
    img = models.ImageField(upload_to='image', blank=True)
    views = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    #typeAuto = models.BooleanField(default=False)
    typeAuto = models.IntegerField(default = 1)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.clothname)
        super(Page, self).save(*args, **kwargs)


    def __str__(self):
        return self.clothname

class Article(models.Model):
    MAX_LENGTH = 128
    title = models.CharField(max_length=MAX_LENGTH, unique=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    authorName = models.CharField(max_length=MAX_LENGTH)
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    page = models.ForeignKey(Page, on_delete=models.DO_NOTHING)
    text = models.TextField(default="This cloth is good!")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comtime']
