from django.contrib import admin

from medic.models import Diagnostic, Record, Result

admin.site.register(Diagnostic)
admin.site.register(Record)
admin.site.register(Result)
