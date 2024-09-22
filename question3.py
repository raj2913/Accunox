# models.py
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def modify_instance(sender, instance, **kwargs):
    instance.name = 'Modified by signal'
    instance.save()

# Test transaction rollback
try:
    with transaction.atomic():
        m = MyModel.objects.create(name='Original Name')
        raise Exception("Force rollback")  # Simulate an error
except Exception:
    pass

# Check if the instance was modified
m = MyModel.objects.filter(name='Modified by signal').first()
if m:
    print("Signal ran and committed.")
else:
    print("Signal did not commit due to rollback.")
