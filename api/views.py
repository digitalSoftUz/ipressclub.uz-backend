import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from datetime import date, timedelta
from rest_framework import pagination
from rest_framework.generics import ListAPIView


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000


class InfoView(APIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    def get(self, request):
        query = self.queryset.last()
        ser = self.serializer_class(query)
        return Response(ser.data)


class PartnersView(APIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class TeamView(APIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class JamoaView(APIView):
    queryset = Jamoa.objects.all()
    serializer_class = JamoaSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class CategoryView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class NewsAllView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        query = self.queryset.all().order_by('-id')
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class NewsView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        query = self.queryset.all().order_by('-id')[4:8]
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class NewsForSingleView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        query = self.queryset.all().order_by('-id')[4:35]
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class NewsByWeekView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        current_week = date.today().isocalendar()[1]
        query = self.queryset.filter(date__week=current_week).order_by('-id')[0:6]
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class NewsByNextWeekView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        query = self.queryset.all().order_by('-id')[6:14]
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class NewsOneView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, pk):
        query = self.queryset.get(id=pk)
        query.watcher += 1
        query.save()
        ser = self.serializer_class(query)
        return Response(ser.data)


class NewsThreeView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        query = self.queryset.all().order_by('-id')[0:3]
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class ProjectsView(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    # pagination_class = StandardResultsSetPagination

    def get(self, request):
        query = self.queryset.all()
        # page = self.paginate_queryset(query)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


class ProjectSingleView(APIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def get(self, request, pk):
        query = self.queryset.get(id=pk)
        ser = self.serializer_class(query)
        return Response(ser.data)


class RegionView(APIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class TripsView(APIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class NewsByCategory(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, pk):
        query = self.queryset.filter(category_id=pk).order_by('-id')[0:10]
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class TripByRegion(APIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer

    def get(self, request, pk):
        query = self.queryset.filter(region_id=pk)
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class AboutXPKView(APIView):
    queryset = AboutXPK.objects.all()
    serializer_class = AboutXPKSerializer

    def get(self, request):
        query = self.queryset.last()
        ser = self.serializer_class(query)
        return Response(ser.data)


class CategoryProjectsView(APIView):
    queryset = CategoryProjects.objects.all()
    serializer_class = CategoryProjectsSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class ProjectbyCategoryView(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk):
        query = self.queryset.filter(category_id=pk)
        # page = self.paginate_queryset(query)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


class StreamingApi(APIView):
    queryset = Streaming.objects.all()
    serializer_class = StreamingSerializer

    def get(self, request):
        query = self.queryset.last()
        ser = self.serializer_class(query)
        return Response(ser.data)


class PhotoView(APIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)


class VideosView(APIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

    def get(self, request):
        query = self.queryset.all()
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)
