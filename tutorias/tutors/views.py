from django.shortcuts import render
from django.db.models import Q

from rest_framework import status
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from tutors.models import Tutor
from users.models import User
from day_hour.models import DayHour
from day_hour.serializers import DayHourSerializers
from users.serializers import UserSerializer
from tutors.serializers import TutorSerializer


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TutorPermission',
            permission_configuration={
                'base': {
                    'create': 'tutors.add_tutor',
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': 'tutors.delete_tutor',
                    'update': 'tutors.change_tutor',
                    'partial_update': 'tutors.change_tutor',
                    'courseTutors': True,
                    'all_tutors':True,
                    'tutor_day_hour':True,
                    'dayhour':True
                }
            }
        ),
    )

    @action(detail=False, url_path='alltutors', methods=['get'])
    def all_tutors(self, request):
        tutors = Tutor.objects.all()
        return Response(TutorSerializer(tutors, many=True).data)

    @action(detail=False, url_path='coursetutors', methods=['post'])
    def courseTutors(self, request):
        try:
            response = []
            print(request)
            courseData = request.data['course_id']
            print('course Data antes de tutors' + courseData)
            tutors = Tutor.objects.filter(course = courseData)
            print("Este es el course Data : " + courseData)
            for tutor in tutors:
                response.append(UserSerializer(tutor.user_id).data)
            return Response(response)
        except:
            return Response({'detail':'id is not valid'}) 

    @action(detail=True, url_path='dayhour', methods=['get'])
    def tutor_day_hour(self, request, pk=None):
        try:
            print('hola')
            all_day_hour = DayHour.objects.all()
            day_hour = DayHour.objects.filter(tutor__user_id=pk)
            start_list = [[False for j in range(15)] for i in range(7)]
            for i in day_hour:
                start_list[i.id//15][i.id % 15] = True
            return Response(start_list, status=status.HTTP_200_OK)
        except:
            return Response({'detail':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)