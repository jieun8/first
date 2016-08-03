from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommentModelForm
# from .forms import ModelForm


def mysum2(request, x):
    return HttpResponse(sum(int(i) for i in x.split('/')))

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))


def new_comments(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES) # QueryDict의 data를 폼 안에
        if form.is_valid():
            form.save()
            return redirect('detail_comments', comment_pk)
            #return redirect('/') localhost:8000 으로
    else:
        form = CommentModelForm()

    return render(request, 'blog/new_comments.html', {'form':form})


def detail_comments(request, comment_pk):
    selected_comment = Comment.objects.filter(pk=comment_pk)
    # comment_pk =
    return render(request, 'detail_comments', {'comment_pk':comment_pk})