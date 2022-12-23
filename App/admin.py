from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Etu_classe)
admin.site.register(AnneScolaire)
admin.site.register(Employe)

#admin.site.register(Agent)
#admin.site.register(Frais)
#admin.site.register(Absence)
#admin.site.register(Matier)
#admin.site,register(Note)
