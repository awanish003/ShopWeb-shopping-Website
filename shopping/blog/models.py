from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    head0 = models.CharField(max_length=300)
    conthead0 = models.CharField(max_length=30000,default="")
    head1 = models.CharField(max_length=500,default="")
    conthead1 = models.CharField(max_length=50000,default="")
    head2 = models.CharField(max_length=500,default="")
    conthead2 = models.CharField(max_length=50000,default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
        return self.title