from multiprocessing import context
from django.shortcuts import render, redirect
from wall_app.models import Message, Comment
from login_app.models import User


def wall(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'messages': Message.objects.all().order_by('-created_at'),
    }
    return render(request, 'wall.html', context)


def post_message(request):
    message = request.POST['message']
    Message.objects.create(
        message=message, user=User.objects.get(id=request.session['id']))
    return redirect('/wall')


def post_comment(request):
    comment = request.POST['comment']
    message = Message.objects.get(id=request.POST['message_id'])
    user = User.objects.get(id=request.session['id'])
    Comment.objects.create(comment=comment, user=user, message=message)
    return redirect('/wall')


def delete(request):
    c = Message.objects.get(id=request.POST['message_id'])
    c.delete()
    return redirect('/wall')
