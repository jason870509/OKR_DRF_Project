from rest_framework import generics, permissions
from reports.models import Report
from reports.serializers import ReportSerializer
from django.contrib.auth.models import User
from reports.models import Category
from reports.mixins import ReportResultsSetPagination
from reports.permissions import IsStaffEditorPermission



class SearchAPIView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    pagination_class = ReportResultsSetPagination

    # authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        author = self.request.GET.get('author')
        title = self.request.GET.get('title') or ""
        category = self.request.GET.get('category')

        if author != "":
            author = User.objects.filter(username=author).first() or ""
        if category != "":
            category = Category.objects.filter(id=category).first() or ""

        results = Report.objects.none()
        
        q = {
            "author": author,
            "title": title,
            "category": category
        }
        print("Q: ", q)
        search = False
        for key in q:
            if q[key] != "" and q[key] is not None:
                search = True
                break
        
        if search:
            user = None
            #     if self.request.user.is_authenticated:
            #         user = self.request.user
            results = qs.search(q, user=user)

        return results