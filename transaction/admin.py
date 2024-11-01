from django.contrib import admin
from .models import UserTransaction
# Register your models here.
@admin.register(UserTransaction)
class UserTransactionAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'transaction_id','amount')
    list_filter = ('borrower', 'transaction_id')
    search_fields = ('borrower', 'transaction_id')