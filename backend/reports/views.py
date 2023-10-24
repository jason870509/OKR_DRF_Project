from rest_framework import generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Report, Category
from .serializers import ReportSerializer, CategorySerializer



@api_view(['GET'])
def api(request, *args, **kwargs):
    """ 
            DRF ( Django Rest Framework ) API
    """
    instance = Report.objects.all().order_by("?").first()
    data = {}

    if instance:
        data = ReportSerializer(instance).data

    return Response(data)



class ReportDetailAPIView(generics.RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'



class ReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = title
        serializer.save(content=content)


class ReportUpdateAPIView(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        description = serializer.validated_data.get('description') or None
        serializer.save()


class ReportDestroyAPIView(generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)



class ReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


    @csrf_exempt
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        print(title)

        serializer.save()


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    



report_detail_view = ReportDetailAPIView.as_view()
report_list_create_view = ReportListCreateAPIView.as_view()
report_update_view = ReportUpdateAPIView.as_view()
report_destroy_view = ReportDestroyAPIView.as_view()

category_list_create_view = CategoryListCreateAPIView.as_view()