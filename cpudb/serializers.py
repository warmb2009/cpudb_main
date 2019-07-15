from .models import Cpu_Url
from .models import *
from rest_framework import serializers


class Cpu_UrlSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cpu_Url
        fields = ('name', 'url')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand


class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket


class FoundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Foundry


class ProcessSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessSize


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package


class MultiplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiplier


class MultiplierUnlockedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiplierUnlocked


class TDPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDP


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market


class ProductionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionStatus


class CodeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeName


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation


class MemorySupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread


class IntegratedGraphicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegratedGraphics


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegratedGraphics


class CpuSerializers(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field='name', queryset=Brand.objects.all(), required=False)
    socket = serializers.SlugRelatedField(
        slug_field='name', queryset=Socket.objects.all())
    foundry = serializers.SlugRelatedField(
        slug_field='name', queryset=Foundry.objects.all())
    process_size = serializers.SlugRelatedField(
        slug_field='name', queryset=ProcessSize.objects.all())
    package = serializers.SlugRelatedField(
        slug_field='name', queryset=Package.objects.all(), required=False, allow_null=True)
    multiplier = serializers.SlugRelatedField(
        slug_field='name', queryset=Multiplier.objects.all(), required=False)
    multiplier_unlocked = serializers.SlugRelatedField(
        slug_field='name', queryset=MultiplierUnlocked.objects.all())
    tdp = serializers.SlugRelatedField(
        slug_field='name', queryset=TDP.objects.all())
    market = serializers.SlugRelatedField(
        slug_field='name', queryset=Market.objects.all())
    production_status = serializers.SlugRelatedField(
        slug_field='name', queryset=ProductionStatus.objects.all())
    codename = serializers.SlugRelatedField(
        slug_field='name', queryset=CodeName.objects.all())
    generation = serializers.SlugRelatedField(
        slug_field='name', queryset=Generation.objects.all())
    memory_support = serializers.SlugRelatedField(
        slug_field='name', queryset=Memory.objects.all(), many=True)
    core = serializers.SlugRelatedField(
        slug_field='name', queryset=Core.objects.all(), required=False)
    thread = serializers.SlugRelatedField(
        slug_field='name', queryset=Thread.objects.all(), required=False)
    integrated_graphics = serializers.SlugRelatedField(
        slug_field='name', queryset=IntegratedGraphics.objects.all())
    feature = serializers.SlugRelatedField(
        slug_field='name', queryset=Feature.objects.all(), many=True)

    class Meta:
        model = Cpus
        fields = '__all__'
