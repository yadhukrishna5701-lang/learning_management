
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class CustomPagination(PageNumberPagination):
    page_size=5
    page_query_param ="page_num"


class Customlimitoffsetpagination(LimitOffsetPagination):

    default_limit = 5
    limit_query_param = 6
    offset_query_param = 4