from django.shortcuts import render
from .models import Cpu_Url, Cpus
from .serializers import Cpu_UrlSerializers
from .serializers import CpuSerializers
from rest_framework.response import Response
from rest_framework.views import APIView


class Cpu(APIView):
    def get(self, request):
        cpu_url = Cpu_Url.objects.all()
        serializer_class = Cpu_UrlSerializers(cpu_url, many=True)

        return Response(serializer_class.data)

    def post(self, request):
        print(request.data)
        serializer = Cpu_UrlSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, cpuid):
        Cpu_Url.objects.filter(pk=cpuid).delete()
        return Response("ok")


class CpuDetail(APIView):
    def get(self, request, cpuid):
        cpu_url = Cpu_Url.objects.filter(pk=cpuid)
        serializer_class = Cpu_UrlSerializers(cpu_url, many=True)

        return Response(serializer_class.data)

    '''
    def post(self, request, pk):
        print(request.data)
        serializer = Cpu_UrlSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    '''

    def delete(self, request, cpuid):
        Cpu_Url.objects.filter(pk=cpuid).delete()
        return Response("ok")


class CpuGet(APIView):
    def get(self, request):
        cpu_url = Cpu_Url.objects.filter(done=0).order_by('?')
        cpu = [cpu_url[0]]
        serializer_class = Cpu_UrlSerializers(cpu, many=True)
        return Response(serializer_class.data)


class CpuTravel(APIView):
    def get(self, request, cpu_name):
        cpu = Cpus.objects.filter(name=cpu_name)
        serializer_class = CpuSerializers(cpu, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        print(request.data)
        serializer = CpuSerializers(data=request.data)
        if serializer.is_valid():
            print('验证成功')
            serializer.save()
            return Response(serializer.data)
        else:
            print('验证失败')
            print(serializer.errors)
            return Response(serializer.errors)
