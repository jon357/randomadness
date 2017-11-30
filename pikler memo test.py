import pickle


with open('donnees','wb') as fichier:
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(variable)


with open('donnees','rb') as fichier:
	mon_depickler = pickle.Unpickler(fichier)
	var_recupere = mon_depickler.load()
