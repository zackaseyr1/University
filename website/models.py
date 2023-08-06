from django.db import models
from django.contrib.auth.models import User


class Code(models.Model):
	user = models.ForeignKey(User, related_name="code", on_delete=models.DO_NOTHING)
	question = models.TextField(max_length=5000)
	code_answer = models.TextField(max_length=5000)
	language = models.CharField(max_length=50)


	def __str__(self):
		return self.question


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phrase=models.CharField(max_length=200)
    ai_image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.phrase)