from django import forms
from django.contrib.auth.models import User
from .models import StudentExtra, Book, IssuedBook

# -------------------------------------------
# Form for Admin Signup
# - Inherits from ModelForm to create a form based on the User model.
# - Includes fields like first name, last name, username, password, and email.
# - Password field is hidden using PasswordInput widget.
# -------------------------------------------
class AdminSignupForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())  # Secure password input field

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password', 'email']


# -------------------------------------------
# Form for Student Signup
# - Works the same way as AdminSignupForm but meant for students.
# - Uses the built-in User model.
# -------------------------------------------
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())  # Secure password input field

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password', 'email']


# -------------------------------------------
# Form to collect additional student details
# - Uses StudentExtra model (assumed to store extra details beyond the User model).
# - Allows entry of enrollment number and branch.
# -------------------------------------------
class StudentExtraForm(forms.ModelForm):
	class Meta:
		model = StudentExtra
		fields = ['enrollment', 'branch']  # Collects student enrollment and branch information


# -------------------------------------------
# Form to add books to the library
# - Uses the Book model.
# - Collects essential details: title, author, ISBN, and category.
# -------------------------------------------
class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'isbn', 'category']


# -------------------------------------------
# Form to issue books to students
# - Uses the IssuedBook model.
# - Collects the student and book details.
# -------------------------------------------
class IssuedBookForm(forms.ModelForm):
	class Meta:
		model = IssuedBook
		fields = ['student', 'book']  # Associates a student with a book being issued


# -------------------------------------------
# Form for user login
# - Simple form that collects a username and password.
# - Uses a CharField for username and a PasswordInput widget for secure password entry.
# -------------------------------------------
class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)  # Text input for username
	password = forms.CharField(widget=forms.PasswordInput())  # Hidden password input field


# -------------------------------------------
# Form to search books in the library
# - Provides a search bar where users can enter a book title or author.
# - The query field is optional.
# -------------------------------------------
class SearchBookForm(forms.Form):
	query = forms.CharField(max_length=200, required=False, label="Search by Title or Author")  # Optional search field


# -------------------------------------------
# Form to return a borrowed book
# - Users select their name (student) and enter the ISBN of the book being returned.
# - Uses a dropdown for students and a text field for ISBN.
# -------------------------------------------
class ReturnBookForm(forms.Form):
	student = forms.ModelChoiceField(queryset=StudentExtra.objects.all(), label="Student")  # Dropdown to select student
	isbn = forms.CharField(max_length=30, label="Book ISBN")  # ISBN input field to identify the book being returned


# -------------------------------------------
# Form to add a book to the "To-Read" list
# - Uses a hidden field to store the book ID.
# - This helps track which book the user wants to save for later reading.
# -------------------------------------------
class ToReadListForm(forms.Form):
	book_id = forms.IntegerField(widget=forms.HiddenInput())  # Stores the book ID without displaying it to the user