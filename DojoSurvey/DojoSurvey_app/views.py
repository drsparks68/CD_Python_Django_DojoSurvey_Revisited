from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def survey(request):
    if request.method == 'POST':
        request.session['result'] = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['comment']
        }
        return redirect('/result')
        #return render(request, 'result.html', context)
    return redirect('/')
    #return render(request, 'result.html')

def result(request):
    context = {'result': request.session['result']}
    return render(request, 'result.html', context)