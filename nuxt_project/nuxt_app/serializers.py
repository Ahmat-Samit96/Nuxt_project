from rest_framework import serializers
from .models import Currency, BitcoinPrice, PricePeriod, PriceSnapshot

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class BitcoinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinPrice
        fields = '__all__'

class PricePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePeriod
        fields = '__all__'

class PriceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSnapshot
        fields = '__all__'

    def create(self, validated_data):
       
        return PriceSnapshot.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.bitcoin_price = validated_data.get('bitcoin_price', instance.bitcoin_price)
        instance.period = validated_data.get('period', instance.period)
        instance.start_timestamp = validated_data.get('start_timestamp', instance.start_timestamp)
        instance.end_timestamp = validated_data.get('end_timestamp', instance.end_timestamp)
        instance.save()
        return instance
