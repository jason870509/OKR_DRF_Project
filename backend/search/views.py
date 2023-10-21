from rest_framework import generics
from reports.models import Report
from reports.serializers import ReportSerializer



class SearchAPIView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q') # 取得參數 q 的值
        
        results = Report.objects.none()
        
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)

        return results