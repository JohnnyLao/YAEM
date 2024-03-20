from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BasePagination(PageNumberPagination):
    """
    Custom pagination class based on PageNumberPagination.
    """

    page_size_query_param = "page_size"  # Parameter name for controlling the page size
    max_page_size = 1000  # Maximum page size allowed

    def get_paginated_response(self, data):
        """
        Overrides the method to customize the pagination response format.
        """
        return Response(
            {
                "next": self.get_next_link(),  # Link to the next page
                "previous": self.get_previous_link(),  # Link to the previous page
                "count": self.page.paginator.count,  # Total number of items
                "pages": self.page.paginator.num_pages,  # Total number of pages
                "results": data,  # Paginated data for the current page
            }
        )
