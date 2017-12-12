import discord
import pickle
from random import choice

client = discord.Client()
LP=[]
j=0
clases=["Assaut du mage de bataille","Assaut du Croisé","Subterfuge de l'archère","Furie du guerrier","Tromperie du mage","Rituel de l'assasin","Négation du sorcier","Frappe du moine","Invocation de Magisfer","Instincts d'éclaireur"]
modo=['Santosvella','ArchFrost','jon357892','Nexos']

@client.event
async def on_message(message):
	

	if message.author == client.user:
		return
	

	if message.content.startswith('!randomadness'):
		modoac=0
		username=message.author.name
		for i in range(len(modo)):
			if username==modo[i]:
				modoac=+1
		if modoac>=1:
			print('randomadness lancé')
			global j
			if j==0:
				rl="Randomadness lancé taper !join pour rejoindre la liste d'attente"
				await client.send_message(message.channel,rl.format())
				j=+1
			else:
				rl="Randomadness deja lancé tapez !join pour rejoindre la liste d'attente"
				await client.send_message(message.channel,rl.format())
	

	if message.content.startswith('!pseudo'):
		pseudoliste=0
		pseudo=message.author.name
		pseudoig=message.content.split()
		with open('pseudodcliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudodiscordliste = mon_depickler.load()
		with open('pseudoigliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudoingameliste = mon_depickler.load()
		for i in range(len(pseudodiscordliste)):
			if pseudodiscordliste[i]==message.author.name:
				pseudoliste=pseudoliste+1
		if pseudoliste==0:
			pseudodiscordliste.append(message.author.name)
			pseudoingameliste.append(pseudoig[1])
		print(pseudodiscordliste)
		print(pseudoingameliste)
		with open('pseudodcliste','wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(pseudodiscordliste)
		with open('pseudoigliste','wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(pseudoingameliste)
	
	
	if message.content.startswith('!join'):
		uname=0
		if j>=1:
			username=message.author.name
			for i in range(len(LP)):
				if username==LP[i]:
					uname=+1
			if uname==0:
				LP.append(username)
				print(username,' a rejoin la liste d attente')
	

	if message.content.startswith('!liste'):
		aliste="Liste des joueurs : {}"
		await client.send_message(message.channel,aliste.format(LP))


	if message.content.startswith('!pliste'):
		with open('pseudodcliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudodiscordliste = mon_depickler.load()
		with open('pseudoigliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudoingameliste = mon_depickler.load()
		pliste="Voici la liste des pseudo enregistrer : \ndiscord = {} \ningame = {}"
		await client.send_message(message.channel,pliste.format(pseudodiscordliste,pseudoingameliste))
	

	if message.content.startswith('!unjoin'):
		if j>=1:
			username=message.author.name
			LP.remove(username)
			print(username,' a quiter la liste d attente')
	

	if message.content.startswith('!duel'):
		with open('pseudodcliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudodiscordliste = mon_depickler.load()
		with open('pseudoigliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudoingameliste = mon_depickler.load()
		if j>=1:
			NLP=0
			for i in range(len(LP)):
				NLP=NLP+1
			if NLP<=1:
				mp="Il faut plus de joueurs"
				await client.send_message(message.channel,mp.format())
			else:
				print('duel lancer')
				R1=choice(LP)
				J1=R1
				LP.remove(R1)
				R2=choice(LP)
				J2=R2
				LP.remove(R2)
				C1=choice(clases)
				C2=choice(clases)
				pig1=0
				pig2=0
				for i1 in range(len(pseudodiscordliste)):
					if J1==pseudodiscordliste[i1]:
						ig1=i1
						pig1=pig1+1
				if pig1>=1:
					pseudig1=pseudoingameliste[ig1]
				else:
					pseudig1='non précisé'
				for i2 in range(len(pseudodiscordliste)):
					if J2==pseudodiscordliste[i2]:
						ig2=i2
						pig2=pig2+1
				if pig2>=1:
					pseudig2=pseudoingameliste[ig2]
				else:
					pseudig2='non précisé'
				dnp="{} [ingame:{}] - {} \n---------------------------VS--------------------------- \n{} [ingame:{}] - {}"
				await client.send_message(message.channel,dnp.format(J1,pseudig1,C1,J2,pseudig2,C2))
		

	if message.content.startswith('!duel+'):
		with open('pseudodcliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudodiscordliste = mon_depickler.load()
		with open('pseudoigliste','rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			pseudoingameliste = mon_depickler.load()
		if j>=1:
			NLP=0
			for i in range(len(LP)):
				NLP=NLP+1
			if NLP<=1:
				mp="Il faut plus de joueurs"
				await client.send_message(message.channel,mp.format())
			else:
				if NLP%2==0:
					NLP=NLP/2
				else:
					NLP=NLP-1
					NLP=NLP/2
				for i in range(NLP):
					print('duel lancer')
					R1=choice(LP)
					J1=R1
					LP.remove(R1)
					R2=choice(LP)
					J2=R2
					LP.remove(R2)
					C1=choice(clases)
					C2=choice(clases)
					pig1=0
					pig2=0
					for i1 in range(len(pseudodiscordliste)):
						if J1==pseudodiscordliste[i1]:
							ig1=i1
							pig1=pig1+1
					if pig1>=1:
						pseudig1=pseudoingameliste[ig1]
					else:
						pseudig1='non précisé'
					for i2 in range(len(pseudodiscordliste)):
						if J2==pseudodiscordliste[i2]:
							ig2=i2
							pig2=pig2+1
					if pig2>=1:
						pseudig2=pseudoingameliste[ig2]
					else:
						pseudig2='non précisé'
					dnp="{} [ingame:{}] - {} \n---------------------------VS--------------------------- \n{} [ingame:{}] - {}"
					await client.send_message(message.channel,dnp.format(J1,pseudig1,C1,J2,pseudig2,C2))
	

	if message.content.startswith('!stop'):
		modoac=0
		username=message.author.name
		for i in range(len(modo)):
			if username==modo[i]:
				modoac=+1
		if modoac>=1:
			if j>=1:
				print('randomadness stoper')
				del LP[:]
				j=-1
	

	if message.content.startswith('!commandes'):
		cmd="Voici la liste des commandes que vous pouvez utiliser : \n!pseudo [pseudo ig] pour ajouter votre pseudo ig , \n!randomadness pour lancer le jeu (modo seulement) , \n!join pour vous mettre en liste d'attente , \n!liste pour afficher la liste des participants , \n!pliste affiche la liste des pseudo enregistrer, \n!unjoin pour vous retirer de la liste d'attente , \n!duel pour tirer au sort un match , \n!duel+ pour tirer plusieurs matchs, \n!stop pour arrêter le jeu (modo seulement) ,\n!commandes pour afficher la liste des commandes ."
		await client.send_message(message.channel,cmd.format())


@client.event
async def on_ready():
	with open('pseudodcliste','rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		pseudodiscordliste = mon_depickler.load()
	with open('pseudoigliste','rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		pseudoingameliste = mon_depickler.load()
	bnj="Bonjour"
#	await client.send_message(discord.Object(id='383618886806929419'),bnj.format())
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	print(pseudodiscordliste)
	print(pseudoingameliste)
	
client.run('MzgzNjE5MjIzNzU2MjEwMTc4.DPm45Q.Oy-nKyLUIurYn-wkMZnezBoaeb8')	#santosvallée
