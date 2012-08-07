from foos.models import Foo, FooForm

from django.shortcuts import render_to_response
from django.template import RequestContext

def foo(request):
    if request.method == 'POST':
        form = FooForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: return HttpResponseRedirect(Foo.get_absolute_url())
        else:
            pass # TODO: error
    else:
        form = FooForm()
    #variables = RequestContext(request, { 'form' : form })
    #return render_to_response('form.html', variables)
    objs = Foo.objects.all()
    return render_to_response('form.html', { 'form' : form, 'objs' : objs })
