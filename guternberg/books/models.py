from django.db import models


class BooksAuthorModel(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'books_author'


class BooksBookModel(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_book'


class BooksBookAuthorsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(BooksBookModel,on_delete=models.CASCADE,db_column='book_id')
    author_id = models.ForeignKey(BooksAuthorModel,on_delete=models.CASCADE,db_column='author_id',related_name='book_author')

    class Meta:
        managed = False
        db_table = 'books_book_authors'


class BooksBookBookshelvesModel(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(BooksBookModel,on_delete=models.CASCADE,db_column='book_id')
    bookshelf_id = models.ForeignKey("BooksBookshelfModel",on_delete=models.CASCADE,db_column='bookshelf_id')

    class Meta:
        managed = False
        db_table = 'books_book_bookshelves'


class BooksBookLanguagesModel(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(BooksBookModel,on_delete=models.CASCADE,db_column='book_id')
    language_id = models.ForeignKey("BooksLanguageModel",on_delete=models.CASCADE,db_column='language_id')

    class Meta:
        managed = False
        db_table = 'books_book_languages'


class BooksBookSubjectsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(BooksBookModel,on_delete=models.CASCADE,db_column='book_id')
    subject_id = models.ForeignKey("BooksSubjectModel",on_delete=models.CASCADE,db_column='subject_id')

    class Meta:
        managed = False
        db_table = 'books_book_subjects'


class BooksBookshelfModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'books_bookshelf'


class BooksFormatModel(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book_id = models.ForeignKey(BooksBookModel,on_delete=models.CASCADE,db_column='book_id')

    class Meta:
        managed = False
        db_table = 'books_format'


class BooksLanguageModel(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'books_language'


class BooksSubjectModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'books_subject'
