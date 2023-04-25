from rest_framework.pagination import PageNumberPagination

class StandartResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_query_param = "page"
    max_page_size = 100