from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter
from .ages import ages_uk

from .models import Geos, Geos_Multi, Geom, User

# Create your views here.

def countries(request):
	geoses = [x.id for x in Geos.objects.all() if x.m_type == 'country']
	geoses = geoses + [x.id for x in Geos_Multi.objects.all() if x.m_type == 'country']
	data = [x for x in Geom.objects.all() if x.id in geoses] 
	return render(request, 'countries.html', {'data':data})

def regions(request):
	geoses = [x.id for x in Geos.objects.all() if x.m_type == 'region']
	geoses = geoses + [x.id for x in Geos_Multi.objects.all() if x.m_type == 'region']
	data = [x for x in Geom.objects.all() if x.id in geoses] 
	return render(request, 'regions.html', {'data':data})

def districts(request):
	geoses = [x.id for x in Geos.objects.all() if x.m_type == 'district']
	geoses = geoses + [x.id for x in Geos_Multi.objects.all() if x.m_type == 'district']
	data = [x for x in Geom.objects.all() if x.id in geoses] 
	return render(request, 'districts.html', {'data':data})

def territory(request, reg_id):
	territory = Geom.objects.get(id=reg_id)
	return render(request, 'region.html', {'territory':territory})

def index(request):
	return render(request, 'index.html')

def user_plot(request):
	users = User.objects.all()
	users = [x for x in users if x.age > 0]

	female_all = [x.age for x in users if x.gender == 2]
	female = dict(Counter(female_all))
	female = [[key, value] for key, value in female.items()]

	male_all = [x.age for x in users if x.gender == 1]
	male = dict(Counter(male_all))
	male = [[key, value] for key, value in male.items()]

	unk_all = [x.age for x in users if x.gender == 0]
	unk = dict(Counter(unk_all))
	unk = [[key, value] for key, value in unk.items()]

	ages = [[x, len(users)*(ages_uk[x]/ages_uk['all'])] for x in ages_uk if x != 'all']
	print(ages)
	census = [[x[0], x[1]] for x in ages]

	w_fem = [x[:] for x in female]
	w_mal = [x[:] for x in male]
	w_unk = [x[:] for x in unk]

	for i in range(len(ages)):
		for j in range(len(female)):
			if ages[i][0] == w_fem[j][0]:
				w_fem[j][1] = ages[i][1] * w_fem[j][1] 
		for k in range(len(w_mal)):
			if ages[i][0] == w_mal[k][0]:
				w_mal[k][1] = ages[i][1] * w_mal[k][1] 
		for l in range(len(w_unk)):
			if ages[i][0] == w_unk[l][0]:
				w_unk[l][1] = ages[i][1] * w_unk[l][1] 

	users = [female, male, unk, w_fem, w_mal, w_unk, census]
	return render(request, 'users.html', {'users':users})
	