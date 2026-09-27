from pygame import *
from random import randint
font.init()
window=display.set_mode((700,500))
display.set_caption("shooter")
background=transform.scale(image.load('galaxy.jpg'),(700,500))

mixer.init()
mixer.music.load('space.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self,o_image,sprite_x,sprite_y,width,height,speed):
        super().__init__()
        self.speed=speed
        self.image=transform.scale(image.load(o_image),(width,height))
        self.rect=self.image.get_rect()
        self.rect.x=sprite_x
        self.rect.y=sprite_y
    
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_RIGHT] and self .rect.x <615:
            self.rect.x+=self.speed

        if keys_pressed[K_LEFT] and self .rect.x >0:
            self.rect.x-=self.speed
        
        


        

    def fire(self):
        global one 
   
        b=Bullet('Bullet.png',self.rect.centerx-6,self.rect.y,15,10,3)
        bullets.add(b)

        if sprite.spritecollide(player,bullettt,False) or one:
            
            a=Bullet('Bullet.png',self.rect.centerx-6,self.rect.y,15,10,3)
            bullets.add(a)
            a=Bullet('Bullet.png',self.rect.centerx+6,self.rect.y,15,10,3)
            bullets.add(a)
            one=True
            
            

        
one=False

class Enemy(GameSprite):
    
    def update(self):
        global missed
        self.rect.y+=self.speed
        if self.rect.y>500:
            missed+=1
            self.rect.y=-50
            self.rect.x=randint(0,620)


class double(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y>500:
            self.rect.y=-50
            self.rect.x=randint(0,620)


class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y<0:
            self.kill()




player=Player('rocket.png',200,390,80,100,5)   
bullets=sprite.Group()
bullettt=sprite.Group()
bullet2 = double('bullet.png',randint(0,620),-50,75,55,randint(1,2))
bullettt.add(bullet2)
monesters=sprite.Group()
for i in range(4):
    ee=Enemy('ufo.png',randint(0,620),-50,75,55,randint(1,2))
    monesters.add(ee)

clock=time.Clock()
run=True
finish=False

points=0
win=font.Font(None,66).render('YOU WIN!!',True,(255,255,255))
lose=font.Font(None,66).render('YOU LOSE!!',True,(55,155,5))
y=0
missed=0
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        elif e.type == KEYDOWN:
            if e.key== K_SPACE:
                player.fire()

    if not finish:
        
        y+=0.4
        if y>500:
            y=0

        window.blit(background,(0,y))
        window.blit(background,(0,y-500))
        collides=sprite.groupcollide(monesters,bullets,True,True)
        

        for c in collides:
            points+=1
            ee=Enemy('ufo.png',randint(0,620),-50,75,55,randint(1,2))
            monesters.add(ee)



        if points>=30:
            finish=True
            window.blit(win,(230,180))
        if missed>=20:
            finish=True
            window.blit(lose,(230,180))
        
        count=font.Font(None,36).render('count:'+str(points),True,(255,255,255))
        missed_label=font.Font(None,36).render('missed:'+str(missed),True,(255,255,255))
        player.draw()
        player.update()
        monesters.draw(window)
        monesters.update()
        bullets.draw(window)
        bullets.update()
        bullettt.draw(window)
        bullettt.update()
        window.blit(count,(10,10))
        window.blit(missed_label,(10,45))


    display.update()

    clock.tick(60)

    '''sprite.spritecollide(player,monesters,False)'''



























#//!
#//TODO
((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))