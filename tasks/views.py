from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json


def home(request):
    return JsonResponse({
        "message": "Task Tracker Backend is working"
    })


# GET - All Tasks
def task_list(request):
    if request.method == "GET":
        tasks = Task.objects.all()

        task_data = []

        for task in tasks:
            task_data.append({
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status
            })

        return JsonResponse({
            "success": True,
            "message": "Tasks fetched successfully",
            "tasks": task_data
        })


# POST - Add Task
@csrf_exempt
def add_task(request):
    if request.method == "POST":
        data = json.loads(request.body)

        task = Task.objects.create(
            name=data["name"],
            description=data["description"],
            status=data["status"]
        )

        return JsonResponse({
            "success": True,
            "message": "Task added successfully",
            "task": {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status
            }
        })


# PUT - Update Task
@csrf_exempt
def update_task(request, task_id):
    if request.method == "PUT":
        try:
            task = Task.objects.get(id=task_id)
            data = json.loads(request.body)

            task.name = data.get("name", task.name)
            task.description = data.get("description", task.description)
            task.status = data.get("status", task.status)

            task.save()

            return JsonResponse({
                "success": True,
                "message": "Task updated successfully",
                "task": {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description,
                    "status": task.status
                }
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Task not found"
            }, status=404)


# DELETE - Delete Task
@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(id=task_id)
            task.delete()

            return JsonResponse({
                "success": True,
                "message": "Task deleted successfully"
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Task not found"
            }, status=404)