from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Book, ToReadList, IssuedBook, StudentExtra
from .forms import AdminSignupForm, UserForm, StudentExtraForm, BookForm, IssuedBookForm
from datetime import date


# -----------------------------------------------
# Home and General Pages
# -----------------------------------------------

# 🏠 Home Page
def home_view(request):
	return render(request, 'library/index.html')

# ℹ️ About Us Page
def aboutus_view(request):
	return render(request, 'library/aboutus.html')

# 📞 Contact Us Page
def contactus_view(request):
	return render(request, 'library/contactus.html')

# 🔑 Admin Click Page (before login)
def adminclick_view(request):
	return render(request, 'library/adminclick.html')

# 🎓 Student Click Page (before login)
def studentclick_view(request):
	return render(request, 'library/studentclick.html')


# -----------------------------------------------
# Authentication (Signup, Login, Logout)
# -----------------------------------------------

# 👤 Admin Signup
def adminsignup_view(request):
	if request.method == "POST":
		form = AdminSignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(form.cleaned_data['password'])
			user.save()
			messages.success(request, "Admin account created successfully!")
			return redirect('adminlogin')
	else:
		form = AdminSignupForm()
	return render(request, 'library/adminsignup.html', {'form': form})


# 🎓 Student Signup
def studentsignup_view(request):
	if request.method == "POST":
		form1 = UserForm(request.POST)
		form2 = StudentExtraForm(request.POST)

		if form1.is_valid() and form2.is_valid():
			user = form1.save(commit=False)
			user.set_password(form1.cleaned_data['password'])
			user.save()

			student_extra = form2.save(commit=False)
			student_extra.user = user  
			student_extra.save()

			messages.success(request, "Student account created successfully!")
			return redirect('studentlogin')
	else:
		form1 = UserForm()
		form2 = StudentExtraForm()
	
	return render(request, 'library/studentsignup.html', {'form1': form1, 'form2': form2})


# 🔄 After Login - Redirect Admin & Student
@login_required
def afterlogin_view(request):
	if request.user.is_superuser:
		return redirect('adminafterlogin')  
	else:
		return redirect('studentafterlogin')  

# 🛠️ Admin After Login View
@login_required
def adminafterlogin_view(request):
    return render(request, 'library/adminafterlogin.html')

# 🎓 Student After Login View
@login_required
def studentafterlogin_view(request):
    return render(request, 'library/studentafterlogin.html')

# 🚪 Logout View
@login_required
def logout_view(request):
	logout(request)
	return redirect('home')


# -----------------------------------------------
# Book Management (Add, View, Delete)
# -----------------------------------------------

# ➕ Add a New Book (Admin Only)
@login_required
def addbook_view(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Book added successfully!")
			return redirect('bookadded')  
	else:
		form = BookForm()
	return render(request, 'library/addbook.html', {'form': form})


# ✅ Book Added Confirmation Page
@login_required
def bookadded_view(request):
	return render(request, 'library/bookadded.html')


# 📚 View All Books
@login_required
def view_books(request):
	books = list(Book.objects.all())  
	return render(request, 'library/viewbook.html', {'books': books})


# ❌ Delete a Book (Only if not issued)
@login_required
def delete_book(request, book_id):
	book = get_object_or_404(Book, id=book_id)

	if IssuedBook.objects.filter(book=book).exists():
		messages.error(request, "Cannot delete this book. It is currently issued.")
		return redirect('view_books')

	book.delete()
	messages.success(request, "Book deleted successfully!")
	return redirect('view_books')


# -----------------------------------------------
# Issued Books (Issue, View, Return)
# -----------------------------------------------

# 📖 Issue a Book to a Student
@login_required
def issuebook_view(request):
	if request.method == "POST":
		form = IssuedBookForm(request.POST)
		if form.is_valid():
			issued_book = form.save(commit=False)
			book = issued_book.book

			# Prevent issuing an already issued book
			if not book.available:
				messages.error(request, "This book is already issued.")
				return redirect('issuebook')

			book.available = False  # Mark as issued
			book.save()
			issued_book.save()

			messages.success(request, "Book issued successfully!")
			return redirect('bookissued')  
	else:
		form = IssuedBookForm()

	books = Book.objects.filter(available=True)
	return render(request, 'library/issuebook.html', {'form': form, 'books': books})


# 📋 View Issued Books & Calculate Fine
@login_required
def viewissuedbook_view(request):
	issued_books = IssuedBook.objects.select_related('book', 'student').all()

	issued_list = []
	today = date.today()

	for issued in issued_books:
		fine = 0
		if issued.expiry_date and issued.expiry_date < today:
			days_late = (today - issued.expiry_date).days
			fine = days_late * 10  # ₹10 per day fine

		issued_list.append([
			issued.student.user.get_full_name(),  
			issued.student.enrollment,  
			issued.book.title,  
			issued.book.author,  
			issued.issue_date,  
			issued.expiry_date,  
			fine  # 🔹 Fine dynamically calculated
		])

	return render(request, 'library/viewissuedbook.html', {'li': issued_list})


# ✅ Book Issued Confirmation Page
@login_required
def bookissued_view(request):
	return render(request, 'library/bookissued.html')


# 🔄 Return a Book
@login_required
def return_book(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	book.available = True
	book.save()

	issued_book = IssuedBook.objects.filter(book=book).first()
	if issued_book:
		issued_book.delete()  

	messages.success(request, "Book returned successfully!")
	return redirect('view_available_books')


# ❌ Delete Issued Book Record
@login_required
def delete_issued_book(request, book_id):
	issued_book = get_object_or_404(IssuedBook, book_id=book_id)
	issued_book.delete()
	messages.success(request, "Issued book record deleted successfully!")
	return redirect('viewissuedbook')


# 👀 View Books Issued by a Specific Student
@login_required
def viewissuedbookbystudent_view(request):
	student_extra = get_object_or_404(StudentExtra, user=request.user)
	issued_books = IssuedBook.objects.filter(student=student_extra).select_related('book')

	return render(request, 'library/viewissuedbookbystudent.html', {'issued_books': issued_books})


# -----------------------------------------------
# View Available Books
# -----------------------------------------------

# 📚 Show Available Books
def view_available_books(request):
	books = Book.objects.filter(available=True)

	if not books.exists():
		messages.info(request, "No books are currently available.")

	return render(request, 'library/viewavailablebooks.html', {'books': books})


# -----------------------------------------------
# To-Read List (Add, View, Remove)
# -----------------------------------------------

# 📖 View To-Read List
@login_required
def view_to_read_list(request):
	student_extra = get_object_or_404(StudentExtra, user=request.user)
	to_read_books = ToReadList.objects.filter(student=student_extra).select_related('book')

	return render(request, 'library/toreadlist.html', {'to_read_books': to_read_books})


# ➕ Add Book to To-Read List
@login_required
def add_to_read_list(request, book_id):
	student_extra = get_object_or_404(StudentExtra, user=request.user)
	book = get_object_or_404(Book, id=book_id)

	if not ToReadList.objects.filter(student=student_extra, book=book).exists():
		ToReadList.objects.create(student=student_extra, book=book)
		messages.success(request, "Book added to your To-Read List!")
	else:
		messages.info(request, "This book is already in your To-Read List.")

	return redirect('view_to_read_list')


# ❌ Remove Book from To-Read List
@login_required
def remove_from_read_list(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	to_read_entry = ToReadList.objects.filter(student__user=request.user, book=book).first()

	if to_read_entry:
		to_read_entry.delete()

	return redirect('view_to_read_list')

# 🎓 View Registered Students
@login_required
def viewstudent_view(request):
    students = StudentExtra.objects.select_related('user').all()  # Fetch all students with user details
    return render(request, 'library/viewstudent.html', {'students': students})