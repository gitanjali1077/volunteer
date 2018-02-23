from django.shortcuts import render, redirect
from register.forms import PostForm
# Create your views here.
from .models import vacancy
from django.shortcuts import render_to_response, get_object_or_404

def indexs(request):
    #a=string
   # profile_form=ProfileForm(request.GET)
   # template = a+'.html'
    return render(request , 'vacancy.html' , {
        
        'posts': vacancy.objects.all()
    })

def detail(request, oid):
    a=vacancy.objects.filter(id=oid).first()
   # profile_form=ProfileForm(request.GET)
   # template = a+'.html'
    return render(request , 'detail.html' , {
        
        'val': a
    })

def add_post(request):
  msgs=''
  post_form=PostForm(request.GET)
  button="Create post"
    #if request.user.username:
      # for empty form
  if request.method == 'GET':
  
    return render(request, 'add_post.html',{'post_form':post_form,'button':button })


  if request.method == 'POST':
        post_form = PostForm(request.POST)
       
        if post_form.is_valid() :
           ab="post chala"       
           post = post_form.save(commit=False)
            
           #prof= profile_form.save()
           title = post_form.cleaned_data['title']
           body = post_form.cleaned_data['body']
           address = post_form.cleaned_data['address']
           city = post_form.cleaned_data['city']
           no_of_vacancies = post_form.cleaned_data['no_of_vacancies']
           last_date = post_form.cleaned_data['last_date']
           
           #profile=profile_form.save(commit=False)
           #profile.user_id=user1.id+1
           #profile.college=profile_form.cleaned_data['college']
           #profile.save()
         
           post.save()
           msgs="New Post added!" 
               #return redirect('index.html')
           return render(request, 'add_post.html',{'post_form':post_form, 'msgs':msgs,'button':button})
   
        else:
             msgs="Some error occured!" 
             return render(request, 'add_post.html',{'post_form':post_form, 'msgs':msgs,'button':button})
   
       
      

  return render(request, 'add_post.html',{'post_form':post_form})

def post_update(request,oid=None):
  msgs=''
  instance = get_object_or_404(vacancy,id=oid)
  post_form=PostForm(request.POST or None,instance=instance)
  button="update post"
           
  if post_form.is_valid() :
           ab="post chala"       
           post = post_form.save(commit=False)
            
           #prof= profile_form.save()
           title = post_form.cleaned_data['title']
           body = post_form.cleaned_data['body']
           address = post_form.cleaned_data['address']
           city = post_form.cleaned_data['city']
           no_of_vacancies = post_form.cleaned_data['no_of_vacancies']
           last_date = post_form.cleaned_data['last_date']
           
           #profile=profile_form.save(commit=False)
           #profile.user_id=user1.id+1
           #profile.college=profile_form.cleaned_data['college']
           #profile.save()
         
           post.save()
           msgs=" Post Updated!" 
               #return redirect('index.html')
           return render(request, 'add_post.html',{'post_form':post_form, 'msgs':msgs,'button':button})
   
  else:
             msgs=""
             button="update post"
             return render(request, 'add_post.html',{'post_form':post_form, 'msgs':msgs,'button':button})
   
  return render(request, 'add_post.html',{'post_form':post_form})

def post_delete(request,oid=None):
  msgs='post sucessfully deleted'
  instance = get_object_or_404(vacancy,id=oid)
  instance.delete()         
  return redirect('/application/')
