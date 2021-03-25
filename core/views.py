from django.shortcuts import render,redirect
from .models import usermessage,newsletter,blogpost,comment
from django.contrib import messages

# Create your views here.

def home(request):
    bpost=blogpost.objects.all()
    mx=usermessage()
    if request.method=='POST':
        msg=request.POST['msg']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        if usermessage.objects.filter(email=email).exists():
            messages.error(request,'Looks like your issue is not resolved we will try to fix it as soon as possible!')
            return redirect('/info')
        else:
            mx=usermessage(email=email,first_name=first_name,last_name=last_name,msg=msg)
            mx.save() 
            messages.success(request,'Your response has been noted successfully!')
            return redirect('/info')
    return render(request,'index/index.html',{'bpost':bpost})


def subscribe(request):
    news=newsletter()
    if request.method=='POST':
        email=request.POST['query']
        if newsletter.objects.filter(email=email).exists():
            messages.warning(request,'Looks like you have already subscribed the newsletter')
            return redirect('/info')
        else:
            news=newsletter(email=email)
            news.save()
            messages.success(request,'You will be informed if there is any update')
            return redirect('/info')
    return render(request,'other/message.html')

def info(request):
    return render(request,'other/message.html')


def blogs(request):
    bpost=blogpost.objects.all()
    return render(request,'core/blogpost.html',{'bpost':bpost})

def blogposts(request,slug):
    if blogpost.objects.filter(slug=slug).exists():
        bpost=blogpost.objects.filter(slug=slug).first()
        cmt=comment.objects.filter(post=bpost,parent=None)
        reply=comment.objects.filter(post=bpost).exclude(parent=None)
        repdict={}
        for rep in reply:
            if rep.parent.Sno not in repdict.keys():
                repdict[rep.parent.Sno]=[rep]   
            else:
                repdict[rep.parent.Sno].append(rep)
        return render(request,'core/post.html',{'bpost':bpost,'comment':cmt,'repdict':repdict})
    else:
        messages.warning(request,'This post doesnt exists!!')
        return redirect('/info')

def search(request):
    search=request.GET['query']
    bpost=blogpost.objects.filter(title__icontains=search)
    return render(request,'core/search.html',{'bpost':bpost})

def postcomment(request):
    if request.method=='POST':
        user=request.user
        pcmt=request.POST['comment']
        parentid=request.POST.get('parentid')
        comtid=request.POST.get('comtid')
        post=blogpost.objects.get(id=comtid)
        if parentid=="":
            comt=comment(cmt_content=pcmt,user=user, post=post)
            comt.save()
            messages.success(request,'Your comment has been posted successfully')
            return redirect(f'/blogposts/{post.slug}')
        else:
            parent=comment.objects.get(Sno=parentid)
            comt=comment(cmt_content=pcmt,user=user, post=post, parent=parent)       
            comt.save()
            messages.success(request,'Your reply has been posted successfully')
            return redirect(f'/blogposts/{post.slug}')
    return redirect(f'/blogposts/{post.slug}')

