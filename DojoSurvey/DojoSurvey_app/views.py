from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def result(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'loc': request.POST['location'],
            'lang': request.POST['language'],
            'comm': request.POST['comment']
        }
        return redirect('/')
        #return render(request, 'result.html', context)
    return redirect('/')
    #return render(request, 'result.html')