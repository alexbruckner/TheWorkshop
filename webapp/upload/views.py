# Create your views here.
from django.core.urlresolvers import reverse
from filetransfers.api import prepare_upload
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from models import UploadForm

#http://www.allbuttonspressed.com/projects/django-filetransfers
from upload.models import UploadModel
from java.views import test_basic_addition, java_compile_and_execute

def upload_handler(request):
    view_url = reverse('upload.views.upload_handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(view_url)

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadForm()
    return direct_to_template(request, 'upload/upload.html',
            {'form': form,
             'upload_url': upload_url,
             'upload_data': upload_data,
             'uploaded' : UploadModel.objects.all(),
             'test_string' : test_basic_addition(),
    })

def upload_code(request):
    source = request.POST['code']
    return direct_to_template(request, 'source/index.html',
            {'source' : source,
             'result' : java_compile_and_execute(source),
    })

