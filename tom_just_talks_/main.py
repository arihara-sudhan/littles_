import pyaudio
import wave
from playsound import playsound
import pygame
import sys
import time

w,h = 1600,900
white = (255,255,255)

class TomTalks:
	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.font = pygame.font.Font("assets_/fonts_/quake.TTF", 35)
		self.name = -1
		self.op = "assets_/audio_/voice0.wav"
		self.tomImg = pygame.image.load("assets_/images_/tomImg.png")
		self.width = 1920
		self.height = 1080
		self.disp = pygame.display.set_mode((self.width,self.height),0,0)
		self.img_back = pygame.image.load("assets_/images_/intro.jpg")
		self.img_back = pygame.transform.scale(self.img_back,(w-150,h-100))
		self.blitARI()

	def blitARI(self):
		x = 100
		y = 120
		xc = 1
		while True:
			if(xc):
				x+=2
			self.disp.blit(self.img_back,(200,120))
			self.disp.blit(self.tomImg,(x,y))
			pygame.display.update()
			if(x>250):
				xc = 0
			for Eveu in pygame.event.get():
				if Eveu.type == pygame.KEYDOWN:
					if Eveu.key == pygame.K_RETURN and xc==0:
						self.blitTomARI()
					if Eveu.key == pygame.K_ESCAPE:
						pygame.display.quit()
						sys.exit()
	def blitTomARI(self):
		i = 1
		while(True):
			for Eve in pygame.event.get():
				if Eve.type == pygame.KEYDOWN:
					if Eve.key == pygame.K_RETURN:
						self.recordAudioARI()
					if Eve.key == pygame.K_ESCAPE:
						pygame.display.quit()
						sys.exit()
			img = pygame.image.load("assets_/images_/000"+str(i)+".jpg")
			img = pygame.transform.scale(img,(w-50,h-100))
			self.disp.blit(img,(200,150))
			time.sleep(0.09)
			i+=1
			if(i==8):
				i=1
			pygame.display.update()


	def recordAudioARI(self):
		text1 = self.font.render('LISTENING...', True, white)
		text1Rect = text1.get_rect()
		text1Rect.center = (450, 880)
		self.disp.blit(text1,text1Rect)
		pygame.display.update()
		self.p = pyaudio.PyAudio()
		self.chunk = 1024
		self.format = pyaudio.paInt24
		self.channels = 2
		self.rate = 128000
		self.secs = 4
		self.stream = self.p.open(format=self.format,
                channels=self.channels,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk)
		self.frames = []
		for i in range(0,int(self.rate/self.chunk*self.secs)):
			self.frames.append(self.stream.read(self.chunk))
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()
		self.saveAudioARI(self.op)

	def saveAudioARI(self,op):
		self.name+=1
		op = "assets_/audio_/voice"+str(self.name)+".wav"
		self.wf = wave.open(op, 'wb')
		self.wf.setnchannels(self.channels)
		self.wf.setsampwidth(self.p.get_sample_size(self.format))
		self.wf.setframerate(self.rate)
		self.wf.writeframes(b''.join(self.frames))
		self.wf.close()
		self.playAudioARI(op)

	def playAudioARI(self,op):
		text1 = self.font.render('SPEAKING...', True, white)
		text1Rect = text1.get_rect()
		text1Rect.center = (450, 880)
		i = 1
		playsound(op,False)
		tT = time.time()
		while(True):
			for Eve in pygame.event.get():
				if Eve.type == pygame.KEYDOWN:
					if Eve.key == pygame.K_ESCAPE:
						pygame.display.quit()
						sys.exit()
			img = pygame.image.load("assets_/images_/0"+str(i).zfill(3)+".jpg")
			img = pygame.transform.scale(img,(w-50,h-100))
			self.disp.blit(img,(200,150))
			self.disp.blit(text1,text1Rect)
			time.sleep(0.09)
			i+=1
			if(i==49):
				i=3
			if(time.time()-tT>4):
				self.blitTomARI()
			pygame.display.update()
t = TomTalks()
