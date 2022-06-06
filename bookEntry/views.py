from django.shortcuts import render, redirect  
from bookEntry.forms import bookForm  
from bookEntry.models import BookEntry  
# Create your views here.  
def index(request):  
    if request.method == "POST":  
        form = bookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/retrieve')  
            except:  
                pass  
    else:  
        form = bookForm()  
    return render(request,'index.html',{'form':form}) 

def retrieve(request):  
    books = BookEntry.objects.all()  
    return render(request,"retrieve.html",{'books':books})   

def edit(request,id):  
    editBook = BookEntry.objects.get(id=id)  
    return render(request,'edit.html', {'book':editBook})  

def update(request, id):  
    book = BookEntry.objects.get(id=id)  
    form = bookForm(request.POST, instance = book)  
    if form.is_valid():  
        form.save()  
        return redirect("/retrieve")  
    return render(request, 'edit.html', {'book': book})  

def destroy(request, id):  
    book = BookEntry.objects.get(id=id)  
    book.delete()  
    return redirect("/retrieve") 
