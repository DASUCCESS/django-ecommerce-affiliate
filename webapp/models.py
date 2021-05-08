from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length = 150, null=True)
    phone = models.CharField(max_length = 150, null=True) 
    email = models.EmailField(max_length=254, null=True)
    date_created = models.DateField(auto_now=False, auto_now_add=False)
    
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    TYPE_OF_TAGS = (
        ('indoor', 'indoor'),
        ('outdoors', 'outdoors'),
        ('general', 'general')
    )
    name = models.CharField(max_length = 150, choices=TYPE_OF_TAGS, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('LAPTOPS', 'LAPTOPS'),
        ('CLOTHING', 'CLOTHING'),
        ('GADGET', 'GADGET'),
    )
    name_of_product = models.CharField(max_length = 150, null=True)
    description = models.CharField(max_length = 150, null=True)
    price = models.FloatField(null=True)
    tags= models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    categories = models.CharField(max_length = 150, choices=CATEGORY, null=True )

    
    def __str__(self):
        return self.name_of_product

       

class Order(models.Model):
    STATUS = (
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('No Orders', 'No Orders'),
    )
    # customer_who_ordered = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product_ordered = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_status = models.CharField(max_length=50, choices=STATUS, null=True)
    # price = models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    date_ordered= models.DateField(auto_now=False, auto_now_add=False, null=True)
    address = models.CharField(max_length=250, null=True)

    def __str__(self): 
        return str(self.product_ordered) + str('-') + str(self.order_status)   

     
