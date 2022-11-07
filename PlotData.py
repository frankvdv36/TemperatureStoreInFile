# https://stackoverflow.com/questions/20928892/python-numpy-array-reading-from-text-file-to-2d-array

# Dit programma werkt los van de SD18B20 verie 11bis
# Leest de fil data.txt in en maakt die klaar voor PLOT
# Converter file to array
# berekening doen op ieder element
# maar er een list van
# PLOT 4 lijnen

# Als test wordt file 11bis.txt gebruikt

# berekent de 4 y-assen en de x-as.
# De lengte van de tabel is = aantal lijnen inde tabel

# https://stackoverflow.com/questions/70828615/converting-data-file-into-numpy-arrays0

# Programma neemt data_11bis en convert naar 2Darray WERKT
# Resultaat is een float
# werkt met variabel file name

import time
import numpy as np
import matplotlib.pyplot as plt
# to install; open LX terminal, cd Desktop, pip install matplotlib    # DOE DIT EERST

path = '/home/pi/Python3/GUI_plot/'
np.set_printoptions(formatter={'float': '{: 0.1f}'.format})     # formaat van printen

# START ----------------------------------------------------------------

# INPUT file name
#fname = int(input("Datum file (YYMMDD): "))    # # gebruik als er cijfers zijn (int)
fname = str(input("Datum file (YYMMDD): "))     # gebruik als er letters/cijfers zijn (str)

# Input check
try:
    #fname = open("/home/pi/Python3/GUI_plot/data_11bis.txt", "r")
    #fname = open("data_11bis.txt", "r")
    fname = open(path+fname+".txt", "r")    # path + fila name
except:
    print ('File bestaat niet, probeer opnieuw')    # https://maschituts.com/how-to-restart-a-program-in-python-explained/
    time.sleep(2)
    quit()

# Maak array van ieder element    
data =[]
for line in fname.readlines():
    data.append(np.fromstring(line,sep=','))
data_array = np.array(data)
#x = data_array[:,0:4]         # 2Darray  
x = data_array[:,2]         # 1Darray
y1 = data_array[:,3]           # 1Darray        ROOD
y2 = data_array[:,4]           # 1Darray        BLAUW
y3 = data_array[:,5]           # 1Darray        GEEL
y4 = data_array[:,6]           # 1Darray        GROEN

# Bepaal lengte lijst voor x-as
lengte = 0
for i in x:
 
    # incrementing counter
    lengte = lengte + 1
print("Lengte van de tabel: " + str(lengte))

# Maak van de array een list
X = x.tolist()              # array to list
Y1 = y1.tolist()              # array to list   ROOD
Y2 = y2.tolist()              # array to list   BLAUW
Y3 = y3.tolist()              # array to list   GEEL
Y4 = y4.tolist()              # array to list   GROEN

#print ('X= ',X); print ('Y1= ',Y1); print('Y2= ',Y2); print ('Y3= ',Y3); print('Y4= ',Y4)
  
# PLOT -----------------------------------------------------------------

# https://www.geeksforgeeks.org/simple-plot-in-python-using-matplotlib/
# to install; open LX terminal, cd Desktop, pip install matplotlib

plt.plot(Y1,'r')
plt.plot(Y2, "b")     # bepaal kleur r, g, or, y, b
plt.plot(Y3, "y")     # bepaal kleur r, g, or, y, b
plt.plot(Y4, 'g')         # idem           # 4th is 4de lijn
  
# naming the x-axis
plt.xlabel('tijd/5min.')              # tekst x-as
  
# naming the y-axis
plt.ylabel('Temp °C')                 # tekst y-as
  
# get current axes command
ax = plt.gca()
  
# get command over the individual
# boundary line of the graph body
ax.spines['right'].set_visible(False)   # geen kader rond grafiek
ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(True)   # wel kader rond grafiek
#ax.spines['top'].set_visible(True)
  
# set the range or the bounds of 
# the left boundary line to fixed range
ax.spines['left'].set_bounds(-10, 55)    # lengte lijn y-as
  
# set the interval by  which 
# the x-axis set the marks
plt.xticks(list(range(0, lengte+1, 12)))         # X-as van -3 tot 9 (laatste element niet)
  
# set the intervals by which y-axis
# set the marks
plt.yticks(list(range(-10, 60, 5)))      # Y-as van -3 tot 18 (laatste element niet)
  
# legend denotes that what color 
# signifies what
ax.legend(['tempH out', 'tempL in', 'tempB buiten', 'tempD H-L'])   # legende in minikader naast grafiek
  
# annotate command helps to write
# ON THE GRAPH any text xy denotes 
# the position on the graph
plt.annotate('IEDERE STREEPJE = 1 UUR', xy = (70, -9))  # tekst boven x-as extra uitleg + coordinaten (1.01, -2.15)
  
# gives a title to the Graph
plt.title('CV temperatuur verloop')             # titel bovenaan
  
plt.show()

# END ==================================================================


