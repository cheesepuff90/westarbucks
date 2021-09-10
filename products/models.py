from django.db import models

class Menu(models.Model):
	name = models.CharField(max_length=20)
	
	class Meta:
		db_table = 'menus'

class Category(models.Model):
	name = models.CharField(max_length=20)
	menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
		
	class Meta:
		db_table = 'categories'

class Product(models.Model):
	name1     = models.CharField(max_length=100)
	name2 = models.CharField(max_length=100)
	description = models.TextField()
	category = models.ForeignKey('Category', on_delete=models.CASCADE)

	class Meta:
		db_table = 'products'

class Image(models.Model):
	url = models.URLField()
	product = models.ForeignKey('Product', on_delete=models.CASCADE)

	class Meta:
		db_table = 'images'

class Allergy_Product(models.Model):
	allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
	product = models.ForeignKey('Product', on_delete=models.CASCADE)

	class Meta:
		db_table = 'allergy products'

class Allergy(models.Model):
	name =  models.CharField(max_length=45)

	class Meta:
		db_table = 'allergy'

class Nutrition(models.Model):
	kcal = models.DecimalField(max_digits=5, decimal_places=1)
	sodium = models.DecimalField(max_digits=5, decimal_places=1)
	saturated = models.DecimalField(max_digits=5, decimal_places=1)
	sugars = models.DecimalField(max_digits=5, decimal_places=1)
	protein = models.DecimalField(max_digits=5, decimal_places=1)
	caffeine = models.DecimalField(max_digits=5, decimal_places=1)
	size_ml = models.IntegerField()
	size_fl = models.IntegerField()
	product = models.ForeignKey('Product', on_delete=models.CASCADE)

	class Meta:
		db_table = 'nutrition'

