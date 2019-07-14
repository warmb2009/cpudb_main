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
        slug_field='name', queryset=Package.objects.all())
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
        '''
        fields = ('name',  # 名字
                  'brand',  # 品牌
                  'brand_id',
                  'socket',  # 核心 针数
                  'socket_id',
                  'foundry',  # 厂家
                  'foundry_id',
                  'process_size',  # 封装面积
                  'process_size_id',
                  'transistors',  # 晶体管数量
                  'die_size',  # 芯片尺寸
                  'package',  # 封装模式
                  'package_id',
                  't_case_max',  # 稳定运行的最大温度
                  'frequency',  # 频率
                  'turbo_clock',  # 睿频
                  'base_clock',  # 基础频率
                  'multiplier',  # 倍频
                  'multiplier_id',
                  'multiplier_unlocked',  # 解锁倍频
                  'voltage',  # 电压
                  'tdp',  # 功率
                  'market',  # 面向市场
                  'production_status',  # 生产状态
                  'released',  # 发布时间
                  'codename',  # 代号
                  'generation',  # 代
                  'part',
                  'memory_support',  # 支持的内存
                  'core',  # 核心数
                  'thread',  # 线程数
                  'smp_cpus',
                  'integrated_graphics',  # 核显
                  'cache_l1',  # 一级缓存
                  'cache_l2',  # 二级缓存
                  'cache_l3',  # 三级缓存
                  'cache_l4',  # 四级缓存
                  'feature',  # 指令集
                  'notes',  # 贴士，备注
                  )

        def create(self, validated_data):
            print('fffff')
            print(Brand.objects.get(name=validated_data.pop('brand')))
            print('llllll')
            brand = Brand.objects.get(name=validated_data.pop('brand')).pk
            socket = Brand.objects.get(name=validated_data.pop('socket')).pk
            foundry = Brand.objects.get(name=validated_data.pop('foundry')).pk
            process_size = Brand.objects.get(
                name=validated_data.pop('process_size')).pk
            package = Brand.objects.get(name=validated_data.pop('package')).pk
            multiplier = Brand.objects.get(
                name=validated_data.pop('multiplier')).pk
            multiplier_unlocked = Brand.objects.get(
                name=validated_data.pop('multiplier_unlocked')).pk
            tdp = Brand.objects.get(name=validated_data.pop('tdp')).pk
            market = Brand.objects.get(name=validated_data.pop('market')).pk
            production_status = Brand.objects.get(
                name=validated_data.pop('production_status')).pk
            codename = Brand.objects.get(
                name=validated_data.pop.pk('codename'))
            generation = Brand.objects.get(
                name=validated_data.pop('generation')).pk
            memory_support = Brand.objects.get(
                name=validated_data.pop('memory_support')).pk
            core = Brand.objects.get(name=validated_data.pop('core')).pk
            thread = Brand.objects.get(name=validated_data.pop('thread')).pk
            integrated_graphics = Brand.objects.get(
                name=validated_data.pop('integrated_graphics')).pk
            feature = Brand.objects.get(name=validated_data.pop('feature')).pk

            validated_data['brand'] = brand
            validated_data['socket'] = socket
            validated_data['foundry'] = foundry
            validated_data['process_size'] = process_size
            validated_data['package'] = package
            validated_data['multiplier'] = multiplier
            validated_data['multiplier_unlocked'] = multiplier_unlocked
            validated_data['tdp'] = tdp
            validated_data['market'] = market
            validated_data['production_status'] = production_status
            validated_data['codename'] = codename
            validated_data['generation'] = generation
            validated_data['memory_support'] = memory_support
            validated_data['core'] = core_
            validated_data['thread'] = thread
            validated_data['integrated_graphics'] = integrated_graphics
            validated_data['feature'] = feature
            instance = super().create(validated_data)

            return instance

    def get_brand(self, obj):
        return obj.brand.name

    def get_socket(self, obj):
        return obj.socket.name

    def get_foundry(self, obj):
        return obj.foundry.name

    def get_process_size(self, obj):
        return obj.process_size.name

    def get_package(self, obj):
        return obj.package.name

    def get_multiplier(self, obj):
        return obj.multiplier.name

    def get_multiplier_unlocked(self, obj):
        return obj.multiplier_unlocked.name

    def get_tdp(self, obj):
        return obj.tdp.name

    def get_market(self, obj):
        return obj.market.name

    def get_production_status(self, obj):
        return obj.process_status.name

    def get_codename(self, obj):
        return obj.codename.name

    def get_generation(self, obj):
        return obj.generation.name

    def get_memory_support(self, obj):
        return obj.memory_support.name

    def get_cores(self, obj):
        return obj.cores.name

    def get_threads(self, obj):
        return obj.threads.name

    def get_integrated_graphics(self, obj):
        return obj.integrated_graphics.name

    def get_feature(self, obj):
        return obj.feature.name

    def create(zself,  validated_data):
        return Cpus.objects.create(
            brand=self.context["brand"],
            socket=self.context["socket"],
            foundry=self.context["foundry"],
            process_size=self.context["process_size"],
            package=self.context["package"],
            multiplier=self.context["multiplier"],
            multiplier_unlocked=self.context["multiplier_unlocked"],
            tdp=self.context["tdp"],
            market=self.context["market"],
            production_status=self.context["production_status"],
            codename=self.context["codename"],
            generation=self.context["generation"],
            memory_support=self.context["memory_support"],
            cores=self.context["cores"],
            threads=self.context["threads"],
            integrated_graphics=self.context["integrated_graphics"],
            feature=self.context["feature"],
            **validated_data)
    '''
