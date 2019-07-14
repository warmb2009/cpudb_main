from django.db import models

# Create your models here.


class Cpu_Url(models.Model):
    '''
    cpu-url 对应
    '''
    name = models.CharField(max_length=32, unique=True)
    url = models.CharField(max_length=128, unique=True)
    cpu = models.OneToOneField('Cpus', on_delete=models.PROTECT, null=True)
    done = models.BooleanField(default=False)


class Cpus(models.Model):
    '''
    cpu
    '''
    # 名称 品牌
    name = models.CharField(max_length=32, unique=True)

    brand = models.ForeignKey(
        'Brand', on_delete=models.PROTECT, null=True, blank=True)

    # 物理核心 physical
    socket = models.ForeignKey(
        'Socket', related_name='socket_cpus', on_delete=models.PROTECT, null=True)  # 针数

    foundry = models.ForeignKey(
        'Foundry', related_name='foundry_cpus', on_delete=models.PROTECT, null=True)  # 厂家

    process_size = models.ForeignKey(
        'ProcessSize', related_name='process_size_cpus', on_delete=models.PROTECT, null=True)  # 封装面积

    transistors = models.CharField(
        max_length=128, null=True, default='')  # 晶体管数量

    die_size = models.CharField(
        max_length=32, null=True, default='')  # 芯片尺寸

    package = models.ForeignKey(
        'Package', on_delete=models.PROTECT, null=True, blank=True, default='')  # 封装模式

    t_case_max = models.CharField(max_length=32, null=True, default='')

    # 工作状况 performance
    frequency = models.CharField(
        max_length=32, null=True, default='', blank=True)  # 频率
    turbo_clock = models.CharField(
        max_length=32, null=True, default='')  # 睿频
    base_clock = models.CharField(
        max_length=32, null=True, default='')  # 基础频率

    multiplier = models.ForeignKey(
        'Multiplier', on_delete=models.PROTECT, null=True)  # 倍频

    multiplier_unlocked = models.ForeignKey(
        'MultiplierUnlocked', on_delete=models.PROTECT, null=True)  # 解锁倍频

    voltage = models.CharField(max_length=32, null=True, default='')  # 电压
    tdp = models.ForeignKey(
        'TDP', on_delete=models.PROTECT, null=True)  # 功率

    # 结构 architecture
    market = models.ForeignKey(
        'Market', on_delete=models.PROTECT, null=True)  # 面向市场

    production_status = models.ForeignKey(
        'ProductionStatus', on_delete=models.PROTECT, null=True)  # 生产状态

    released = models.CharField(
        max_length=32, null=True, default='')  # 发布时间
    codename = models.ForeignKey(
        'CodeName', on_delete=models.PROTECT, null=True)  # 代号

    generation = models.ForeignKey(
        'Generation', on_delete=models.PROTECT, null=True)  # 代

    part = models.CharField(max_length=64, null=True, default='')
    memory_support = models.ManyToManyField(
        'Memory', blank=True)  # 支持的内存

    # 核心cores
    core = models.ForeignKey(
        'Core', on_delete=models.PROTECT, null=True)  # 核心数

    thread = models.ForeignKey(
        'Thread', on_delete=models.PROTECT, null=True)  # 线程数

    smp_cpus = models.CharField(max_length=32, null=True, default='')
    integrated_graphics = models.ForeignKey(
        'IntegratedGraphics', on_delete=models.PROTECT, null=True)  # 核显

    # 缓存 cache
    cache_l1 = models.CharField(
        max_length=32, null=True, default='')  # 一级缓存
    cache_l2 = models.CharField(
        max_length=32, null=True, default='')  # 二级缓存
    # 三级缓存
    cache_l3 = models.CharField(max_length=32, null=True, default='')
    # 四级缓存
    cache_l4 = models.CharField(max_length=32, null=True, default='')

    # 指令集 features
    feature = models.ManyToManyField('Feature')

    # 备注，贴士 notes
    notes = models.TextField(default='', null=True)


class Brand(models.Model):
    '''
    品牌
    '''
    name = models.CharField(max_length=32, unique=True)
    pic = models.CharField(max_length=128, null=True, default='')


class Socket(models.Model):
    """
    接口
    """
    name = models.CharField(max_length=32, unique=True)


class Foundry(models.Model):
    """
    代工厂
    """
    name = models.CharField(max_length=32, unique=True)


class ProcessSize(models.Model):
    """
    封装工艺
    """
    name = models.CharField(max_length=32, unique=True)


# class DieSize(models.Model):
#    """
#    芯片大小
#    """
#    name = models.CharField(max_length=32)


class Package(models.Model):
    """
    封装模式
    """
    name = models.CharField(max_length=32, unique=True)


# class TCaseMax(models.Model):
#    """
#    稳定运行的最大温度
#    """
#    name = models.CharField(max_length=32, unique=True)


class Multiplier(models.Model):
    """
    倍频
    """
    name = models.CharField(max_length=32, unique=True)


class MultiplierUnlocked(models.Model):
    """
    解锁倍频
    """
    name = models.CharField(max_length=32, unique=True)


class TDP(models.Model):
    """
    功耗
    """
    name = models.CharField(max_length=32, unique=True)


class Market(models.Model):
    """
    面向市场
    """
    name = models.CharField(max_length=32, unique=True)


class ProductionStatus(models.Model):
    """
    生产状态
    """
    name = models.CharField(max_length=32, unique=True)


class CodeName(models.Model):
    """
    代号
    """
    name = models.CharField(max_length=32, unique=True)


class Generation(models.Model):
    """
    代
    """
    name = models.CharField(max_length=64, unique=True)


class Memory(models.Model):
    """
    内存
    """
    name = models.CharField(max_length=32, unique=True)


class Core(models.Model):
    """
    核心数
    """
    name = models.CharField(max_length=32, unique=True)


class Thread(models.Model):
    """
    线程数
    """
    name = models.CharField(max_length=32, unique=True)


class IntegratedGraphics(models.Model):
    """
    核显
    """
    name = models.CharField(max_length=32, unique=True)


class Feature(models.Model):
    """
    指令集
    """
    name = models.CharField(max_length=32, unique=True)
