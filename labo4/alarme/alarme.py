import gpiozero as gp
from time import sleep
from .models import Zone

class MonSysteme:
    def __init__(self):
        #### Partie Alarm GPIOZERO
        self.sega = gp.LED(20)
        self.segb = gp.LED(21)
        self.segc = gp.LED(16)
        self.segd = gp.LED(26)
        self.sege = gp.LED(19)
        self.segf = gp.LED(13)
        self.segg = gp.LED(27)

        self.ma_led = gp.LED(18)

        self.btn = gp.Button(24)

        self.zone1 = gp.Button(22)
        self.zone2 = gp.Button(17)
        self.zone3 = gp.Button(4)
        self.zone4 = gp.Button(12)

        self.systemStatus = 0

    
        self.zone1.when_pressed = self.btnClick
        self.zone2.when_pressed = self.btnClick
        self.zone3.when_pressed = self.btnClick
        self.zone4.when_pressed = self.btnClick

        self.show0()

    def show0(self):
        # 0
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.on()

    def show1(self):
        #1
        self.sega.on()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.on()
        self.segg.on()


    def show2(self):
        #2
        self.sega.off()
        self.segb.off()
        self.segc.on()
        self.segd.off()
        self.sege.off()
        self.segf.on()
        self.segg.off()  
        

    def show3(self):
        #3
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.on()
        self.segf.on()
        self.segg.off() 


    def show4(self):
        #4
        self.sega.on()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.off()
        self.segg.off() 


    def show5(self):
        #5
        self.sega.off()
        self.segb.on()
        self.segc.off()
        self.segd.off()
        self.sege.on()
        self.segf.off()
        self.segg.off()  
    


    def show6(self):
        #6
        self.sega.off()
        self.segb.on()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.off() 


    def show7(self):
        #7
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.on()
        self.segg.on()     



    def show8(self):
        #8
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.off()  


    def show9(self):
        #9
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.off()
        self.segg.off()    



    def showA(self):
        #A
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.off()
        self.segf.off()
        self.segg.off()

    def cout_up(self):
        # 0
        self.show0()
        sleep(1)

        # 1
        self.show1()
        sleep(1)

        # 2
        self.show2()
        sleep(1)

        # 3
        self.show3()
        sleep(1)

        # 4
        self.show4()
        sleep(1)

        # 5
        self.show5()
        sleep(1)

        # 6
        self.show6()
        sleep(1)

        # 7
        self.show7()
        sleep(1)

        # 8
        self.show8()
        sleep(1)

        # 9
        self.show9()
        sleep(1)


    def cout_down(self):
        #9
        self.show9()    
        sleep(1)

        #8
        self.show8()  
        sleep(1)

        #7
        self.show7()   
        sleep(1)

        #6
        self.show6()  
        sleep(1)

        #5
        self.show5() 
        sleep(1)

        #4
        self.show4()  
        sleep(1)

        #3
        self.show3()    
        sleep(1)

        #2
        self.show2()  
        sleep(1)

        #1
        self.show1()    
        sleep(1)
        
        #0
        self.show0()
        sleep(1)

    def activer(self):
        if self.systemStatus == 0:
            self.cout_up()
            self.showA()
            self.ma_led.on()
            self.systemStatus = 1
        

    def desactiver(self):
        if self.systemStatus == 1:
            self.cout_down()
            self.show0()
            self.ma_led.off()
            self.systemStatus = 0

    def reinitialiser(self):
        if self.systemStatus == 1:
            self.showA()
            self.ma_led.on()
            self.systemStatus = 1
            zone1 = Zone.objects.get(titre='Zone 1')
            zone1.etat = 0
            zone1.save()
            zone2 = Zone.objects.get(titre='Zone 2')
            zone2.etat = 0
            zone2.save()
            zone3 = Zone.objects.get(titre='Zone 3')
            zone3.etat = 0
            zone3.save()
            zone4 = Zone.objects.get(titre='Zone 4')
            zone4.etat = 0
            zone4.save()
            


    def btnClick(self):
        if self.systemStatus == 1:
            if self.zone1.is_pressed:
                self.show1()
                self.ma_led.blink(on_time=0.4, off_time=0.4)
                zone1 = Zone.objects.get(titre='Zone 1')
                zone1.etat = 1
                zone1.save()
            elif self.zone2.is_pressed:
                self.show2()
                self.ma_led.blink(on_time=0.4, off_time=0.4)
                zone2 = Zone.objects.get(titre='Zone 2')
                zone2.etat = 1
                zone2.save()
            elif self.zone3.is_pressed:
                self.show3()
                self.ma_led.blink(on_time=0.4, off_time=0.4)
                zone3 = Zone.objects.get(titre='Zone 3')
                zone3.etat = 1
                zone3.save()
            elif self.zone4.is_pressed:
                self.show4()
                self.ma_led.blink(on_time=0.2, off_time=0.2)
                zone4 = Zone.objects.get(titre='Zone 4')
                zone4.etat = 1
                zone4.save()



alarme = MonSysteme()