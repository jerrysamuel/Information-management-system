from django.db import models

class Resourcecategory(models.Model):
    name = models.CharField(max_length= 40)
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    category = models.ForeignKey(Resourcecategory, on_delete=models.CASCADE, verbose_name='Resources')
    name = models.CharField(max_length=40, null=False, blank=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    weight = models.DecimalField(max_digits=10, decimal_places=2) 
    worth =  models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name


HUMANCATEGORY_CHOICES = (
    ('management', 'Management'),
    ('service', 'Service'),
    ('kitchen', 'Kitchen'),
    ('support', 'Support'),
)
GENDER_CHOICES = (
    ('male','Male'),
    ('female', 'Female')

)
class Humanresource(models.Model):
    humancategory = models.CharField(max_length=15, choices=HUMANCATEGORY_CHOICES)
    name = models.CharField(max_length= 45, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='employee', null=True, blank=True )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='male')


    def __str__(self):
        return self.name

class Accountdetail(models.Model):
    name = models.OneToOneField(Humanresource, on_delete=models.CASCADE)
    accountnum= models.DecimalField(max_digits=11, blank=False, null=False, decimal_places=0)
    bank_name= models.CharField(max_length=45, blank=False)

    def __str__(self):
        return f"{self.name} - {self.accountnum}"

class Menucategory(models.Model):
    name= models.CharField(max_length=45, blank=False)
    image= models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Menuitem(models.Model):
    category = models.ForeignKey(Menucategory, on_delete=models.CASCADE, verbose_name= 'menuitem')
    name = models.CharField(max_length=45)
    description= models.TextField(max_length=700)
    price = models.DecimalField(decimal_places=2, max_digits=15, null=False, blank=False)
    image = models.ImageField(upload_to='menu', null= True, blank=True)

    def __str__(self):
        return self.name
    
RATING_CHOICES = (
    ('1'  , '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
class Feedback(models.Model):
    user = models.CharField(max_length=35, blank=False, null=True)
    item = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    comment =models.TextField(max_length=150, null=True, blank=True)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='1')


    
class Sales(models.Model):
    item = models.ForeignKey(Resource, on_delete=models.CASCADE)
    customer = models.CharField(max_length=45, null=True, default="Anonymous")
    unit_sold = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, editable=True, null=True)


class Foodsales(models.Model):
    food = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    unit_sold = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, editable=True, null=True)

