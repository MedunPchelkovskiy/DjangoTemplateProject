from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()

GENRES_CHOICES = (
    ("Fiction", "Fiction"),
    ("Fantasy", "Fantasy"),
    ("Novel", "Novel"),
    ("Mystery", "Mystery"),
    ("Thriller", "Thriller"),
    ("Crime", "Crime"),
    ("Horror", "Horror"),
    ("Memoir", "Memoir"),
    ("Biography", "Biography"),
    ("Poetry", "Poetry"),
    ("History", "History"),
    ("Other", "Other"),
)


class Publishers(models.Model):
    publisher_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.publisher_name


class Authors(models.Model):
    class Meta:
        ordering = ('name',)

    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)],
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.name)


class Books(models.Model):
    class Meta:
        ordering = ('-book_id',)

    book_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=234)
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True,
                                   null=True)  # TODO:
    # image = cloudinary_models.CloudinaryField(null=True, blank=True, )
    genre = models.CharField(max_length=30, choices=GENRES_CHOICES)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)
    year_of_publication = models.PositiveIntegerField()
    borrower = models.CharField(max_length=50, null=True, blank=False)
    borrow_counter = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    return_date = models.DateField(default=None, null=True)
    is_borrow = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )

    autor = models.ForeignKey(
        Authors,
        null=False,
        blank=False,
        on_delete=models.RESTRICT

    )
    publisher = models.ForeignKey(
        Publishers,
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )
