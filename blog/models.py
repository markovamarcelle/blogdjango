from django.db import models
from django.utils import timezone

# Create your models here.
#creer la classe post.models.Models:c'est objet creer dans django et se cree aussi dans la bd
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	publiesh_date = models.DateTimeField(blank=True, null=True)
#methode pusblished et modifie aussi la valeur de la publication
	def publish(self):
		self.publiesh_date = timezone.now()
		self.save()
		#le titre de l'article sous forme de chaine de caractere
		def __str__(self):
			return self.title
