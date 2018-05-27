
# Create your views here.
from django.shortcuts import redirect, get_object_or_404, render

from product.forms import CommentForm
from product.models import Comment


def create_comment(request, item_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_id = request.user.id
                form.item_id = item_id
                form.save()
                return redirect('/item/{}'.format(item_id))

    else:
        return redirect('/')

def delete_comment(request, comment_id, item_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user.id)
        if request.method == "POST":
            comment.delete()
            return redirect('/item/{}'.format(item_id))
        return render(request, "product/detail.html")
    else:
        return redirect('/')

def update_comment(request, comment_id, item_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id, user=request.user.id)
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('/item/{}'.format(item_id))
        else:
            form = CommentForm(instance=comment)
        return render(request, 'product/comment_update.html', {'form': form})
    else:
        return redirect('/')