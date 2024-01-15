from django.contrib import admin
from .models import Currency, BitcoinPrice, PricePeriod, PriceSnapshot

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol']
    search_fields = ['name']

@admin.register(BitcoinPrice)
class BitcoinPriceAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'price', 'currency']
    search_fields = ['timestamp']

@admin.register(PricePeriod)
class PricePeriodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(PriceSnapshot)
class PriceSnapshotAdmin(admin.ModelAdmin):
    list_display = ['bitcoin_price', 'period', 'start_timestamp', 'end_timestamp']
    search_fields = ['start_timestamp', 'end_timestamp']
