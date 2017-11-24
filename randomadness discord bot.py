import discord
from random import choice

client = discord.Client()
LP=[]
j=0
clases=["Assaut du mage de bataille","Assault du Coisé","Subterfuge de l'archère","Furie du guerrier","Tromperie du mage","Rituel de l'assasin","Négation du sorcier","Frappe du moine","Invocation de Magisfer","Instincts d'éclaireur"]
pseudodiscord=['jon357892','Santosvella','ArchFrost','Glandeuranon','ptitjoueur']
pseudoig=['Jonathan357','Santosvella','ArchFrost','glandeuranon','Ptitjoueur']
modo=['Santosvella','ArchFrost','jon357892']

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
			global j
			if j==0:
				rl='Randomadness lancé taper !join pour rejoindre la liste d attente'
				await client.send_message(discord.Object(id='383618886806929419'),rl.format())
				j=+1
			else:
				rl='Randomadness deja lancé tapez !join pour jouer'
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
		aliste='liste des joueurs : {}'
		await client.send_message(discord.Object(id='383618886806929419'),aliste.format(LP))
	if message.content.startswith('!unjoin'):
		if j>=1:
			LP.remove(username)
			print(username,' a quiter la liste d attente')
	if message.content.startswith('!duel'):
		if j>=1:
			NLP=0
			for i in range(len(LP)):
				NLP=NLP+1
			if NLP<=1:
				mp='Il faut plus de joueurs'
				await client.send_message(message.channel,mp.format())
			else:
				R1=choice(LP)
				J1=R1
				LP.remove(R1)
				R2=choice(LP)
				J2=R2
				LP.remove(R2)
				C1=choice(clases)
				C2=choice(clases)
				for i in range(len(pseudodiscord)):
					if J1==pseudodiscord[i]:
						ig=i
						pig1=1
				if pig1==1:
					pseudig1=pseudoig[ig]
				else:
					pseudig1='non précisé'
				for i in range(len(pseudodiscord)):
					if J2==pseudodiscord[i]:
						ig=i
						pig2=1
				if pig2==1:
					pseudig2=pseudoig[ig]
				else:
					pseudig2='"non précisé'
				dnp1='{} [ ingame: {} ] - {}' 
				dnp2='{} [ ingame: {} ] - {}'
				await client.send_message(discord.Object(id='383618886806929419'),dnp1.format(J1,pseudig1,C1))
				await client.send_message(discord.Object(id='383618886806929419'),'---------------------------VS---------------------------')
				await client.send_message(discord.Object(id='383618886806929419'),dnp1.format(J2,pseudig2,C2))
	if message.content.startswith('!stop'):
			modoac=0
			username=message.author.name
			for i in range(len(modo)):
				if username==modo[i]:
					modoac=+1
			if modoac>=1:
				if j>=1:
					del LP[:]
					j=-1
	if message.content.startswith('!commande'):
		cmd='voila la liste des commande :'
		cmdrando='!randomadness pour lancé le jeu , '
		cmdj='!join pour vous metre en liste d attente ,'
		cmdl='!liste pour afficher la liste des participent , '
		cmduj='!unjoin pour vous retirer de la liste d attente , '
		cmdd='!duel pour tirer au sort un match ,'
		cmds='!stop pour arreter le jeu .'
		await client.send_message(discord.Object(id='383618886806929419'),cmd.format())
		await client.send_message(discord.Object(id='383618886806929419'),cmdrando.format())
		await client.send_message(discord.Object(id='383618886806929419'),cmdj.format())
		await client.send_message(discord.Object(id='383618886806929419'),cmdl.format())
		await client.send_message(discord.Object(id='383618886806929419'),cmduj.format())
		await client.send_message(discord.Object(id='383618886806929419'),cmdd.format())
		await client.send_message(discord.Object(id='383618886806929419'),cmds.format())

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