from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Adopted', 'Adopted'),
    )
    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pets/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AdoptionRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    reason = models.TextField()
    previous_pet_experience = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.pet.name}"