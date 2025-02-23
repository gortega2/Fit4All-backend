from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status, mixins, generics
from .models import *
from .serializer import *
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


# Generic List views

class TagsList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    

class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

#TODO: Implement error checking on the routine field when POSTing
class GuideList(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class Userlist(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

# Generic Detail views

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


@csrf_exempt
def signup_view(request):
    data = json.loads(request.body)
    taken = User.objects.filter(username=data['username']).exists()

    if taken is True:
        return JsonResponse({"message": "That username has already been taken"}, status=status.HTTP_400_BAD_REQUEST )
    user = User.objects.create_user(username=data['username'], password=data['password'])
    print(user)
    serializer = CustomUserSerializer(user)
    if user is not None:
        login(request, user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({"message": "Unable to login"}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def login_view(request):


    print(request.body)
    data = json.loads(request.body)
    print(data)
    user_object = User.objects.get(username=data['username'])
    serializer = CustomUserSerializer(user_object)
    user = authenticate(request, username=data['username'], password=data['password'])
    if user is not None:
        login(request, user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({"message": "Unable to login"}, status=status.HTTP_400_BAD_REQUEST, safe=False)


class GuideDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def retrieve_object(self, pk):
        try:
            return Guide.objects.get(pk=pk)
        except Guide.DoesNotExist:
            raise Http404
        

    # generic functionality
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    def put(self, request, pk, format=None):
        guide = self.retrieve_object(pk)

        data = request.data
        print(data)
        # Check if the routine is being updated, otherwise skip this step
        if 'routine' in data.keys():
            # print(data['routine'][0])
            
            # print(json_data)
            # print(type(json_data))
            try:
                print('Entering except block')
                json_data = json.loads(data['routine'])
                r_serializer = RoutineSerializer(data={'routine': json_data})
            except Exception as e:
                print(f'There was an error: {e}')
                return Response(f'Error checking routine object: {e}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            if not r_serializer.is_valid():
                return Response(r_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

        serializer = GuideSerializer(guide, data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
        

        

        

# Specialized API views