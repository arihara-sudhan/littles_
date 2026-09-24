from PIL import Image
import cv2 as cvari
import pygame as pgari
import sys
import time
from cvzone.HandTrackingModule import HandDetector as hdari
from pygame import mixer

white = ((255,255,255))

class ARI_DRIVES:

	def __init__(self):
		mixer.init()
		mixer.music.load('assets_/audio_/Race.mp3')
		mixer.music.play()
		pgari.font.init()
		self.font = pgari.font.Font("GOTHICB.ttf", 35)
		self.cam = cvari.VideoCapture(0)
		self.bk = pgari.display.set_mode((1920,1080))
		self.bg = pgari.image.load("assets_/images_/BG.jpg")
		self.bg = pgari.transform.scale(self.bg,(1920,1080))
		self.road = pgari.image.load("assets_/images_/ROAD.jpg")
		self.road = pgari.transform.scale(self.road,(680,800))
		self.car_red = pgari.image.load("assets_/images_/CARRE.png")
		self.car_red = pgari.transform.rotate(self.car_red,-90)
		self.car_red = pgari.transform.scale(self.car_red,(150,230))
		self.car_green = pgari.image.load("assets_/images_/CARG.png")
		self.car_green = pgari.transform.rotate(self.car_green,90)
		self.car_green1 = pgari.transform.scale(self.car_green,(120,210))
		self.car_green2 = pgari.transform.scale(self.car_green,(120,210))
		self.det = hdari(detectionCon=0.8,maxHands=1)
		self.show()

	def EXPLOMU(self):
		Clink1 = mixer.music.load('assets_/audio_/explosion.mp3')
		mixer.music.play()

	def GOVER(self,score):
		text1 = self.font.render('SCORE : '+str(score), True, white)
		text2 = self.font.render('ENTER TO START', True, white)
		text3 = self.font.render('ESC TO EXIT', True, white)
		text1Rect = text1.get_rect()
		text2Rect = text2.get_rect()
		text3Rect = text3.get_rect()
		text1Rect.center = (w // 2, h // 2-110)
		text2Rect.center = (w // 2, h // 2-70)
		text3Rect.center = (w // 2, h // 2-30)
		self.bk.blit(text1, text1Rect)
		self.bk.blit(text2, text2Rect)
		self.bk.blit(text3, text3Rect)

	def show(self):
		x = 400
		yt1 = -100
		yt2 = yt1-600
		carg1 = ()
		carg2 = ()
		while True:
			if yt1>1700:
				yt1 = -100
			yt2 = yt1-600
			yt1+=50
			c = 0
			for eve in pgari.event.get():
				if eve.type==pgari.KEYDOWN:
					if eve.key==pgari.K_ESCAPE:
						sys.exit()
			status,self.frame = self.cam.read()
			self.frame = cvari.resize(self.frame,(800,800))
			self.frame = cvari.flip(self.frame,1)
			hands,self.frame = self.det.findHands(self.frame,flipType=False)
			if hands:
				point = hands[0]['lmList'][8][0:2]
				print(point[0])
				if(point[0]<300):
					pass
				elif(point[0]>700):
					pass
				else:
					x = point[0]
			c+=1
	
			cvari.imwrite("frame%d.jpg" %c, self.frame)
			self.bk.blit(self.bg,(0,0))
			face = pgari.image.load("frame%d.jpg" %c)
			self.bk.blit(face,(900,150))
			self.bk.blit(self.road,(240,130))
			self.bk.blit(self.car_red,(x,680))
			if yt2 in range(600-80,630) and x in range(340-30,380+50):
				self.EXPLOMU()
				for x in range(20):
                    img = pgari.image.load("screenshots_/%dframe.png"%x)
					img = pgari.transform.scale(img,(500,500))
					img.set_colorkey("black")
					self.bk.blit(self.road,(240,130))
					self.bk.blit(self.car_red,(x,680))
					self.bk.blit(self.car_green1,(360,yt2))
					self.bk.blit(self.car_green2,(700,yt1))
					self.bk.blit(img,(x+100,680))
					pgari.display.update()
				for x in pgari.event.get():
					if x.type==pgari.KEYDOWN:
						if x.key==pgari.K_RETURN:
							ARI_DRIVES()
						if x.key==pgari.K_ESCAPE:
							sys.exit()
				time.sleep(2)
				sys.exit()

			if yt1 in range(600-80,630) and x in range(680-80,720+30):
				self.EXPLOMU()
				for x in range(20):
                    img = pgari.image.load("screenshots_/%dframe.png"%x)
					img = pgari.transform.scale(img,(500,500))
					img.set_colorkey("black")
					self.bk.blit(self.road,(240,130))
					self.bk.blit(self.car_red,(x,680))
					self.bk.blit(self.car_green1,(360,yt2))
					self.bk.blit(self.car_green2,(700,yt1))
					self.bk.blit(img,(x+500,550))
					pgari.display.update()
				time.sleep(2)
				sys.exit()
			self.bk.blit(self.car_green1,(360,yt2))
			self.bk.blit(self.car_green2,(700,yt1))
			pgari.display.update()

ARI_DRIVES()
