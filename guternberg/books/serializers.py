from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from books.models import BooksBookModel, BooksBookAuthorsModel, BooksBookLanguagesModel, BooksBookSubjectsModel, \
    BooksBookBookshelvesModel, BooksFormatModel


class BookSerializer(ModelSerializer):
    authors = SerializerMethodField()
    languages = SerializerMethodField()
    subjects = SerializerMethodField()
    book_shelves = SerializerMethodField()
    links = SerializerMethodField()

    class Meta:
        model = BooksBookModel
        fields = "__all__"
        read_only = True

    def get_authors(self,obj):
        data = BooksBookAuthorsModel.objects.select_related("author_id").filter(book_id=obj).values_list("author_id__name",flat=True)
        return data

    def get_languages(self,obj):
        data = BooksBookLanguagesModel.objects.select_related("language_id").filter(book_id=obj).values_list("language_id__code",flat=True)
        return data

    def get_subjects(self,obj):
        data = BooksBookSubjectsModel.objects.select_related("subject_id").filter(book_id=obj).values_list("subject_id__name",flat=True)
        return data

    def get_book_shelves(self,obj):
        data = BooksBookBookshelvesModel.objects.select_related("bookshelf_id").filter(book_id=obj).values_list("bookshelf_id__name",flat=True)
        return data

    def get_links(self,obj):
        data = BooksFormatModel.objects.filter(book_id=obj).values("url","mime_type")
        return data
