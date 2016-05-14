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

def percentage_plot(request):
	population_percent = [[x, 100*(ages_uk[x]/ages_uk['all'])] for x in ages_uk if x != 'all']
	users = User.objects.all()
	users_number = len(users)
	users_age = [x.age for x in users]

	users_age = Counter(users_age)
	users_age = [[key, value] for key, value in users_age.items() if 0 <= key <= 90]
	users_percent = [[x[0], 100*(x[1]/users_number)] for x in users_age]

	for i in range(91):
		if i not in [x[0] for x in users_age]:
			users_age.append([i, 0])
	users_age.sort(key=lambda x: x[0])

	weighted_users = []
	for i in range(len(population_percent)):
		try:
			weighted_users.append([population_percent[i][0], int((population_percent[i][1]/users_percent[i][1])*users_age[i][1])])
		except IndexError:
			weighted_users.append([population_percent[i][0], 0])


	stats = [users_age, weighted_users]
	return render(request, 'weighted_users.html', {'stats':stats})




	
	