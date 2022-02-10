from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import employee, outlet
from app.serializers import OutletSerializer, EmployeeSerializer

class GetListOfOutlets(APIView):
    def get(self, request, phone=None):
        try:
            emp = employee.Employee.objects.get(phone_number=phone)
            o = outlet.Outlet.objects.filter(e=emp)
            serialazer = OutletSerializer(o, many=True)
            return Response({"result": serialazer.data})
        except:
            return Response({"result": "There is no phone like that"})