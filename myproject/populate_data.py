import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Now import models after setting up Django
from myapp.models import User, Contact

# Create sample users and contacts
for i in range(50):
    user = User.objects.create_user(
        username=f"user_{i}",
        password="password123",
        phone_number=f"{random.randint(1000000000, 9999999999)}"
    )
    for j in range(20):
        Contact.objects.create(
            user=user,
            name=f"Contact_{j}",
            phone_number=f"{random.randint(1000000000, 9999999999)}"
        )

print("Sample data population complete.")
