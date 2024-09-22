# models.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def check_thread(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

# Creating a new instance of MyModel
print(f"Main thread ID: {threading.get_ident()}")
m = MyModel.objects.create(name='Test Object')