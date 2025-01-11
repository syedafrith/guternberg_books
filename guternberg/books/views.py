from django.core.paginator import Paginator
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import BooksBookModel
from books.serializers import BookSerializer


class BookView(APIView):
    def get(self,request):
        qp = request.query_params
        page_no = qp.get("page_no",1)
        filters_map = {
            "gutenberg_id__in":qp.get("book_id"),
            "booksbooklanguagesmodel__language_id__code__in":qp.get("language"),
            "booksformatmodel__mime_type__in":qp.get("mime_type"),
        }

        # topic filters logic
        subject_filters = Q()
        book_shelves_filters = Q()
        if qp.get("topic"):
            for topic in qp.get("topic").split(","):
                subject_filters |= Q(booksbooksubjectsmodel__subject_id__name__icontains=topic)
                book_shelves_filters |= Q(booksbookbookshelvesmodel__bookshelf_id__name__icontains=topic)
        topic_filters = Q(subject_filters|book_shelves_filters)

        # title filters logic
        title_filters = Q()
        if qp.get("title"):
            for title in qp.get("title").split(","):
                title_filters |= Q(title__icontains=title)

        # author filters logic
        author_filters = Q()
        if qp.get("author"):
            for author in qp.get("author").split(","):
                author_filters |= Q(booksbookauthorsmodel__author_id__name__icontains=author)



        filters = {k: v.split(",") for k, v in filters_map.items() if v}
        qs = BooksBookModel.objects.filter(topic_filters,title_filters,**filters).order_by("-download_count")
        paginated_qs = Paginator(qs, 25).page(page_no)
        serialized_data = BookSerializer(paginated_qs,many=True).data
        data = {
            "no_of_books":qs.count(),
            "data":serialized_data
        }
        return Response(data)