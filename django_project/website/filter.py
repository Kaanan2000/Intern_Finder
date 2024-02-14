import django_filters
from job.models import Job

class Jobfilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expre='icontains')
    class Meta:
        model = Job
        fields = ['title', 'state', 'job_type', 'industry']