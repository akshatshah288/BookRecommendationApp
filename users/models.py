from django.db import models

class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=10)  # Adjusted max_length to 10 for mobile numbers
    email = models.EmailField(unique=True, max_length=100)  # Use EmailField for better validation
    locality = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)  # Use TextField for longer addresses
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='waiting')

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'user_registrations'



from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()

    genre = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)  # You can link this to User model if using auth
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.book.title}"


# models.py
class Favorite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.book.title} - Favorite"
