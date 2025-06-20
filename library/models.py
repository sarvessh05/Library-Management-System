from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

# ---------------------------------------------------
# Function to calculate the expiry date for issued books
# - Returns the current date + 14 days (default loan period)
# ---------------------------------------------------
def get_expiry():
	return date.today() + timedelta(days=14)  # 14-day borrowing period


# ---------------------------------------------------
# Book Model: Represents a book in the library
# - isbn: Unique identifier for each book
# - title: Name of the book
# - author: Name of the author
# - category: Genre or category of the book
# - available: Boolean flag to track book availability
# ---------------------------------------------------
class Book(models.Model):
	isbn = models.CharField(max_length=20, unique=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	available = models.BooleanField(default=True)  # Updates when book is issued/returned

	def __str__(self):
		return f"{self.title} by {self.author}"  # Returns a readable string representation of the book


# ---------------------------------------------------
# StudentExtra Model: Stores additional student details
# - user: Links to the built-in User model (one-to-one)
# - enrollment: Unique enrollment number for students
# - branch: Student's field of study
# ---------------------------------------------------
class StudentExtra(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	enrollment = models.CharField(max_length=15, unique=True)
	branch = models.CharField(max_length=50)

	def __str__(self):
		return self.user.username  # Returns the username of the student


# ---------------------------------------------------
# IssuedBook Model: Tracks books issued to students
# - student: References a student who borrows the book
# - book: References the issued book
# - issue_date: Auto-filled with the current date when a book is issued
# - return_date: Nullable field; filled when the book is returned
# - expiry_date: Auto-set to 14 days after issue date
# ---------------------------------------------------
class IssuedBook(models.Model):
	student = models.ForeignKey(StudentExtra, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	issue_date = models.DateField(auto_now_add=True)  # Automatically set when issued
	return_date = models.DateField(null=True, blank=True)  # Empty until book is returned
	expiry_date = models.DateField(default=get_expiry)  # Default due date (14 days from issue)

	def save(self, *args, **kwargs):
		"""
		Overrides the save method to update book availability.
		- If return_date is not set, mark the book as unavailable.
		- If return_date is set, mark the book as available.
		"""
		if not self.return_date:
			self.book.available = False  # Book is currently issued
		else:
			self.book.available = True  # Book is returned and available again
		self.book.save()  # Save the updated book status
		super().save(*args, **kwargs)  # Call the original save method

	def __str__(self):
		return f"{self.book.title} issued to {self.student.user.username}"


# ---------------------------------------------------
# ToReadList Model: Allows students to save books they want to read later
# - student: References the student who wants to read the book
# - book: References the book added to the reading list
# - unique_together: Ensures a student cannot add the same book multiple times
# ---------------------------------------------------
class ToReadList(models.Model):
	student = models.ForeignKey(StudentExtra, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('student', 'book')  # Prevents duplicate entries for the same book-student pair

	def __str__(self):
		return f"{self.student.user.username} wants to read {self.book.title}"