from django.db import models

# Create your models here.

#----------------------------------------------------------------

class Usernew(models.Model):
    ID_Usernew=models.IntegerField(unique=True,primary_key=True,default=0)
    Username=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Password=models.IntegerField()

    def __str__(self):
        return f"{self.ID_Usernew}"
#{self.Username},{self.Email},{self.Password}

class Post(models.Model):
    ID_Post=models.IntegerField(unique=True,primary_key=True,default=0)
    Title=models.CharField(max_length=255)
    Content=models.TextField(max_length=255)
    Category=models.CharField(max_length=255)
    Date_Published=models.DateField()

    def __str__(self):
        return f"{self.ID_Post}"
#{self.Title},{self.Content},{self.Category},{self.Date_Published}
class Comment(models.Model):
    ID_Comment=models.IntegerField(unique=True,null=True,default=0)
    Post_ID=models.ForeignKey(Post,on_delete=models.CASCADE)
    User_ID=models.ForeignKey(Usernew,on_delete=models.CASCADE)
    Content=models.CharField(max_length=255)
    Date_Posted=models.DateField()
    def __str__(self):
        return f"{self.ID_Comment} {self.Post_ID},{self.User_ID},{self.Content},{self.Date_Posted}"

class Category (models.Model):
    ID_Category=models.IntegerField(unique=True,null=True)
    Name=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.ID_Category} {self.Name}"


