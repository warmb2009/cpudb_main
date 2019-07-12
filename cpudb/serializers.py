from .models import Cpu_Url
from .models import Cpus
from rest_framework import serializers


class Cpu_UrlSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cpu_Url
        fields = ('name', 'url')


class CpuSerializers(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    socket = serializers.SerializerMethodField()
    foundry = serializers.SerializerMethodField()
    process_size = serializers.SerializerMethodField()
    package = serializers.SerializerMethodField()
    t_case_max = serializers.SerializerMethodField()
    multiplier = serializers.SerializerMethodField()
    multiplier_unlocked = serializers.SerializerMethodField()
    tdp = serializers.SerializerMethodField()
    market = serializers.SerializerMethodField()
    production_status = serializers.SerializerMethodField()
    codename = serializers.SerializerMethodField()
    generation = serializers.SerializerMethodField()
    memory_support = serializers.SerializerMethodField()
    cores = serializers.SerializerMethodField()
    threads = serializer.SerializerMethodField()
    integrated_graphics = serializer.SerializerMethodField()

    feature = serializer.SerializerMethodField()

    class Meta:
        model = Cpus
        fields = ('name',  # 名字
                  'brand',  # 品牌
                  'socket',  # 核心 针数
                  'foundry',  # 厂家
                  'process_size',  # 封装面积
                  'transistors',  # 晶体管数量
                  'die_size',  # 芯片尺寸
                  'package',  # 封装模式
                  't_case_max',  # 稳定运行的最大温度
                  'frequency',  # 频率
                  'turbo_clock',  # 睿频
                  'base_clock',  # 基础频率
                  'multiplier',  # 倍频
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
                  'cores',  # 核心数
                  'threads',  # 线程数
                  'smp_cpus',
                  'integrated_graphics',  # 核显
                  'cache_l1',  # 一级缓存
                  'cache_l2',  # 二级缓存
                  'cache_l3',  # 三级缓存
                  'cache_l4',  # 四级缓存
                  'feature',  # 指令集
                  'notes',  # 贴士，备注
                  )

    def get_brand(self, obj):
        return obj.brand_f.name

    def get_socket(self, obj):
        return obj.socket_f.name

    def get_foundry(self, obj):
        return obj.foundry_f.name

    def get_process_size(self, obj):
        return obj.process_size_f.name

    def get_package(self, obj):
        return obj.package_f.name

    def get_t_case_max(self, obj):
        return obj.t_case_max_f.name

    def get_multiplier(self, obj):
        return obj.multiplier_f.name

    def get_multiplier_unlocked(self, obj):
        return obj.multiplier_unlocked_f.name

    def get_tdp(self, obj):
        return obj.tdp_f.name

    def get_market(self, obj):
        return obj.market_f.name

    def get_production_status(self, obj):
        return obj.process_status_f.name

    def get_codename(self, obj):
        return obj.codename_f.name

    def get_generation(self, obj):
        return obj.generation_f.name

    def get_memory_support(self, obj):
        return obj.memory_support_f.name

    def get_cores(self, obj):
        return obj.cores_f.name

    def get_threads(self, obj):
        return obj.threads.name

    def get_integrated_graphics(self, obj):
        return obj.integrated_graphics_f.name

    def get_feature(self, obj):
        return obj.feature_f.name

    def create(self,  validated_data):
        # 处理外键字段
        return Cpus.objects.create(author=self.context["author"], **validated_data)
