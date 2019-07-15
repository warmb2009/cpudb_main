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
    name = models.CharField('CPU名字', max_length=32, unique=True, )

    brand = models.ForeignKey(
        'Brand', on_delete=models.PROTECT, null=True, blank=True)

    # 物理核心 physical
    # 针数
    socket = models.ForeignKey('Socket', verbose_name='物理核心',
                               related_name='socket_cpus', on_delete=models.PROTECT, null=True)

    # 厂家
    foundry = models.ForeignKey('Foundry', verbose_name='代工厂',
                                related_name='foundry_cpus', on_delete=models.PROTECT, null=True)

    # 封装面积
    process_size = models.ForeignKey('ProcessSize', verbose_name='封装面积',
                                     related_name='process_size_cpus', on_delete=models.PROTECT, null=True)

    transistors = models.CharField(
        verbose_name='晶体管数量', max_length=128, null=True, default='')  # 晶体管数量

    die_size = models.CharField('芯片尺寸',
                                max_length=32, null=True, default='')  # 芯片尺寸

    package = models.ForeignKey('Package', verbose_name='封装模式',
                                on_delete=models.PROTECT, null=True)  # 封装模式

    t_case_max = models.CharField(
        't_case_max', max_length=32, null=True, default='')

    # 工作状况 performance
    frequency = models.CharField(
        '工作状态', max_length=32, null=True, default='', blank=True)  # 频率
    turbo_clock = models.CharField(
        '睿频', max_length=32, null=True, default='')  # 睿频
    base_clock = models.CharField(
        '基础频率', max_length=32, null=True, default='')  # 基础频率

    # 倍频
    multiplier = models.ForeignKey(
        'Multiplier', verbose_name='倍频', on_delete=models.PROTECT, null=True)

    # 解锁倍频
    multiplier_unlocked = models.ForeignKey(
        'MultiplierUnlocked', verbose_name='解锁倍频',  on_delete=models.PROTECT, null=True)

    voltage = models.CharField(
        '电压', max_length=32, null=True, default='')  # 电压
    # 功率
    tdp = models.ForeignKey('TDP', verbose_name='功率',
                            on_delete=models.PROTECT, null=True)

    # 结构 architecture
    # 面向市场
    market = models.ForeignKey(
        'Market', verbose_name='市场',  on_delete=models.PROTECT, null=True)

    # 生产状态
    production_status = models.ForeignKey(
        'ProductionStatus', verbose_name='生产状态', on_delete=models.PROTECT, null=True)

    released = models.CharField('发布时间',
                                max_length=32, null=True, default='')  # 发布时间
    codename = models.ForeignKey('CodeName', verbose_name='代号',
                                 on_delete=models.PROTECT, null=True)  # 代号

    generation = models.ForeignKey('Generation', verbose_name='代',
                                   on_delete=models.PROTECT, null=True)  # 代

    part = models.CharField(max_length=64, null=True, default='')
    memory_support = models.ManyToManyField(
        'Memory', verbose_name='内存',                                             blank=True)  # 支持的内存

    # 核心cores
    core = models.ForeignKey('Core', verbose_name='核心数',
                             on_delete=models.PROTECT, null=True)  # 核心数

    thread = models.ForeignKey('Thread', verbose_name='线程数',
                               on_delete=models.PROTECT, null=True)  # 线程数

    smp_cpus = models.CharField(max_length=32, null=True, default='')
    integrated_graphics = models.ForeignKey(
        'IntegratedGraphics', verbose_name='核显', on_delete=models.PROTECT, null=True)  # 核显

    # 缓存 cache
    cache_l1 = models.CharField('一级缓存',
                                max_length=32, null=True, default='')  # 一级缓存
    cache_l2 = models.CharField('二级缓存',
                                max_length=32, null=True, default='')  # 二级缓存
    # 三级缓存
    cache_l3 = models.CharField('三级缓存', max_length=32, null=True, default='')
    # 四级缓存
    cache_l4 = models.CharField('四级缓存', max_length=32, null=True, default='')

    # 指令集 features
    feature = models.ManyToManyField('Feature', verbose_name='指令集')

    # 备注，贴士 notes
    notes = models.TextField('贴士', default='', null=True)

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = 'CPU'


class Brand(models.Model):
    '''
    品牌
    '''
    name = models.CharField(max_length=32, unique=True)
    pic = models.CharField(max_length=128, null=True, default='')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class Socket(models.Model):
    """
    接口
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '接口'
        verbose_name_plural = '接口'


class Foundry(models.Model):
    """
    代工厂
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '代工厂'
        verbose_name_plural = '代工厂'


class ProcessSize(models.Model):
    """
    封装工艺
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '封装工艺'
        verbose_name_plural = '封装工艺'

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

    class Meta:
        verbose_name = '封装模式'
        verbose_name_plural = '封装模式'

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

    class Meta:
        verbose_name = '倍频'
        verbose_name_plural = '倍频'


class MultiplierUnlocked(models.Model):
    """
    解锁倍频
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '解锁倍频'
        verbose_name_plural = '解锁倍频'


class TDP(models.Model):
    """
    功耗
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '功耗'
        verbose_name_plural = '功耗'


class Market(models.Model):
    """
    面向市场
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '面向市场'
        verbose_name_plural = '面向市场'


class ProductionStatus(models.Model):
    """
    生产状态
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '生产状态'
        verbose_name_plural = '生产状态'


class CodeName(models.Model):
    """
    代号
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '代号'
        verbose_name_plural = '代号'


class Generation(models.Model):
    """
    代
    """
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = '代'
        verbose_name_plural = '代'


class Memory(models.Model):
    """
    内存
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '内存'
        verbose_name_plural = '内存'


class Core(models.Model):
    """
    核心数
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '核心数'
        verbose_name_plural = '核心数'


class Thread(models.Model):
    """
    线程数
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '线程数'
        verbose_name_plural = '线程数'


class IntegratedGraphics(models.Model):
    """
    核显
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '核显'
        verbose_name_plural = '核显'


class Feature(models.Model):
    """
    指令集
    """
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '指令集'
        verbose_name_plural = '指令集'
