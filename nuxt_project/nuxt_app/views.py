from rest_framework import generics
from rest_framework.response import Response
from .models import Currency, BitcoinPrice, PricePeriod, PriceSnapshot
from .serializers import CurrencySerializer, BitcoinPriceSerializer, PricePeriodSerializer, PriceSnapshotSerializer

class CurrencyListCreateView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CurrencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class BitcoinPriceListCreateView(generics.ListCreateAPIView):
    queryset = BitcoinPrice.objects.all()
    serializer_class = BitcoinPriceSerializer

class BitcoinPriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BitcoinPrice.objects.all()
    serializer_class = BitcoinPriceSerializer

class PricePeriodListCreateView(generics.ListCreateAPIView):
    queryset = PricePeriod.objects.all()
    serializer_class = PricePeriodSerializer

class PricePeriodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PricePeriod.objects.all()
    serializer_class = PricePeriodSerializer

class PriceSnapshotListCreateView(generics.ListCreateAPIView):
    queryset = PriceSnapshot.objects.all()
    serializer_class = PriceSnapshotSerializer

class PriceSnapshotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceSnapshot.objects.all()
    serializer_class = PriceSnapshotSerializer
