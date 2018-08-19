import pygame
import time

pygame.init()

#---------------------------------------------------------<< INITIALIZATION OF PYGAME VARIABLES >>------------------------------------------------------------

display_width = 1100            #variable for width
display_height = 650           #variable for height   

white=(255,255,255)		#display RGB values for white

game_display = pygame.display.set_mode((display_width,display_height))            #variable for display screen
pygame.display.set_caption("Dragon Ball Z Arcade Game")
clock = pygame.time.Clock()        						#variable for game's clock


#-------------------------------------------------------<< INITIALIZATION OF CHARACTER VARIABLES >>------------------------------------------------------------

	
x1=100					# initial X-position of Goku 
y1=250					# initial Y-position of Goku 

x2=900					# initial X-position of Frieza 
y2=250					# initial Y-position of Frieza 

xmin=0; ymin=50; xmax=930; ymax=370	# end coordinates of boundaries

crashed = False				# end-game or run-game condition		

x1_change=0
y1_change=0
x2_change=0
y2_change=0

goku_width = 99
goku_height = 225
frieza_width = 126
frieza_height = 226

goku_lives=30; frieza_lives=30

goku_punch_impact = 2; frieza_punch_impact = 2
goku_kick_impact = 1; frieza_kick_impact = 1
goku_mover = 0; frieza_mover = 0

goku_attack_allow=1; frieza_attack_allow=1

goku_attackspeed = 0.1; goku_attackpause = 0.1
frieza_attackspeed = 0.1; frieza_attackpause = 0.1

goku_punch_activate=0; goku_kick_activate=0; goku_hurt_activate=0
frieza_punch_activate=0; frieza_kick_activate=0; frieza_hurt_activate=0

gtime_i=0; gtime_f=0
ftime_i=0; ftime_f=0


g_pausetime_i=0; g_pausetime_f=0
f_pausetime_i=0; f_pausetime_f=0


#----------------------------------- IMAGE FILES FOR ANIMATIONS ------------------------------


goku_r1 = pygame.image.load('goku_right.png').convert()	# normal stance (same order followed everywhere)
goku_r2 = pygame.image.load('goku_rightkick.png').convert()	# kick stance
goku_r3 = pygame.image.load('goku_rightpunch.png').convert()	# punch stance
goku_r4 = pygame.image.load('goku_hurtright.png').convert()	# hurt stance

goku_h  = pygame.image.load('gokulife.png').convert()	# health bar

goku_l1 = pygame.image.load('goku_left.png').convert()	
goku_l2 = pygame.image.load('goku_leftkick.png').convert()	
goku_l3 = pygame.image.load('goku_leftpunch.png').convert()	
goku_l4 = pygame.image.load('goku_hurtleft.png').convert()	




frieza_l1 = pygame.image.load('frieza_left.png').convert()
frieza_l2 = pygame.image.load('frieza_leftkick.png').convert()
frieza_l3 = pygame.image.load('frieza_leftpunch.png').convert()
frieza_l4 = pygame.image.load('frieza_hurtleft.png').convert()

frieza_h  = pygame.image.load('friezalife.png').convert()	# health bar

frieza_r1 = pygame.image.load('frieza_right.png').convert()
frieza_r2 = pygame.image.load('frieza_rightkick.png').convert()
frieza_r3 = pygame.image.load('frieza_rightpunch.png').convert()
frieza_r4 = pygame.image.load('frieza_hurtright.png').convert()

gamelogo = pygame.image.load('gamelogo1.png').convert()

g_face = 1
f_face = -1

#------------------------------------ GOKU ANIMATION FUNCTIONS --------------------------------
 
def goku(x,y):
	if g_face==1:
		game_display.blit(goku_r1,(x,y))
	else:
		game_display.blit(goku_l1,(x,y))
def goku_kick(x,y):
	if g_face==1:
		game_display.blit(goku_r2,(x,y))
	else:
		game_display.blit(goku_l2,(x,y))

def goku_punch(x,y):
	if g_face==1:
		game_display.blit(goku_r3,(x,y))
	else:
		game_display.blit(goku_l3,(x,y))

def goku_hurt(x,y):
	if g_face==1:
		game_display.blit(goku_r4,(x,y))
	else:
		game_display.blit(goku_l4,(x,y))

def goku_health(x,y):
	if goku_lives==0:
		goku_lost()
	else:
		game_display.blit(goku_h,(x,y))


#------------------------------------ FRIEZA ANIMATION FUNCTIONS -------------------------------

def frieza(x,y):
	if f_face==1:
		game_display.blit(frieza_r1,(x,y))
	else:
		game_display.blit(frieza_l1,(x,y))

def frieza_kick(x,y):
	if f_face==1:
		game_display.blit(frieza_r2,(x,y))
	else:
		game_display.blit(frieza_l2,(x,y))

def frieza_punch(x,y):
	if f_face==1:
		game_display.blit(frieza_r3,(x,y))
	else:
		game_display.blit(frieza_l3,(x,y))

def frieza_hurt(x,y):
	if f_face==1:
		game_display.blit(frieza_r4,(x,y))
	else:
		game_display.blit(frieza_l4,(x,y))

def frieza_health(x,y):
	if frieza_lives==0:
		frieza_lost()
	else:
		game_display.blit(frieza_h,(x,y))

def game_logo(p,q):
	game_display.blit(gamelogo,(p,q))
#----------------------------------------TEXT DISPLAY FUNCTIONS----------------------------------------------

def text_objects(text,font):
	textSurface=font.render(text,False,black)
	return textSurface,textSurface.get_rect()
def message_display(text):
	Basicfont=pygame.font.Font('freesansbold.ttf',30)
	textsurf,textRect=text_objects(text,Basicfont)
	textRect.center=(250,250)
	game_display.blit(textsurf,textRect)

def frieza_lost():
	message_display("Frieza lost")

def goku_lost():
	message_display("Goku lost")


#----------------------------------HEALTH DISPLAY--------------------------------------------------------------

def goku_health(x,y):
	if goku_lives==0:
		goku_lost()
	else:
		game_display.blit(goku_h,(x,y))

def frieza_health(x,y):
	if frieza_lives==0:
		frieza_lost()
	else:
		game_display.blit(frieza_h,(x,y))

k=1
p=140
q=200
#-----------------------------------------------------------------------<< MAIN RUNTIME LOOP >>---------------------------------------------------------------------


while not crashed:			#condition to check the for the game to run continuously
	
	if k==1:
		game_display.fill(white)
		game_logo(p,q)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				k=0
#----------------------------- TIMER ATTACK ANIMATIONS --------------------------------------
	
	if goku_lives<=0 or frieza_lives<=0:
		crashed = True

	if (goku_kick_activate==1 or goku_punch_activate==1 or frieza_hurt_activate==1):		# timer for hurt/attack animation
		gtime_f = time.time()
		frieza_attack_allow=0
		if gtime_f - gtime_i >= goku_attackspeed:
			goku_kick_activate=0
			goku_punch_activate=0							# (deactivate all attack and hurt animations)
			frieza_hurt_activate=0
			frieza_attack_allow=1
			goku_attack_allow=0							# (restrict Goku from attacking)
			g_pausetime_i = time.time()						# (start measuring the time for which attack will be prohibited)

	if (frieza_kick_activate==1 or frieza_punch_activate==1 or goku_hurt_activate==1):
		ftime_f=time.time()
		goku_attack_allow=0
		if ftime_f - ftime_i >= frieza_attackspeed:
			frieza_kick_activate=0		
			frieza_punch_activate=0
			goku_hurt_activate=0
			goku_attack_allow=1
			f_pausetime_i = time.time()

	if g_pausetime_i!=0:
		g_pausetime_f = time.time()
		if g_pausetime_f - g_pausetime_i >= goku_attackpause:
			g_pausetime_i=0
			g_pausetime_f=0
			goku_attack_allow = 1

	if f_pausetime_i!=0:
		f_pausetime_f = time.time()
		if f_pausetime_f - f_pausetime_i >= frieza_attackpause:
			f_pausetime_i=0
			f_pausetime_f=0
			frieza_attack_allow = 1
	

#------------------------------- UPDATING PLAYER COORDINATES ----------------------------------------------------------------------


	
			#---------------------------- updating coordinates of Goku


	
	if (x1<=xmin and x1_change<0) or (x1>=xmax and x1_change>0)       or      ( ((x2-x1<=goku_width and x2>x1 and x1_change>0) or (x1-x2<=frieza_width and x1>x2 and x1_change<0))  and  ( (y1-y2<=frieza_height and y1>=y2) or (y2-y1<=goku_height and y2>=y1) ) ):				
		x1_change = 0		
								
	  		
	
	if (y1<=ymin and y1_change<0) or (y1>=ymax and y1_change>0)       or      ( ((y2-y1<=goku_height and y2>y1 and y1_change>0) or (y1-y2<=frieza_height and y1>y2 and y1_change<0))  and ( (x1-x2<=frieza_width and x1>=x2) or (x2-x1<=goku_width and x2>=x1) ) ):	
		y1_change = 0
	
	



			#----------------------------- updating coordinates of Frieza


	if (x2<=xmin and x2_change<0) or (x2>=xmax and x2_change>0)       or      ( ((x1-x2<=frieza_width and x1>x2 and x2_change>0) or (x2-x1<=goku_width and x2>x1 and x2_change<0))  and ( (y1-y2<=frieza_height and y1>=y2) or (y2-y1<=goku_height and y2>=y1) ) ):		
		x2_change = 0
	
	
	
	if (y2<=ymin and y2_change<0) or (y2>=ymax and y2_change>0)       or      ( ((y1-y2<=frieza_height and y1>y2 and y2_change>0) or (y2-y1<=goku_height and y2>y1 and y2_change<0))   and ( (x1-x2<=frieza_width and x1>=x2) or (x2-x1<=goku_width and x2>=x1) ) ):
		y2_change = 0


	x1+=x1_change
	y1+=y1_change
	x2+=x2_change
	y2+=y2_change
	
#------------------------ RESETTING DISPLAY TO WHITE AND UPDATING -----------------------

	
	pygame.display.update()
	game_display.fill(white) 		


#------------------------------- PRINTING CHARACTER FRAMES ------------------------------

	if goku_hurt_activate==1:
		if g_face==1:
			if frieza_punch_activate==1:
				goku_hurt(x2 - 184, y1)
			elif frieza_kick_activate==1:
				goku_hurt(x2 - 224, y1)
		elif g_face==-1:
			if frieza_punch_activate==1:
				goku_hurt(x2 + 218, y1)
			elif frieza_kick_activate==1:
				goku_hurt(x2 + 298, y1)
	
	elif goku_kick_activate==1:			#display Goku's animations
		goku_kick(x1 + g_face * 50, y1)

	elif goku_punch_activate==1:
		goku_punch(x1 + g_face * 30, y1)

	else:
		goku(x1,y1)
	



	if frieza_hurt_activate==1:
		if f_face==1:
			if goku_punch_activate==1:
				frieza_hurt(x1 - 220, y2)
			elif goku_kick_activate==1:
				frieza_hurt(x1 - 250, y2)
		elif f_face==-1:
			if goku_punch_activate==1:
				frieza_hurt(x1 + 200, y2)
			elif goku_kick_activate==1:
				frieza_hurt(x1 + 275, y2)

	elif frieza_kick_activate==1:			#display Frieza's animations
		frieza_kick(x2 + f_face * 60, y2)

	elif frieza_punch_activate==1:
		frieza_punch(x2 + f_face * 30, y2)

	else:
		frieza(x2,y2)					
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True


#-------------------------------------------PRINTING HEALTHBARS-------------------------

	for i in range(goku_lives):
		goku_health( 4 + i * 12, 16)
	for i in range(frieza_lives):
		frieza_health( 1086 - i * 12, 16)	

#------------------------------------------- MOVEMENT ------------------------------------------------------------------------------------	
	if event.type == pygame.KEYDOWN:

		if event.key == pygame.K_LEFT:		# moving Frieza
			f_face=-1
			x2_change=-5
			
		elif event.key == pygame.K_RIGHT:
			f_face=1
			x2_change=5
			
		elif event.key == pygame.K_UP:
			y2_change=-5
			
		elif event.key == pygame.K_DOWN:
			y2_change=5
			


		elif event.key == pygame.K_w:		# moving Goku	
			y1_change=-5
			
		elif event.key == pygame.K_s:
			y1_change=5
			
		elif event.key == pygame.K_a:
			g_face=-1
			x1_change=-5
			
		elif event.key == pygame.K_d:
			g_face=1
			x1_change=5
			
				
#----------------------------------- GOKU'S ATTACKS --------------------------------------

		if event.key == pygame.K_LCTRL:		# Goku's kick
			if goku_attack_allow==1:
				goku_kick_activate=1
				gtime_i=time.time()
				x1_change=0
				y1_change=0
			
				if goku_kick_activate==1:
					goku_attack_allow=0
					if (x2-x1<=200 and x2>x1) and abs(y2-y1)<=100 and g_face==1:
						frieza_hurt_activate=1
						frieza_lives -= goku_kick_impact
						f_face=-1
					elif (x1-x2<=150 and x1>x2) and abs(y2-y1)<=100 and g_face==-1:
						frieza_hurt_activate=1
						frieza_lives -= goku_kick_impact
						f_face=1
			
		
		if event.key == pygame.K_LALT:		# Goku's punch
			if goku_attack_allow==1:
				goku_punch_activate=1
				gtime_i=time.time()
				x1_change=0
				y1_change=0
			
				if goku_punch_activate==1:
					goku_attack_allow=0
					if (x2-x1<=110 and x2>x1) and abs(y2-y1)<=70 and g_face==1:
						frieza_hurt_activate=1
						frieza_lives -= goku_punch_impact
						f_face=-1
					elif (x1-x2<=130 and x1>x2) and abs(y2-y1)<=70 and g_face==-1:
						frieza_hurt_activate=1
						frieza_lives -= goku_punch_impact
						f_face=1
			

#---------------------------------- FRIEZA'S ATTACKS --------------------------------------

		if event.key == pygame.K_RCTRL:		# Frieza's kick
			if frieza_attack_allow==1:
				frieza_kick_activate=1
				ftime_i=time.time()
				x2_change=0
				y2_change=0
				if frieza_kick_activate==1:
					frieza_attack_allow=0
					if (x1-x2<=150 and x1>x2) and abs(y1-y2)<=100 and f_face==1:
						goku_hurt_activate=1
						goku_lives -= frieza_kick_impact
						g_face=-1
					elif (x2-x1<=150 and x2>x1) and abs(y1-y2)<=100 and f_face==-1:
						goku_hurt_activate=1
						goku_lives -= frieza_kick_impact
						g_face=1


		if event.key == pygame.K_RALT:		# Frieza's punch
			if frieza_attack_allow==1:
				frieza_punch_activate=1
				ftime_i=time.time()
				x1_change=0
				y1_change=0
			
				if frieza_punch_activate==1:
					frieza_attack_allow=0
					if (x1-x2<=140 and x1>x2) and abs(y1-y2)<=70 and f_face==1:
						goku_hurt_activate=1
						goku_lives -= frieza_punch_impact
						g_face=-1
					elif (x2-x1<=100 and x2>x1) and abs(y1-y2)<=70 and f_face==-1:
						goku_hurt_activate=1
						goku_lives -= frieza_punch_impact
						g_face=1

#--------------------------------------- KEYUP CODE ---------------------------------------
			
	if event.type == pygame.KEYUP:
		
		if event.key==pygame.K_a or event.key==pygame.K_d:
			x1_change=0
		if event.key==pygame.K_w or event.key==pygame.K_s:
			y1_change=0
		if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
			x2_change=0
		if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
			y2_change=0

#------------------------------------------------------------------------------------------
			

	clock.tick(100)					# setting clock speed

pygame.quit()
quit()