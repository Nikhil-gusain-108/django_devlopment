from django.shortcuts import render
def home(request):
    data={
        'name':["kjb","kiuvb","bjvjghvy"]
    }
    return render(request,"index.html",data)
def aboutus(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request,"contact.html")
def raw(request):
    data={
        'name':["kjb","kiuvb","bjvjghvy"]
    }
    return render(request,"raw.html",data)
def names_list(request):
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']  # Example list of names
    context = {
        'names': names,
    }
    return render(request, 'names.html', context)
def test(request):
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']  # Example list of names
    context = {
        'names': names,
    }
    return render(request,"test.html",context)
