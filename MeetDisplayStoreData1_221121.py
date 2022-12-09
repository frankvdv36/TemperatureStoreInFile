# Multi SD18B20 
# https://community.element14.com/products/raspberry-pi/raspberrypi_projects/b/blog/posts/multiple-ds18b20-temp-sensors-interfacing-with-raspberry-pi
# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
# SPDX-License-Identifier: MIT
# https://www.tutorialspoint.com/python3/time_strftime.htm		ALEGMENE INFO
# https://www.geeksforgeeks.org/get-current-date-using-python/
# https://github.com/wahajmurtaza/Pygame_Percent_Gauge/blob/main/percentage_gauge.py
# https://www.pygame.org/docs/ref/gfxdraw.html
# https://www.w3schools.com/colors/default.asp 
# /usr/local/lib/python3/ is het pad waar de Modules te vinden zijn 
# Dit programma toont 4 wijzers met tijd en datum in het midden. Variabelen zijn: datum tijd now tempH, tempL, tempB, tempH-L
# Sensoren + display worden uitgevraagd iedere 15sec, datafile iedere 300sec.
# File: start.py = CVfileMakerGauges11.py
# File aangepast naar tijd HHMMSS en datum YYMMDD = CVfileMakerGauges11bis.py
# Iedere dag een file met file name 'datum'.txt vb 221104.txt = CVfileMakerGauges12.py >>> MeetDisplayStoreData.py
# Temperatuur BUITEN -1.5°C gezet. Regel 383

import os                           # Temperatuur deel
import glob                         # Temp deel
import time                         # Temp deel
from datetime import datetime       # Datum en tijd voor in datafile
from datetime import date           # Datum voor in datafile
import pygame                       # Gauges
import pygame.gfxdraw               # Gauges
import math                         # Gauges
from time import gmtime, strftime   # dashboard

#-----------------------------------------------------------------------
# Dashboard

circle_c = (150, 150, 150)              # background color circle
bg_c = (70, 70, 70)                     # background color
width, height = (1680, 990)             # window afmetingen 1680x990 vol

lavender= (255, 240, 245)
darkblue= ( 0, 0, 139)
sladegray= (112, 128, 144)
palegreen= (152, 251, 152)
Tomato= (255, 99, 71)
lightblue= (173, 216, 230)
navajowhite= (255, 222, 173)
coral= (255, 127, 80)

titel= 'Dashboard'                    # txt bovenrand          
#txtcenter = 'Dashboard'               # txt center beeld, staat bij Linksboven
txt = [255, 222, 173]                   # Txt midden voor tijd en datum
x1 =  650       # X positie txt midden 
y1 =  475       # y positie txt midden

percentage = 5      # groter dan 4 is boog opvullen, dus gebeurt nu direct

# Declair variabelen
now =0      # tijd en datum in 1 getal. Gebruikt om wachtlussen te sturen.
tempH = 40   # temp Hoog
tempL = 40    # temp Laag  
tempB = 10    # temp Buiten
tempD = 0    # verschil Hoog en Laag

#=======================================================================

# Alles voor sensoren uitlezen en datafile schrijven

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TEMPERATUREN OPHALEN

# These lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'

# Get all the filenames begin with 28 in the path base_dir.
device_folder = glob.glob(base_dir + '28*')[0]
device_folder1 = glob.glob(base_dir + '28*')[1]
device_folder2 = glob.glob(base_dir + '28*')[2]

# print alle adressen van de sensoren
print (device_folder)
print (device_folder1)
print (device_folder2)


device_file = device_folder + '/w1_slave'
device_file1 = device_folder1 + '/w1_slave'
device_file2 = device_folder2 + '/w1_slave'

#reading temperature from folder
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    #print('raw_f',lines)
    f.close()
    return lines

def read_temp_raw1():
    g = open(device_file1, 'r')
    lines1 = g.readlines()
    #print('raw_g',lines1)
    g.close()
    return lines1

def read_temp_raw2():
    h = open(device_file2, 'r')
    lines2 = h.readlines()
    #print('raw_h',lines2)
    h.close()
    return lines2

#converting the temperature data to human readable form

def read_temp():
    lines = read_temp_raw()                 # lees temperatuur raw
    while lines[1].strip()[-3:] != 'YES':
        lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

def read_temp1():
    lines1 = read_temp_raw1()
    while lines1[1].strip()[-3:] != 'YES':
        lines1 = read_temp_raw1()
        equals_pos1 = lines1[1].find('t=')
        temp_string1 = lines1[1][equals_pos1 +2:]
        temp_c1 = float(temp_string1) / 1000.0
        #temp_f1 = temp_c1 * 9.0 / 5.0 + 32.0
        return temp_c1

def read_temp2():
    lines2 = read_temp_raw2()
    while lines2[1].strip()[-3:] != 'YES':
        lines2 = read_temp_raw2()
        equals_pos2 = lines2[1].find('t=')
        temp_string2 = lines2[1][equals_pos2 +2:]
        temp_c2 = float(temp_string2) / 1000.0
        #temp_f2 = temp_c2 * 9.0 / 5.0 + 32.0
        return temp_c2

#-----------------------------------------------------------------------
# TIJD en DATUM OPHALEN

def read_timedate():
    
    tijd = strftime("%H%M%S")                   #   180021 
    datum = strftime("%y%m%d")					 #   220926
    return datum, tijd                      # keer terug met 2 gegevens

#-----------------------------------------------------------------------
# SCHRIJF STRING NOP SD-KAART

def write_file(filedata): # schrijf de meegegeven data op SD kaart
    
    fo = open("/home/pi/Python3/SD18B20/"+datum+".txt", "a") # open file volgens pad, indien onbestaand maak aan
    fo.write (filedata) # Er wordt geschreven in opgegeven pad en voeg nieuwe data toe
    fo.close()          # Close opend file

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------------------------------------------------------------
# Alles voor dashboard

class Gauge:
    def __init__(self, screen, FONT, x_cord, y_cord, thickness, radius, circle_colour, glow=True):
        self.screen = screen
        self.Font = FONT
        self.font = pygame.font.SysFont('Arial', 50) # extra text boog
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.thickness = thickness
        self.radius = radius
        self.circle_colour = circle_colour
        self.glow = glow
                
#-----------------------------------------------------------------------
# Links boven Temp Hoog

    def draw1(self, percent): 
            

        acc1 = [255, 99, 71]    # kleur boog 
        ac1 = [255, 99, 71] # kleur txt center boog 
        txt1 = [255,255,255] # kleur txt                                     
        fill_angle = int((tempH+2)*270/80)       # hoek 270° per % +2 = offset boog midden 
        if fill_angle >= 270:
            fill_angle = 280                     # boog 100% opvullen
        if fill_angle <=10:                             
            fill_angle =10                        # boog 2.7% opvullen
        '''    
        if fill_angle >=0 and fill_angle <=68:    # tussen -20 en 0 Blauw (regel van drie met 270°)
            acc1 = [173, 216, 230]
        if fill_angle >= 68 and fill_angle <155: # tussen 0 en 25 groen
            acc1 = [0,250,0]  
        if fill_angle >= 155 and fill_angle <= 280:# boven 25 Rood             
            acc1 = [255,0,0]                       # kleur boog    
        '''    
        pertext = self.Font.render(str(tempH) + "°C", True, ac1)  # °C of % of hpa                                      # Temperatuur in °C
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(self.Font.render(time.strftime("%d-%m | %H:%M"), True, txt), (x1,y1))                          # Txt midden in beeld   Local time Date ********
        self.screen.blit(self.font.render('Temp Hoog    ', True, txt1), (int(self.x_cord/1.5), int(self.y_cord*1.7)))     # TEXT bij boog = OK
        self.screen.blit(self.font.render('0', True, acc1), (int(self.x_cord*0.7), int(self.y_cord*1.4)))             # cijfer begin boog
        self.screen.blit(self.font.render('80', True, acc1), (int(self.x_cord*1.15), int(self.y_cord*1.4)))             # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)
        
        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog maar lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc1) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return
#-----------------------------------------------------------------------
# Rechts boven Temp Laag

    def draw2(self, percent):
        
        acc2 = [0,255,250]    # kleur boog 
        ac2 = [0,255,255] # kleur txt center boog 
        txt2= [255,255,255] # kleur txt 
            
        fill_angle = int((tempL+2)*270/80)       # hoek 270° per % +2 = offset boog midden 
        if fill_angle >= 270:    #
            fill_angle = 280
        if fill_angle <=10:
            fill_angle=10
      
        pertext = self.Font.render(str(tempL) + "°C", True, ac2)  # °C 
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(self.font.render('Temp Laag', True, txt2), (int(self.x_cord/1.1), int(self.y_cord*1.7)))       # TEXT bij boog = OK
        self.screen.blit(self.font.render('0', True, ac2), (int(self.x_cord*0.9), int(self.y_cord*1.4)))              # cijfer begin boog
        self.screen.blit(self.font.render('80', True, ac2), (int(self.x_cord*1.05), int(self.y_cord*1.4)))              # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)

        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog maar lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc2) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return
#-----------------------------------------------------------------------
# Links onder Temp Buiten

    def draw3(self, percent):
   
        acc3 = [250,250,0]    # kleur boog indien geen voorwaarden waarbij kleuren veranderen
        ac3 = [255,255,0] # kleur txt center boog 
        txt3 = [255,255,255] # kleur txt        
        fill_angle = int((tempB+22)*270/60)       # hoek per % +2 = offset boog midden
        if fill_angle >= 270:
            fill_angle = 280                     # boog 100% opvullen
        if fill_angle <=10:                             
            fill_angle=10                        # boog 2.7% opvullen
        
        pertext = self.Font.render(str(tempB) + "°C", True, ac3)
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(self.font.render('Temp Buiten', True, txt3), (int(self.x_cord/1.5), int(self.y_cord*1.22)))       # TEXT bij boog = OK
        self.screen.blit(self.font.render('-20', True, ac3), (int(self.x_cord*0.7), int(self.y_cord*1.14)))              # cijfer begin boog
        self.screen.blit(self.font.render('40', True, ac3), (int(self.x_cord*1.15), int(self.y_cord*1.14)))              # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)

        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog maar lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc3) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return
#-----------------------------------------------------------------------
# Rechts onder Temp H-L

    def draw4(self, percent):
            
        acc4 = [152, 251, 152]    # kleur boog 
        ac4 = [152, 251, 152] # kleur txt center boog 
        txt4 = [255,255,255] # kleur txt wit   
        tempD = tempH - tempL 
        fill_angle = int((tempD+27)*270/50)       # hoek per 50%  vb (270* 1000/500) # 25° + 2 offset zodat 0°C midden is
        
        if fill_angle >= 270:
            fill_angle = 280                       # boog 100% opvullen
        if fill_angle <=10:                             
            fill_angle=10                          # boog 2.7% opvullen 
        '''    
        if fill_angle >=0 and fill_angle <81:      # tussen 500 en 800 Palegreen           Rekenvoorbeeld   (800-500)*270/1000°= 081
            acc4 = [152, 251, 152]      
        if fill_angle >=81 and fill_angle <135:    # tussen 800 en 1000 Coral oranje       Rekenvoorbeeld   (1000-500)*270/1000°= 135
            acc4 = [255, 127, 80]
        if fill_angle >= 135 and fill_angle <=280: # tussen 1000 en 1500 Rood
            acc4 = [255,0,0]  
        '''    
        pertext = self.Font.render(str(round(tempD,1)) + "°C", True, ac4)  # °C 
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(self.font.render('Temp H-L', True, txt4), (int(self.x_cord/1.09), int(self.y_cord*1.22)))       # TEXT bij boog = OK
        self.screen.blit(self.font.render('-25', True, ac4), (int(self.x_cord*0.9), int(self.y_cord*1.14)))              # cijfer begin boog
        self.screen.blit(self.font.render('25', True, ac4), (int(self.x_cord*1.05), int(self.y_cord*1.14)))              # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)

        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog met lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc4) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return                        
        
#-----------------------------------------------------------------------

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(titel) # Tekst boven

    fps = 0.2    # snelheid refresh screen nu op 5s
    FONT = pygame.font.SysFont('Franklin Gothic Heavy', 100) # size tekens value
#-----------------------------------------------------------------------
    my_gauge1 = Gauge(       # Links boven
        screen=screen,
        FONT=FONT,
        x_cord=width / 4,   # plaats gauges x
        y_cord=height / 4,  # plaats gauges y
        thickness= 40,   # dikte boog was 50
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
#-----------------------------------------------------------------------
    my_gauge2 = Gauge(          # Rechts boven
        screen=screen,
        FONT=FONT,
        x_cord=width / 1.3,   # plaats gauges x
        y_cord=height / 4,  # plaats gauges y
        thickness= 40,   # dikte boog
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
#-----------------------------------------------------------------------
    my_gauge3 = Gauge(          # Links onder 
        screen=screen,
        FONT=FONT,
        x_cord=width / 4,   # plaats gauges x
        y_cord=height / 1.3,  # plaats gauges y
        thickness= 40,   # dikte boog
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
#-----------------------------------------------------------------------
    my_gauge4 = Gauge(          # Rechts onder
        screen=screen,
        FONT=FONT,
        x_cord=width / 1.3,   # plaats gauges x
        y_cord=height / 1.3,  # plaats gauges y
        thickness= 40,   # dikte boog
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------------------------------------------------------------
#-----------------------------------------------------------------------

#percentage = 5      # groter dan 4 is boog opvullen, dus gebeurt nu direct
#now = round (time.time())   # maak een geheel getal in sec.
nowOld = 0
while True:     # Routine voor sensoren SD18B20 + Datafile invullen
    
    # Start: opvragen datum en tijd voor datafile
    
    nu = read_timedate()        # haal tijd en datum op # nu bevat 2 gegevens
    datum = (nu[0])             # ken datum toe
    tijd = (nu[1])              # ken tijd toe
    
    # Tijd in één getal voor wachtlussen
    
    now = round (time.time())   # GETAL sedert 1970, maak een geheel getal in sec.
    
    #print (now)
  
    # Start: opvragen temperaturen 
    try:
        temp = read_temp()       
        temp1 = read_temp1() 
        temp2 = read_temp2() 
        datumtijd = read_timedate()
        tempB = temp -1.5          # Correctie volgens buitenthermostaat CV
        tempB = round (tempB,1)      # Sensor met gele band ..5A8F
        tempH = round (temp1,1)     # Sensor met rode band ..B8D6
        tempL = round (temp2,1)     # Sensor met blauwe band ..ABF4
        
        print ('\n', 'Temp Hoog Rood= ', tempH, '°C\n', 'Temp Laag Blauw= ', tempL, '°C\n', 'Temp Buiten Geel= ', tempB, '°C\n', 'Time= ',now, '\n')
    except:
        tempH = 0    
        tempL = 0
        tempB = 0 
        # restart programma???
        print ('sensors konden niet uigevraagd worden')
                
    # Display op dashboard update iedere 15sec.
       
    screen.fill(bg_c)                     # zonder deze lijn wordt steeds overelkaar geprojecteerd
    my_gauge1.draw1(percent=percentage)   # toon beeld gauge1
    my_gauge2.draw2(percent=percentage)   # toon beeld gauge2
    my_gauge3.draw3(percent=percentage)   # toon beeld gauge3
    tempD = tempH - tempL                 # bereken verschil
    tempD = round (tempD, 1)
    my_gauge4.draw4(percent=percentage)   # toon beeld gauge4
    pygame.display.update()               # toont beeld
    clock.tick(fps)
    time.sleep(9)                         # wacht tot ongeveer 15sec. Uitlezen + display duurt ongeveer 6sec.
         
    # Maak string volgens format-methode https://stackoverflow.com/questions/19457227/how-to-print-like-printf-in-python3
    # Voorbeeld # data = "{0}, {1}".format(datum, tijd)   # maak string volgens formaat = voorbeeld
    if now >= nowOld + 300:               # Deze lus wordt iedere 300s doorlopen ivm datafile
        filedata = "{0}, {1}, {2}, {3}, {4}, {5}, {6} \n".format(datum, tijd, now, tempH, tempL, tempB, tempD)
        #filedata = "{0}, {1}, {2}, {3}, {4}, {5}, {6} \n".format([datum, tijd, now, tempH, tempL, tempB, tempD])
        print ('filedata= ',filedata)         # laat data zien
        # schrijf filedata op SD kaart
        write_file(filedata)              # geef data mee tussen haakjes
        nowOld = now      
        
#=======================================================================

