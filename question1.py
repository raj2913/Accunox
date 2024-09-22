# models.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate a slow signal handler
    print("Signal handler finished.")

# Creating a new instance of MyModel
m = MyModel.objects.create(name='Test Object')
print("Object created")