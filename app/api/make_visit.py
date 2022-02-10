from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import employee, outlet, visit
from app.serializers import MakeVisitSerializer


class MakeVisit(APIView):
    def post(self, request):
        try:
            e = employee.Employee.objects.get(phone_number=request.POST['phone'])
            v = visit.Visit.objects.get(latitude=request.POST['lat'], longitude=request.POST['lon'])
            if e == v.get_outlet().get_employee():
                visit.Visit.objects.create(longitude=request.POST['lon'], latitude=request.POST['lat'], visit_outlet=v.get_outlet())
                return Response(200)
            else:
                return Response(300)
        except:
            return Response(400)
