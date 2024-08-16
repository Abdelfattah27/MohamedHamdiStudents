from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'august', 'september', 'october', 'november', 'december',
                    'january', 'february', 'march', 'april', 'may')
    list_filter = ('august', 'september', 'october', 'november', 'december',
                   'january', 'february', 'march', 'april', 'may')
    search_fields = ('name',)
    actions = ['mark_all_paid']

    def mark_all_paid(self, request, queryset):
        queryset.update(august=True, september=True, october=True, november=True,
                        december=True, january=True, february=True, march=True,
                        april=True, may=True)
        self.message_user(request, "Selected students' payments marked as paid for all months.")

    mark_all_paid.short_description = "Mark all payments as paid"

admin.site.register(Student, StudentAdmin)
