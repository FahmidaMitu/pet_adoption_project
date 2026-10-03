from django.contrib import admin
from .models import Pet, AdoptionRequest

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_type', 'breed', 'status', 'location')
    list_filter = ('status', 'animal_type', 'gender')
    search_fields = ('name', 'breed', 'location')

@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'status', 'created_at')
    list_filter = ('status',)

    # Business Logic Rule 3: Admin request Approve korle Pet-er status auto 'Adopted' hobe
    def save_model(self, request, obj, form, change):
        if change and obj.status == 'Approved':
            obj.pet.status = 'Adopted'
            obj.pet.save()
        super().save_model(request, obj, form, change)