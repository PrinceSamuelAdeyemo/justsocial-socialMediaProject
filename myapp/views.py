
from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Follower, User, Profile, Post, LikePost
from django.contrib.auth.models import User, auth
from django.core import mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.views import View

# Create your views here.
"""
def index(request):
    user_object = User.objects.get(username= request.user.username)
    user_profile = Profile.objects.get(user = user_object)
    context_dict = {'user_profile': user_profile}
    return render(request, 'homepage.html', context_dict)
"""    
    

# Signup view 
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstName']
        middle_name = request.POST['middleName']
        last_name = request.POST['lastName']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        phoneNum = request.POST['phoneNum']
        
        if password != password2:
            messages.info(request, "Passwords don't match")
            return redirect('/signup')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email taken")
            else:
                user = User.objects.create_user(username= username, email = email, first_name = first_name, last_name = last_name, password=password)
                user.save()
                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user = user_model, id_user = user_model.id, first_name = first_name, middle_name = middle_name, last_name = last_name)
                new_profile.save()
                
                new_profile.first_name = first_name
                new_profile.middle_name = middle_name
                new_profile.last_name = last_name
                
                authenticate_user = auth.authenticate(username=username, password = password)
                if authenticate_user is not None:
                    
                    subject = "Welcome to testing software"
                    message = f'Hello, {user.username}. \nThank you for registering with us at Software testing. We hope you enjoy your stay with us.'
                    email_from = settings.EMAIL_HOST_USER
                    recipients = [user.email,]
                    
                    auth.login(request, authenticate_user)
                    try:
                        mail.send_mail(subject, message, email_from, recipients)
                    except:
                        pass
                    return redirect('/settings')
        
        
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid login details")
            return render(request, "signin.html")
    
    else:
        return render(request, 'signin.html')

# @login_required(login_url='/signin')
def homepage(request):
    
    
    try:
        user_object = User.objects.get(username = request.user.username)
        user_profile = Profile.objects.get(user = user_object)
        
        posts = Post.objects.all()
        
        context_dict = {'user_profile': user_profile, 'posts': posts}
        return render(request, 'homepage.html', context_dict)
    
    except User.DoesNotExist:
        posts = Post.objects.all()
        context_dict = {'user_profile': '', 'posts': posts}
        return render(request, 'homepage.html', context_dict)
    
    except Profile.DoesNotExist:
        posts = Post.objects.all()
        context_dict = {'user_profile': '', 'posts': posts}
        return render(request, 'homepage.html', context_dict)
    

@login_required(login_url='/signin')
def settings(request):
    
    user_profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        
        if request.FILES.get("profileImg") == None:
            profile_img = user_profile.profileImg
            first_name = request.POST['firstName']
            middle_name = request.POST['middleName']
            last_name = request.POST['lastName']
            bio = request.POST['bio']
            #password = request.POST['password']
            #phoneNum = request.POST['phoneNum']
            
            user_profile.profileImg = profile_img
            user_profile.first_name = first_name
            user_profile.middle_name = middle_name
            user_profile.last_name = last_name
            if bio != None:
                user_profile.bio = bio
            else:
                user_profile.bio = ''
            
            user_profile.save()
            
        elif request.FILES.get("profileImg") != None:
            profile_img = request.FILES.get('profileImg')
            first_name = request.POST['firstName']
            middle_name = request.POST['middleName']
            last_name = request.POST['lastName']
            bio = request.POST['bio']
            #password = request.POST['password']
            #phoneNum = request.POST['phoneNum']
            
            user_profile.profileImg = profile_img
            user_profile.first_name = first_name
            user_profile.middle_name = middle_name
            user_profile.last_name = last_name
            if bio != None:
                user_profile.bio = bio
            else:
                user_profile.bio = ''
            
            user_profile.save()
            
        redirect('/settings')
            
    
    return render(request, 'settings.html', {'user_profile': user_profile})


'''
def header(request):
    try: 
        if request.user.is_authenticated:
            user_object = User.objects.get(username= request.user.username)
            user_profile = Profile.objects.get(user = user_object)
        
            context_dict = {'user_profile': user_profile}
            return render(request, 'header.html', context_dict)
        else:
            if request.user.is_authenticated is None:
                user_profile = ''
                context_dict = {'user_profile': user_profile}
                return render(request, 'header.html', context_dict)
    except:
        if request.user.is_authenticated is None:
            user_profile = ''
            context_dict = {'user_profile': user_profile}
            return render(request, 'header.html', context_dict)
        
'''
'''
@login_required(login_url='/signin')

def logout(request):
    
    auth.logout(request)
    return redirect('signin')
    
    if request == 'POST':
        auth.logout(request)
        return redirect('signin')
        
    else:
        pass

'''


class Logout(View):
    def get(self, request):
        auth.logout(self.request)
        return redirect('signin')


@login_required(login_url='/signin')
def uploadpost(request):
    if request.method == "POST":
        
        if request.FILES.get("postImage") is not None:
            
            username = request.user.username
            first_name = request.user.first_name.capitalize()
            last_name = request.user.last_name.capitalize()
            caption = request.POST["caption"]
            postImage = request.FILES.get("postImage")
            
            name = (first_name + ' ' + last_name).title()
            
            uploadedPost = Post.objects.create(username = username, name = name, caption = caption, postImage = postImage)
            uploadedPost.save()
            
            return redirect('/')
            
        else:
            username = request.user.username
            first_name = request.user.first_name
            last_name = request.user.last_name
            caption = request.POST["caption"]
            postImage = None
            
            
            
            uploadedPost = Post.objects.create(username = username, caption = caption, postImage = postImage)
            uploadedPost.save()
            
            return redirect('/')
        
    else:
        return redirect('/')

@login_required(login_url="/signin")
def like_post(request):
    #username = Post.objects.get(username = )
    reaction_username = request.user.username
    post_id = request.GET.get('post_id')
    
    post = Post.objects.get(id = post_id)
    #post_likes = Post.object.all()
    
    like_filter = LikePost.objects.filter(post_id = post_id, reaction_username = reaction_username).first()
    
    if like_filter == None:
        new_like = LikePost.objects.create(post_username = post.username, post_id = post_id, reaction_username = reaction_username)
        post.noOfLikes += 1
        new_like.save()
        post.save()
        
        return redirect('/')
        
    else:
        like_filter.delete()
        post.noOfLikes -= 1
        post.save()
        return redirect('/')

# @login_required(login_url="/signin")
def profile(request, pk):
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(username = pk)
    user_posts_length = len(user_posts)
    
    follower = request.user.username
    user = pk
    
    if Follower.objects.filter(user = pk, follower = follower).first():
        button_text = "Unfollow"
        
    else:
        button_text = "Follow"
        

    user_followers = len(Follower.objects.filter(user = pk))
    user_following = len(Follower.objects.filter(follower = pk))

    context = {'user_object': user_object,
               'user_profile': user_profile,
               'user_posts': user_posts,
               'user_posts_length': user_posts_length,
               'button_text': button_text,
               'user_followers': user_followers,
               'user_following': user_following,}
    return render(request, 'profile.html', context)


@login_required(login_url='/signin')
def follow(request):
    if request.method == 'POST':
        if "follow" in request.POST:
            pageOwner = request.POST["pageowner"]
            follower = request.POST["follower"]
            
            if Follower.objects.filter(user = pageOwner, follower = follower).first():
                delete_follower = Follower.objects.get(user = pageOwner, follower = follower)
                delete_follower.delete()
                return redirect(f'/profile/{pageOwner}')
            
            else:
                new_follower = Follower.objects.create(user = pageOwner, follower = follower)
                new_follower.save()
                
                return redirect(f'/profile/{pageOwner}')
            
        elif "followers" in request.POST:
            pageOwner = request.POST["pageowner"]
            total_followers = Follower.objects.all()
            num_of_followers = len(total_followers)
            
            return HttpResponse(f"{num_of_followers}")
            
            
    else:
        return redirect('/')
    

class SearchProfile(View):
    def post(self, request):
        pk = request.POST["searchUsername"].lower()
        try:
            user_object = User.objects.filter(username__icontains = pk).order_by("username")
            if not user_object.exists():
                return HttpResponse("Doesn't exist!")
            else:
                user_objects_list = []
                profile_lists = []
                for user in user_object:
                    user_objects_list.append(user.id)
                    
                for each in user_objects_list:
                    profile_list = Profile.objects.filter(id_user = each)
                    profile_lists.append(profile_list)
                    
                profile_lists = [item for each_profile_object in profile_lists for item in each_profile_object]
                context = {'search': profile_lists}
            return render(request, 'search.html', context=context)
        except User.DoesNotExist:
            return HttpResponse("Doesn't exist!")
        
'''
def search_profile(request):
    if request.method == 'POST':
        pk = request.POST["searchUsername"].lower()
        try:
            user_object = User.objects.filter(username__icontains = pk).order_by("username")
            if not user_object.exists():
                return HttpResponse("Doesn't exist!")
            else:
                user_objects_list = []
                profile_lists = []
                for user in user_object:
                    user_objects_list.append(user.id)
                    
                for each in user_objects_list:
                    profile_list = Profile.objects.filter(id_user = each)
                    profile_lists.append(profile_list)
                    
                profile_lists = [item for each_profile_object in profile_lists for item in each_profile_object]
                context = {'search': profile_lists}
            return render(request, 'search.html', context=context)
        except User.DoesNotExist:
            return HttpResponse("Doesn't exist!")
        
'''       
'''  
            
            for each in emp:
                    profile_list = Profile.objects.filter(user = each)
                    profile_lists.append(profile_list)
                    
                allprofile_lists = list(chain(*profile_lists))
                
                    
                print(allprofile_lists)
                
                
                
                list(chain(*profile_lists))
                '''