from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import  status
from django.http import JsonResponse


class AcessoList(APIView):
    def get(self, request):
        try:
            lista_acessos = Acesso.objects.all()
            serializer = AcessoSerializer(lista_acessos, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem:' "Ocorreu um erro no servidor"},
                                starus=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = AcessoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AcessoDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk =="0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            acesso = Acesso.objects.get(pk=pk)
            serializer = AcessoSerializer(acesso)
            return Response(serializer.data)
        except Acesso.DoesNotExist:
            return JsonResponse({'mensagem': "O acesso não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                            status=status.HTTP_400_BAD_REQUEST)
            acesso = Acesso.objects.get(pk=pk)
            serializer = AcessoSerializer(acesso, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        except Acesso.DoesNotExist:
            return JsonResponse({'mensagem': "O acesso não existe"},
                                status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."}, status=status.HTTP_400_BAD_REQUEST)
            acesso = Acesso.objects.get(pk=pk)
            acesso.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Acesso.DoesNotExist:
            return JsonResponse({'mensagem': "O acesso não existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
