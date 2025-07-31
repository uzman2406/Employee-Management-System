from django.contrib import admin
from .models import Emp  # 👈 import your model

admin.site.register(Emp)  # 👈 register the model
