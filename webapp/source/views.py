# Create your views here.
from django.views.generic.simple import direct_to_template
from source.models import User, UserForm

def index (request):
    return direct_to_template(request, 'source/index.html', {'login':request.session.get('user')})

def login (request):
   if request.method == 'POST':
       if request.POST['submit'] == 'register':
            form = UserForm(request.POST)
            form.save()
            setSessionUser(request, request.POST['name'], request.POST['password'])
       if request.POST['submit'] == 'login':
            setSessionUser(request, request.POST['name'], request.POST['password'])
       if request.POST['submit'] == 'logout':
            del request.session['user']

   return index(request)

def setSessionUser(request, name, password):
   user = User.objects.get(name=name, password=password)
   request.session['user'] = user
