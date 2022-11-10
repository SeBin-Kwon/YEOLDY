from django.shortcuts import render,redirect
from .forms import QnaForm
# Create your views here.



def index(request):
    return render(request, 'community/index')
def qua_create(request):
    if request.method == 'POST':
        qna_form = QnaForm(request.post, request.FILES)
        if qna_form.is_valid():
            qna = qna_form.save(commit=False)
            qna.user = request.user
            qna.save()
            return redirect('community:index')
    else:
        qna_form = QnaForm()
    context={
        'qna_form':qna_form,
    }
    return render(request, 'community/qua_create.html',context)
def qua_detail(request):
    return render(request)
def qua_update(request):
    return render(request)
def qua_delete(request):
    return render(request)