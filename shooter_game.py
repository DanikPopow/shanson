from pygame import *
from random import randint

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption('Космос')

ground = image.load('galaxy.jpg')
ground = transform.scale(ground,(win_width,win_height))

mixer.init()
mixer.music.load('Spaceee.ogg') 
mixer.music.play()

class GameSprite(sprite.Sprite):
	def __init__(self,img,w,h,x,y,speed):
		sprite.Sprite.__init__(self)
		self.w=w 
		self.h=h 
		self.image = image.load(img)
		self.image = transform.scale(self.image, (self.w, self.h))
		self.rect = self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.speed=speed
	def reset(self):
		window.blit(self.image ,(self.rect.x, self.rect.y))

class Player(GameSprite):
	def __init__(self,img,w,h,x,y,speed):
		GameSprite.__init__(self,img,w,h,x,y,speed)
	def update(self):
		keys = key.get_pressed()
		if keys[K_a] and self.rect.x>0:
			self.rect.x-=self.speed
		elif keys[K_d] and self.rect.x+self.w<win_width:
			self.rect.x+=self.speed
			
class UFO(GameSprite):
	def __init__(self,img,w,h,x,y,speed):
		GameSprite.__init__(self,img,w,h,x,y,speed) 
		self.direction="up"
	def update(self):
		self.rect.y+=self.speed
		if self.rect.y+self.h>win_height:
			self.rect.x=0
			self.rect.x = randint(0 , win_width-self.w)
 
Rocket = Player(img="rocket.png",w=50,h=50,x=100,y=440,speed=5)
enemys = sprite.Group()
for i in range(5):
	enemy = UFO(img="ufo.png",w=100,h=50,x=0,y=10,speed=1)
	enemys.add(enemy)

clock = time.Clock()
FPS = 60



while True:
	window.blit(ground,(0,0))
	enemys.draw(window)
	enemys.update()
	Rocket.reset()
	Rocket.update()
	enemy.reset()
	enemy.update()
	display.update()
	for i in event.get(): 
		if i.type==QUIT:
			quit()
	clock.tick(FPS)
