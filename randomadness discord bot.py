import discord
from random import choice

client = discord.Client()
LP=[]
j=0
clases=["Assaut du mage de bataille","Assaut du Croisé","Subterfuge de l'archère","Furie du guerrier","Tromperie du mage","Rituel de l'assasin","Négation du sorcier","Frappe du moine","Invocation de Magisfer","Instincts d'éclaireur"]
pseudodiscord=['jon357892','Santosvella','ArchFrost','Glandeuranon','ptitjoueur','K13b3r','poulpix69','Nexos']
pseudoig=['Jonathan357','Santosvella','ArchFrost','glandeuranon','Ptitjoueur','K13b3r','poulpix69','Nexos999']
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
				rl="Randomadness lancé taper !join pour rejoindre la liste d attente"
				await client.send_message(discord.Object(id='383618886806929419'),rl.format())
				j=+1
			else:
				rl="Randomadness deja lancé tapez !join pour jouer"
				await client.send_message(discord.Object(id='383618886806929419'),rl.format())
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
		await client.send_message(discord.Object(id='383618886806929419'),aliste.format(LP))
	if message.content.startswith('!unjoin'):
		if j>=1:
			username=message.author.name
			LP.remove(username)
			print(username,' a quiter la liste d attente')
	if message.content.startswith('!duel'):
		if j>=1:
			NLP=0
			for i in range(len(LP)):
				NLP=NLP+1
			if NLP<=1:
				mp="Il faut plus de joueurs"
				await client.send_message(discord.Object(id='383618886806929419'),mp.format())
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
				for i1 in range(len(pseudodiscord)):
					if J1==pseudodiscord[i1]:
						ig1=i1
						pig1=pig1+1
				if pig1>=1:
					pseudig1=pseudoig[ig1]
				else:
					pseudig1='non précisé'
				for i2 in range(len(pseudodiscord)):
					if J2==pseudodiscord[i2]:
						ig2=i2
						pig2=pig2+1
				if pig2>=1:
					pseudig2=pseudoig[ig2]
				else:
					pseudig2='non précisé'
				dnp="{} [ingame:{}] - {} \n---------------------------VS--------------------------- \n{} [ingame:{}] - {}"
				await client.send_message(discord.Object(id='383618886806929419'),dnp.format(J1,pseudig1,C1,J2,pseudig2,C2))
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
		cmd="Voici la liste des commandes que vous pouvez utiliser : \n!randomadness pour lancer le jeu (modo seulement) , \n!join pour vous mettre en liste d'attente , \n!liste pour afficher la liste des participants , \n!unjoin pour vous retirer de la liste d'attente , \n!duel pour tirer au sort un match , \n!stop pour arrêter le jeu (modo seulement) ,\n!commandes pour afficher la liste des commandes ."
		await client.send_message(discord.Object(id='383618886806929419'),cmd.format())

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

#client.run('MzgwMTMwMTYyMjI3OTM3Mjgy.DO0Idg.TTH3LMVssf9BC2mncXXOZcXeusc')	#jon test bot
#client.run('MzgyOTc0NDI1MDA5NDg3ODgz.DPdgSQ.owv2T2CX-xHuip0MhDjUI7R6WZQ')	#test bot priver
client.run('MzgzNjE5MjIzNzU2MjEwMTc4.DPm45Q.Oy-nKyLUIurYn-wkMZnezBoaeb8')	#santosvallée
#discord.Object(id='383618886806929419')
