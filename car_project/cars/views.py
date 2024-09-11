from django.http import JsonResponse
from django.shortcuts import render
from car_project.cars.models import Car

#
# def car_list(request):
#     cars = Car.objects.all()
#     return render(request, 'car_list.html', {'cars': cars})

def car_list_json(request):
    cars = Car.objects.all()
    car_data = [
        {
            'url': car.url,
            'title': car.title,
            'time': car.time,
            'year': car.year,
            'mileage': car.mileage,
            'location': car.location,
            'description': car.description,
            'image': car.image,
            'modified_date': car.modified_date,
            'price': car.price,
        }
        for car in cars
    ]
    return JsonResponse(car_data, safe=False)
