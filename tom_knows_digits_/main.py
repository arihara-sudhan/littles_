import pygame
import numpy
import cv2
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import sys

w,h = 1600,900
white = (255,255,255)

class TomCounts_ARI:
	def __init__(self):
		pygame.mixer.init()
		pygame.init()
		pygame.font.init()
		self.det = None
		self.list = []
		self.font = pygame.font.Font("assets_/fonts_/quake.TTF", 80)
		self.count = 0
		self.width = 1920
		self.height = 1080
		self.disp = pygame.display.set_mode((self.width,self.height),0,0)
		pygame.display.set_caption("MNIST Tom")
		self.img = pygame.image.load("assets_/images_/0001.jpg")
		self.img = pygame.transform.scale(self.img,(w+120,h+160))
		test_set = datasets.MNIST('data_', train=False, download=True, transform=transforms.ToTensor())
		self.test_loader = DataLoader(test_set, batch_size=32, shuffle=True)
		self.CAPTURE_ALL()

	def blitForever(self,val=None):
		if(val!=None):
			if(val not in self.list):
				self.list = []
				self.list.append(val)
				self.playAudioARI(val)
		else:
			self.disp.blit(self.img,(560,0,0,0))
		self.disp.blit(self.imgframe,(0,0,0,0))
		text1 = self.font.render("TOM DETECTED "+str(self.det), True, white)
		text1Rect = text1.get_rect()
		text1Rect.center = (w//2,h)
		self.blittext()
		pygame.display.update()

	def blittext(self):
		text1 = self.font.render("TOM DETECTED "+str(self.det), True, white)
		text1Rect = text1.get_rect()
		text1Rect.center = (w//2+600,h+40)
		self.disp.blit(text1,text1Rect)
 
	def playAudioARI(self,op):
		i = 1
		self.det = op[9]
		pygame.mixer.music.load(op)
		pygame.mixer.music.play()
		while(True):
			img = pygame.image.load("assets_/images_/0"+str(i).zfill(3)+".jpg")
			img = pygame.transform.scale(img,(w+120,h+160))
			self.disp.blit(img,(560,0,0,0))
			i+=1
			if(i==10):
				return
			self.disp.blit(self.imgframe,(0,0,0,0))
			self.blittext()
			pygame.display.update()

	def CAPTURE_ALL(self):
		model = torch.load('models_/mnist.pt')
		correct = 0 ; total = 0
		with torch.no_grad():
			for data in self.test_loader:
				x, y = data
				output = model(x.view(-1, 784))
				for idx, i in enumerate(output):
					if torch.argmax(i) == y[idx]:
						correct +=1
					total +=1
		print(f'Accuracy: {round(correct/total, 3)}')
		th=0
		while True:
			digit = int(torch.argmax(model(x[th].view(-1, 784))[0]))
			frame = numpy.array(transforms.ToPILImage()(x[th]).convert("RGB"))[:, :, ::-1].copy()
			frame = cv2.resize(frame,(w//2+50+50,h+50+80))
			cv2.imwrite('data_/imgframe.jpg',frame)
			self.imgframe = pygame.image.load("data_/imgframe.jpg")
			self.blitForever(f'assets_/audio_/{digit}.mp3')
			self.blitForever()
			for	eve in pygame.event.get():
				if eve.type==pygame.KEYDOWN:
					if eve.key==pygame.K_RIGHT and th<15:
						th+=1
					elif eve.key==pygame.K_LEFT and th>0:
						th-=1
					elif eve.key==pygame.K_ESCAPE:
						sys.exit()

TomCounts_ARI()
