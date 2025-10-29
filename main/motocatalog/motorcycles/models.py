from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    founded = models.IntegerField()
    logo = models.ImageField(upload_to='brands/')
    
    def __str__(self):
        return self.name

class Motorcycle(models.Model):
    TYPE_CHOICES = [
        ('sport', 'Спортивный'),
        ('cruiser', 'Круизер'),
        ('naked', 'Голый'),
        ('touring', 'Туристический'),
        ('enduro', 'Эндуро'),
        ('classic', 'Классический'),
    ]
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    motorcycle_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    engine_volume = models.IntegerField(help_text="Объем в куб.см")
    power = models.IntegerField(help_text="Мощность в л.с.")
    torque = models.IntegerField(help_text="Крутящий момент Н·м")
    weight = models.IntegerField(help_text="Вес в кг")
    seat_height = models.IntegerField(help_text="Высота седла в мм")
    fuel_capacity = models.IntegerField(help_text="Объем бака в литрах")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    main_image = models.ImageField(upload_to='motorcycles/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class MotorcycleImage(models.Model):
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='motorcycles/gallery/')
    caption = models.CharField(max_length=200, blank=True)

class Specification(models.Model):
    motorcycle = models.OneToOneField(Motorcycle, on_delete=models.CASCADE)
    transmission = models.CharField(max_length=50)
    frame_type = models.CharField(max_length=100)
    front_brakes = models.CharField(max_length=100)
    rear_brakes = models.CharField(max_length=100)
    front_suspension = models.CharField(max_length=100)
    rear_suspension = models.CharField(max_length=100)
    fuel_consumption = models.FloatField(help_text="Расход л/100км")
