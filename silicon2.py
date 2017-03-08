import sys
import pygame
from pygame.locals import *


pygame.init()
fps   = pygame.time.Clock()
size  = width,height = 1280,720
ascii = "abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*"
black = [0,0,0]
red   = [255,0,0]
green = [0,255,0]
blue  = [0,0,255]
gray  = [[211,211,211],[215,215,215],[227,227,227],[239,239,239]]
white = [255,255,255]

class disptext:
	def __init__(self,text,color,location,screen,text_size = 25,speed =[0,0]):
		self.text = text
		self.color = color
		self.location = location
		self.screen = screen
		self.speed = speed
		self.size= text_size


	def textobj(self):
		self.surface = self.font.render(self.text,True,self.color)
		self.surfacerect = self.surface.get_rect()
		
	def permadisplaytext(self):
		
		self.font = pygame.font.SysFont('couriernew.ttf',self.size)
		self.textobj()
		self.surfacerect.left,self.surfacerect.top= self.location
		self.screen.blit(self.surface,self.surfacerect)
		
	def move(self):
		self.location[0]+=self.speed[0]
		self.location[1]+=self.speed[1]
	
	def update(self,text,color):
		self.text = text
		self.color = color
		
		
		


		
class imageloader:
	def __init__(self,image,pos,screen):
		self.screen=screen
		self.image = pygame.image.load(image)
		self.imagerect = self.image.get_rect()
		self.imagerect.left,self.imagerect.top = pos
	def delcolor(self,color):
		self.image.set_colorkey(color)
		
	def update(self):
		self.screen.blit(self.image,self.imagerect)
		
	def move(self,speed):
		self.imagerect = self.imagerect.move(speed)
		self.screen.blit(self.image,self.imagerect)
		
		
class hero(imageloader):
	def __init__(self,cord,image,speed,screen):
		imageloader.__init__(self,image,cord,screen)
		self.cord  = cord
		self.speed = speed
		
	def updatepos(self):
		self.imagerect = self.imagerect.move(self.speed)
		self.screen.blit(self.image,self.imagerect)
		
	def updateimage(self,image):
		self.image = pygame.image.load(image)
		self.imagerect = self.image.get_rect()
		self.screen.blit(self.image,self.imagerect)
		
		
		
		
class levels:
	
	def __init__(self,screen):
		self.playername  	   	= ''
		self.silatom     	   	= {'no':3888,'rate':2}
		self.phatom      	   	= {'no':1,'rate':.002}
		self.bratom            	= {'no':1,'rate':.002}
		self.playersp      	   	= ""
		self.playerresp  	   	= ['','','','']
		self.displayplayerresp 	= [0,0,0,0,0]
		self.screen = screen
		self.properresp		   	= ['hi','hi!','hello']
		self.textatoms  	   	= {'Si':disptext("number of sillicon atoms    :"+ str(int(self.silatom['no'])),black,[40,60],self.screen),
						          'P': disptext("number of phosphor atoms :"+ str(int(self.phatom['no'])),black,[40,80],self.screen),
								  'Br':disptext("number of boron atoms       :"+ str(int(self.bratom['no'])),black,[40,100],self.screen),}
		
		
		self.tabtext 	 		= {'t1':disptext("MINE",black,[40,10],self.screen)}
		
		self.bglayers    		= {"lay0":pygame.Rect((12,27),(1256,676)),
								   "lay1":pygame.Rect((15,30),(1250,670)),
								   "lay2":pygame.Rect((1280,300),(880,3))}
						 
		self.bgspeed      		= {"lay0":[0,0],"lay1":[0,0],"lay2":[-2,0]}
		
		self.speechbubble 		= {'dev0':imageloader("speech.bmp",[550,60],self.screen)}
		
		self.creditspeed 		=  [[0,-1],[-4,0]]
		
		self.speech		  		= {'dev0':disptext("this is the devoloper sahil. say HI!",black,[560,70],self.screen,20),
								   'dev1':disptext(self.playersp,black,[560,80],self.screen,20),
								   'dev2':disptext("HI ! player what is your name",black,[560,90],self.screen,20),
								   'dev3':disptext("well thats a weird way to say hi by the way whats your name",black,[560,90],self.screen,20),
								   'dev4':disptext(self.playersp,black,[560,100],self.screen,20),
								   'dev5':disptext("well hello there",black,[560,110],self.screen,20),
								   'dev6':disptext("wow youre name is sahil too , say what , do you want a special feature",black,[560,110],self.screen,20),
								   'dev7':disptext(self.playersp,black,[560,120],self.screen,20),
								   'dev8':disptext("ok here is your feature, color",black,[560,130],self.screen,20),
								   'dev9':disptext("ill allow you to skip to the end",black,[560,130],self.screen,20),
								   
								   
								   
								   
								   
								   'nar0':disptext("WAAAAIIIIITTTTTT",black,[1280,130],self.screen,30,self.creditspeed[1])}
						
		self.credits 			=  imageloader("ball.bmp",[272,720],self.screen)

		
		self.devoloper 			=  hero([1280,255],"sahilbw.bmp",[-5,0],self.screen)
		
		
		
		self.devoloper.delcolor(white)
		self.speechbubble['dev0'].delcolor(white)
		
		
		
		
	def level1(self):
	
		self.textatoms['Si'].update("number of sillicon atoms :"+ str(int(self.silatom['no'])),black)
		self.textatoms['Si'].permadisplaytext()
		self.silatom['no']+=self.silatom['rate']
		
		
	def level2(self):
		self.level1()
		self.textatoms['P'].update("number of phosphor atoms :"+ str(int(self.phatom['no'])),black)
		self.textatoms['Br'].update("number of boron atoms    :"+ str(int(self.bratom['no'])),black)
		
		self.textatoms['P'].permadisplaytext()
		self.textatoms['Br'].permadisplaytext()
		
		self.bratom['no']+=self.bratom['rate']
		self.phatom['no']+=self.phatom['rate']
		
		if self.silatom['no']>4000 and level==2:
			self.intro_dev()
		
		
	def level3(self):
		
		pygame.draw.rect(self.screen,black,self.bglayers['lay0'])
		pygame.draw.rect(self.screen,gray[3],self.bglayers['lay1'])
		self.level2()

		
	def level4(self):
		self.level3()
		pygame.draw.polygon(self.screen,black,((12,29),(113,29),(100,3),(25,3)),3)
		pygame.draw.polygon(self.screen,gray[3],((14,30),(111,30),(98,5),(28,5)))
		self.tabtext['t1'].permadisplaytext()
		
		
	def intro_dev(self):
		if self.bglayers['lay2'].left>400:
			self.bglayers['lay2']=self.bglayers['lay2'].move(self.bgspeed['lay2'])
		pygame.draw.rect(self.screen,black,self.bglayers['lay2'])
		
		if self.bglayers['lay2'].left==400 and self.devoloper.imagerect.left>550:
			self.devoloper.updatepos()
			
		self.devoloper.screen.blit(self.devoloper.image,self.devoloper.imagerect)
		
		
		if self.devoloper.imagerect.left==550:
			self.speechbubble['dev0'].update()
			self.speech["dev0"].permadisplaytext()
			self.speech['dev1'].update(self.playersp,black)
		
			if not self.playerresp[0] :self.speech["dev1"].permadisplaytext()
			
			
			if self.playerresp[0] in self.properresp[0:3]:
				self.displayplayerresp[0] = 1
			
			if self.displayplayerresp[0] or len(self.playerresp[0])>2:
				self.text_input(0,'dev1','dev2','dev3',len(self.playerresp[0])>2)
				self.speech['dev4'].update(self.playersp,black)
				
				if not self.playerresp[1] :self.speech["dev4"].permadisplaytext()
			
				if self.playerresp[1]:
					self.displayplayerresp[1] = 1
					self.fastfinish = self.playerresp[1]=='sahil'
					self.playername = self.playerresp[1]
					self.speech['dev5'].update("well helo there "+self.playername + " do you want a new feature",black)
					
				if self.displayplayerresp[1] :
					self.text_input(1,'dev4','dev5','dev6',self.fastfinish)
					self.speech['dev7'].update(self.playersp,black)
				if not self.playerresp[2] :self.speech["dev7"].permadisplaytext()
				
				if self.playerresp[2]:
					self.displayplayerresp[2] = 1
					
				if self.displayplayerresp[2]:
					self.text_input(2,'dev7','dev8','dev9',self.fastfinish)
					if self.fastfinish:
						self.fake_ending()
			
			
	def text_input(self,speechno,str1,str2,str3,condition):
		self.speech[str1].update(self.playerresp[speechno],black)
		self.speech[str1].permadisplaytext()
		
		if condition:
			self.speech[str3].permadisplaytext()
			
		elif self.displayplayerresp[speechno]:
			self.speech[str2].permadisplaytext()
		
	def fake_ending(self):
		self.screen.fill(white)
		self.credits.update()
		if self.credits.imagerect.top >200:
			self.credits.move(self.creditspeed[0])
		
		elif self.credits.imagerect.top == 200:
			self.speech['nar0'].permadisplaytext()
			if self.speech['nar0'].surfacerect.left > 580:
				self.speech['nar0'].move()
				
				

		
def main():

	global level
	level = 2
	screen = pygame.display.set_mode(size)
	screen.fill(white)
	pygame.display.update()
	main_lvl = levels(screen)
	respondkey = 0
	while 1:
	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			
			elif event.type == KEYDOWN:
				if chr(event.key) in ascii:
					main_lvl.playersp+=chr(event.key)
					
				elif event.key == K_RETURN:
					main_lvl.playerresp[respondkey] = main_lvl.playersp
					main_lvl.playersp = ''
					respondkey+=1

		screen.fill(white)
		if level == 1:
			main_lvl.level1()
			if main_lvl.silatom['no'] ==1000:
				level = 2
				
		elif level == 2:
			main_lvl.level2()
			
		
		elif level == 3:
			main_lvl.level4()
		
		print(fps.get_fps())
		fps.tick(60)
		
		
		
		pygame.display.update()
		a=fps.get_fps()
main()