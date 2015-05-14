from django.shortcuts import render_to_response
from readreview.models import movie, comments

# Create your views here.
def home(request):

	""" receives home page request and serves the display html
	    input : home page request
	    returns : display.html 
	"""
	#first 10 entries in the movies table
	values = movie.objects.all()[:10]
	#movie entries passed as dictionary
	return render_to_response('display.html',{'movie':values})

####
from django.http import HttpResponseRedirect
from readreview import commentsForm

def comments(request):
    # checking data for POST request
    if request.method == 'POST':
        form = commentsForm(request.POST)
	formObj = form.save(commit = False)
	name = request.POST.get('name')
	comments = request.POST.get('comments')
	formObj = comments(name,comments)
	formObj.save()
        return HttpResponseRedirect('/')


