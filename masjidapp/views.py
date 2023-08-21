from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import status

from .models import Countries,States,District,Masjidregister

from .serializers import Countriesserializer,Stateserializer,Districtserializer,Masjidserializer
# Create your views here.
class CountrylistAPIView(GenericAPIView):
    serializer_class=Countriesserializer
    def get(self,request):
        Countrylist=Countries.objects.all()
        if (Countrylist.count()>0):
             serializer=Countriesserializer(Countrylist,many=True)
             return Response({'data': serializer.data, 'message': 'Success','success' :1})
        else:           
            return Response({'data': 'Data Notavailable'},status=status.HTTP_400_BAD_REQUEST)
        

class StatelistAPIView(GenericAPIView):
    serializer_class=Stateserializer
    def get(self,request):
        Statelist=States.objects.all()
        if (Statelist.count()>0):
             serializer=Stateserializer(Statelist,many=True)
             return Response({'data': serializer.data, 'message': 'Success','success' :1})
        else:           
            return Response({'data': 'Data Notavailable'},status=status.HTTP_400_BAD_REQUEST)
        
class DistrictlistAPIView(GenericAPIView):
    serializer_class=Districtserializer
    def get(self,request):
        Districtlist=District.objects.all()
        if (Districtlist.count()>0):
             serializer=Districtserializer(Districtlist,many=True)
             return Response({'data': serializer.data, 'message': 'Success','success' :1})
        else:           
            return Response({'data': 'Data Notavailable'},status=status.HTTP_400_BAD_REQUEST)

class MasjidRegisterAPIView(GenericAPIView):
    serializer_class=Masjidserializer
    def post(self,request):
        country=request.data.get("country")
        state=request.data.get("state")
        district=request.data.get("district")
        name=request.data.get("name")
        aliasname=request.data.get("aliasname")
        bname=(aliasname).split(',')
        cname=str(bname)
        print(bname)
        print(aliasname)
        print(cname)
        address=request.data.get("address")
        serializer=self.serializer_class(data={'country':country,'state':state,'district':district,'name':name,'aliasname':aliasname,'address':address})
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Registered sussesfully','success':1},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'messages':'Failed','success':0},status=status.HTTP_400_BAD_REQUEST)
    

# class AllDataAPIView(GenericAPIView):
#     def get(self, request):
#         country_list = Countries.objects.all()
#         state_list = States.objects.all()
#         district_list = District.objects.all()

#         country_serializer = Countriesserializer(country_list, many=True)
#         state_serializer = Stateserializer(state_list, many=True)
#         district_serializer = Districtserializer(district_list, many=True)

#         data = {
#             'countries': country_serializer.data,
#             'states': state_serializer.data,
#             'districts': district_serializer.data,
#             'message': 'Success',
#             'success': 1
# }
       

#         return Response(data)

class AllDataAPIView(GenericAPIView):
    def get(self, request):
        country_list = Countries.objects.all()
        state_list = States.objects.all()
        district_list = District.objects.all()
        if (country_list and state_list and district_list.count()>0):
            country_serializer = Countriesserializer(country_list, many=True)
            state_serializer = Stateserializer(state_list, many=True)
            district_serializer = Districtserializer(district_list, many=True)
            return Response({'countries': country_serializer.data,'states': state_serializer.data,'districts': district_serializer.data,'message': 'Success','success': 1})
        else:
            return Response({'countries': 'data'},status=status.HTTP_400_BAD_REQUEST)
        
class MasjidlistAPIView(GenericAPIView):
    serializer_class=Masjidserializer
    def get(self,request):
        Masjidlist=Masjidregister.objects.all()
        if (Masjidlist.count()>0):
            serializer=Masjidserializer(Masjidlist,many=True)
            return Response({'Masjid_data':serializer.data,'message': 'Success','success' :1})
        return Response({'Maasjid_data': 'Data Notavailable'},status=status.HTTP_400_BAD_REQUEST)
