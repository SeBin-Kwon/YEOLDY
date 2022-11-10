from django.shortcuts import render,redirect,get_object_or_404
from .forms import QnaForm,ReviewForm
from .models import QnA,Review
from django.contrib import messages
# Create your views here.



def index(request):
    qna = QnA.objects.all()
    context={
        'qna':qna
    }
    return render(request, 'community/index.html', context)
def qna_create(request):
    if request.method == 'POST':
        qna_form = QnaForm(request.POST, request.FILES)
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
    return render(request, 'community/qna_create.html',context)

def qna_detail(request, qna_pk):
    qna = QnA.objects.get(pk=qna_pk)
    context={
        'qna':qna
    }
    return render(request,'community/qna_detail.html', context)

def qna_update(request, qna_pk):
    qna = get_object_or_404(QnA, pk=qna_pk)
    if request.user == qna.user:
        if request.method == "POST":
            qna_form= QnaForm(request.POST, request.FILES, instance=qna)
            if qna_form.is_valid():
                qna = qna_form.save(commit=False)
                qna.user = request.user
                qna.save()
                messages.success(request, '수정 완료')
                return redirect('community:qna_detail', qna_pk)
        else:
            qna_form= QnaForm(instance=qna)
        context={
            'qna_form':qna_form,
        }
        return render(request, 'community/qna_create.html',context)
    else:
        messages.success(request, '작성자만 수정가 가능함')
        return redirect('community:qna_detail', qna_pk)

def qna_delete(request, qna_pk):
    qna = get_object_or_404(QnA, pk=qna_pk)
    if request.user == qna.user:
        if request.method == "POST":
            qna.delete()
            messages.success(request, '삭제 완료')
            return redirect('community:index',qna_pk)
    else:
        messages.success(request, '작성자만 삭제가 가능함')
        return redirect('community:index',qna_pk)

#리뷰 
def review_index(request):
    review = Review.objects.all()
    context={
        'review':review
    }
    return render(request, 'community/index.html', context)

def review_create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_index')
    else:
        review_form = ReviewForm()
    context={
        'review_form': review_form,
    }
    return render(request, 'community/review_create.html',context)

def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context={
        'review':review
    }
    return render(request,'community/review_detail.html', context)

def review_update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == "POST":
            review_form= ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.save()
                messages.success(request, '수정 완료')
                return redirect('community:review_detail', review_pk)
        else:
            review_form= ReviewForm(instance=review)
        context={
            'review_form':review_form,
        }
        return render(request, 'community/review_create.html',context)
    else:
        messages.success(request, '작성자만 수정가 가능함')
        return redirect('community:review_detail', review_pk)

def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == "POST":
            review.delete()
            messages.success(request, '삭제 완료')
            return redirect('community:review_index',review_pk)
    else:
        messages.success(request, '작성자만 삭제가 가능함')
        return redirect('community:review_index',review_pk)


