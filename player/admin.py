from django.contrib import admin

# Register your models here.
from player.models import *

class SubmissionInline(admin.TabularInline):
    model = Submission
    extra = 1

class PlayerAdmin(admin.ModelAdmin):
    inlines = [SubmissionInline]
    search_fields = ['user__first_name', 'user__last_name', 'level']
    list_display = ('user', 'level', 'levelTime')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('player', 'question', 'timestamp')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Submission, SubmissionAdmin)