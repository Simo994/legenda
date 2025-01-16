from django.contrib import admin
from .models import Reservation, Feedback
from django.utils import timezone

# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date', 'time', 'guests', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('name', 'phone', 'email')
    ordering = ('-created_at',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('created_at', 'is_read')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    def save_model(self, request, obj, form, change):
        if change and 'is_read' in form.changed_data:
            # Если сообщение помечено как прочитанное
            if obj.is_read:
                obj.read_by = request.user
                obj.read_at = timezone.now()
        super().save_model(request, obj, form, change)
