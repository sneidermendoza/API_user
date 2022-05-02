from django.http import JsonResponse
from django.views import View
from .models import personas
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class PersonasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, id=0):
        if (id>0):
            peoples = list(personas.objects.filter(id=id).values())
            if len(peoples) > 0:
                people = peoples[0]
                datos = {'message': "success", 'personas': people}
            else:
                datos = {'message': "persona no encontrada...."}
            return JsonResponse(datos)
        else:
            peoples= list(personas.objects.values())
            if len(peoples) > 0:
                datos = {'message': "success", 'personas': peoples}
            else:
                datos = {'message': "personas no encontradas...."}
        return JsonResponse(datos)

    
    def post(self,request):
        jd = json.loads(request.body)
        personas.objects.create(name=jd['name'],apellido=jd['apellido'],edad=jd['edad'])
        datos = {'message': "success"}
        return JsonResponse(datos)

    
    def put(self, request, id):
        jd = json.loads(request.body)
        peoples = list(personas.objects.filter(id=id).values())
        if len(peoples) > 0:
            people= personas.objects.get(id=id)
            people.name = jd['name']
            people.apellido = jd['apellido']
            people.edad = jd['edad']
            people.save()
            datos = {'message': "success"}
        else:
            datos = {'message': "personas no encontradas...."}
        return JsonResponse(datos)
    
    
    def delete(self,request, id):
        peoples = list(personas.objects.filter(id=id).values())
        if len(peoples) > 0:
            personas.objects.filter(id=id).delete()
            datos = {'message': "success"}
        else:
            datos = {'message': "personas no encontradas...."}
        return JsonResponse(datos)