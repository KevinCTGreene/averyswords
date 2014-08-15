from django.shortcuts import render, get_object_or_404
from models import Flashcard
from django.http import HttpResponseRedirect, HttpResponse 
from django.http import Http404
from googlescraper import google_image
import datetime
import collections

def getActiveWords():
	
	wordlist = Flashcard.objects.all()
	active = []
	for item in wordlist:
		margin = item.activedate + datetime.timedelta(days=5)
		if margin >= datetime.date.today() >= item.activedate:
			active.append(item)
			
	active = sorted(active, key=lambda x: x.content)
	return active
	
#The main page
def home(request):
		
		
	#Words of the week
	active_words = getActiveWords()

	#Old words - where activedate is less than 5 days ago				
	old_words = Flashcard.objects.filter(activedate__lt=(datetime.date.today() - datetime.timedelta(days=5)))
      
	#Mastered words go here - mastered box is checked
	mastered_words = Flashcard.objects.filter(mastered=True)
	
	
	#Words for review - marked box is checked
	marked_words = Flashcard.objects.filter(marked=True)
	
	#Map the lists of objects for use in the template
	context = {'active_words': active_words, 'old_words': old_words, 'mastered_words': mastered_words,'marked_words': marked_words}
	#Return the rendered page
   
	return render(request, 'flashcards/index.html', context)
        
def index(request):
	pass

#The detail page for each word
def detail(request, flashcard_id):

			
			
		#Return 404 is specific object does not exist
		output = get_object_or_404(Flashcard,content=flashcard_id)
				#Scrape Google image search for the first image matching the word
		try:
			image_address = google_image(output.content)
		except:	
			image_address = None
			
		prev_word = None
		next_word = None
		
		if Flashcard.objects.get(content=flashcard_id) in getActiveWords():
			active_words = getActiveWords()

			i = [p for p,x in enumerate(active_words) if x.content == flashcard_id] #returns index of said item
			i = i[0]
			
			
			if i == 0:
				try: 
					next_word = active_words[i+1]
				except IndexError:
					next_word = None
			elif i == 4:
				try:
					prev_word = active_words[i-1]
				except IndexError:
					prev_word = None
			else:
				try:
					next_word = active_words[i+1]
				except IndexError:
					next__word = None
				try: 
					prev_word = active_words[i-1]
				except IndexError:
					prev_word = None
		else:
                        active_words = []
		

		
		#output.times_viewed += 1
		
		
		
		
		#Return the rendered page
		return render(request, 'flashcards/detail.html', {'flashcard': output, 'image_address': image_address, 'next_word': next_word, 'prev_word': prev_word, 'active_words': active_words})

def update(request, flashcard_id):
	output = get_object_or_404(Flashcard,content=flashcard_id)
	checkbox = request.POST.get('check1', None)
	if checkbox == "marked":
		output.marked = True
		output.save()
	else:
		output.marked = False
		output.save()
		
	checkbox2 = request.POST.get('check2', None)
	if checkbox2 == "mastered":
		output.mastered = True
		output.save()
	else:
		output.mastered = False
		output.save()
	return HttpResponseRedirect('/words/%s/' % flashcard_id)
