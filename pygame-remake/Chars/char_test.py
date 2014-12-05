import pyTreeBee,pygame,sys,os,time, pygame.mixer, copy
import cPickle as pickle
from pygame.locals import*
infoObject = pygame.display.Info()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((infoObject.current_w//2)-400, (infoObject.current_h//2)-300)
temporarydisplay=pygame.display.set_mode((800,600))

class charSprite(object):
    def __init__(self,spritesheet,spritesize,stepnextsprite,rewind,pos=(0,0)):
        self.sheet=spritesheet
        self.size=spritesize
        self.x_sheet=0
        self.y_sheet=0
        self.x=pos[0]
        self.y=pos[1]
        self.step=stepnextsprite
        self.rewind=rewind
        self.next=1
        self.pause_time=0
        self.repeats=0
        self.stop=False
        self.wait=False
        self.invert=[False,False]
        self.frame=0
    def setPause(self,pause):
        self.pause_time=pause
    def setStop(self,repeats):
        self.repeats=repeats
    def setLine(self, line):
        if line>=0 and line<int(self.sheet.get_height()/self.size[1]): self.y_sheet=line
    def getNextImage(self):
        self.frame+=1
        if self.wait and self.frame%(self.pause_time+self.step)==0:
            self.wait=False
            if self.x_sheet==int(self.sheet.get_width()/self.size[0])-1: self.x_sheet-=1
            if self.rewind: self.x_sheet+=1
        if self.frame%self.step==0 and self.stop==False and self.wait==False:
            if int(((self.x_sheet+1)*self.size[0])/self.sheet.get_width())>=1 or (self.x_sheet+1)<=(-self.next+1)/2:
                if self.rewind:
                    self.next=(-1)
                    self.x_sheet=int(self.sheet.get_width()/self.size[0])-2
                    self.rewind=False
                else:
                    self.x_sheet=(-self.next+1)/2
                    if self.next==(-1):
                        self.next=1
                        self.rewind=True
                        
                if self.repeats>0:
                    self.repeats-=(-self.next+1)/2
                    if self.repeats==0:
                        self.stop=True
                        self.x_sheet=int(self.sheet.get_width()/self.size[0])-1
                if self.pause_time>0:
                    self.wait=True
                    if self.next==-1:self.x_sheet=int(self.sheet.get_width()/self.size[0])-1
                    if self.rewind:self.x_sheet=(-self.next+1)/2
            else:
                self.x_sheet+=self.next
        return pygame.transform.flip(self.sheet.subsurface((self.x_sheet*self.size[0],self.y_sheet*self.size[1]),self.size),self.invert[0],self.invert[1])
    def blitOn(self,screen):
        screen.blit(self.getNextImage(),(self.x,self.y))

class personagem(object):
    def __init__(self,char_sprite,speed):
        self.char=char_sprite
        self.up=False
        self.down=False
        self.right=False
        self.left=False
        self.speed=speed
    def keyControls(self,event):
        if event.type==KEYUP:
            if event.key==K_UP:    self.up=False
            if event.key==K_DOWN:  self.down=False
            if event.key==K_RIGHT: self.right=False
            if event.key==K_LEFT:  self.left=False
        if event.type==KEYDOWN:
            if event.key==K_UP:    self.up=True
            if event.key==K_DOWN:  self.down=True
            if event.key==K_RIGHT: self.right=True
            if event.key==K_LEFT:  self.left=True
        return False
    def blitOn(self,scr):
        if self.up:
            self.char.setLine(2)
            self.char.y-=self.speed
        elif self.down:
            self.char.setLine(1)
            self.char.y+=self.speed
        elif self.right:
            self.char.invert=[False,False]
            self.char.setLine(0)
            self.char.x+=self.speed
        elif self.left:
            self.char.invert=[True,False]
            self.char.setLine(0)
            self.char.x-=self.speed
        if self.up or self.down or self.right or self.left:
            self.char.stop=False
        else:
            self.char.x_sheet=1
            self.char.stop=True
        self.char.blitOn(scr)

class mapa(object):
    def __init__(self):
        self.tile1=pygame.image.load("trapezios.png").convert()
        self.tile2=pygame.image.load("ladrilho.png").convert()
    def blitOn(self,scr):
        for x in range(20):
            for y in range(4):
                scr.blit(self.tile1,(x*40,y*40))
                scr.blit(self.tile2,((x*40),(y*40)+(4*40)))
                scr.blit(self.tile2,((x*40),(y*40)+(8*40)))
                scr.blit(self.tile1,((x*40),(y*40)+(12*40)))
        

teste_sprite=charSprite(pygame.image.load("headbanger.png").convert_alpha(),(40,60),9,True,(100,100))
teste_sprite.setLine(0)
teste_sprite=personagem(teste_sprite,2)
tela=pyTreeBee.dynamicScreen((800,600),60,(255,255,255),mapa(),teste_sprite)
pyTreeBee.treeBeeStart(tela)
pygame.quit()

