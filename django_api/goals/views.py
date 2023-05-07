from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from .models import Goal
from .serializers import GoalSerializer

@csrf_exempt
def goal_list_create(request):
    if request.method == 'GET':
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GoalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def goal_detail(request, goal_id):
    try:
        goal = Goal.objects.get(pk=goal_id)
    except Goal.DoesNotExist:
        return JsonResponse( "Does Not Exist" ,status=status.HTTP_404_NOT_FOUND, safe=False)

    if request.method == 'DELETE':
        goal.delete()
        return JsonResponse(goal.goal,status=status.HTTP_204_NO_CONTENT, safe=False)

    else:
        return JsonResponse("Incorrect request",status=status.HTTP_405_METHOD_NOT_ALLOWED, safe=False)