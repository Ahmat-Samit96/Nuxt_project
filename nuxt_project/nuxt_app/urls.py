from django.urls import path
from .views import (
    CurrencyListCreateView, CurrencyDetailView,
    BitcoinPriceListCreateView, BitcoinPriceDetailView,
    PricePeriodListCreateView, PricePeriodDetailView,
    PriceSnapshotListCreateView, PriceSnapshotDetailView
)

urlpatterns = [
    # Маршруты для модели Currency
    path('currencies/', CurrencyListCreateView.as_view(), name='currency-list-create'),
    path('currencies/<int:pk>/', CurrencyDetailView.as_view(), name='currency-detail'),

    # Маршруты для модели BitcoinPrice
    path('bitcoin-prices/', BitcoinPriceListCreateView.as_view(), name='bitcoin-price-list-create'),
    path('bitcoin-prices/<int:pk>/', BitcoinPriceDetailView.as_view(), name='bitcoin-price-detail'),

    # Маршруты для модели PricePeriod
    path('price-periods/', PricePeriodListCreateView.as_view(), name='price-period-list-create'),
    path('price-periods/<int:pk>/', PricePeriodDetailView.as_view(), name='price-period-detail'),

    # Маршруты для модели PriceSnapshot
    path('price-snapshots/', PriceSnapshotListCreateView.as_view(), name='price-snapshot-list-create'),
    path('price-snapshots/<int:pk>/', PriceSnapshotDetailView.as_view(), name='price-snapshot-detail'),
]
