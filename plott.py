import matplotlib.pyplot as mplot
import numpy             as npy


bdepth    = 8
vref      = 3.3
n_markers = 100

# getting info from here

settings = npy.loadtxt( "/home/b01-103/Desktop/Scripts/settings.txt", dtype = float )
d_data   = npy.loadtxt( "/home/b01-103/Desktop/Scripts/data.txt"    , dtype = int   ) # digital data (0-255)

#work with the data

samplerate   = settings[0]
quantization = settings[1]
size         = d_data.size / 5
a_data       = d_data / ( 2 ** bdepth ) * vref # analog data (0V - Vref V)
period       = 1 / samplerate
maxtime      = period * d_data.size *0.001
datatime     = npy.linspace( 0, maxtime , num = d_data.size )
chargetime   = d_data.argmax() * period *0.001
unchargetime = (max( datatime ) - chargetime)

# the graph part

fig, ax = mplot.subplots( figsize = (16, 10), dpi = 200 ) # layout = "constrained"
ax.set_title( "Процесс зарядки-разрядки конденсатора", wrap = True )
ax.set_xlabel( "t, s" )
ax.set_ylabel( "U, V" )
ax.set_xlim( 0, maxtime )
ax.set_ylim( 0, max( a_data ) * 1.1 )
ax.text( chargetime + maxtime / 15, 0.8 * max( a_data ), f"Время заряда: {chargetime:.1f} с\n\nВремя разряда: {unchargetime:.1f} с", fontsize = 20, color = "blue" )
ax.minorticks_on()
ax.grid( True )
ax.grid( True, "minor", ls = ":" )
# ax.xaxis.set_major_locator( NullLocator )
markrate = int( size / n_markers )
ax.plot( datatime, a_data, marker = 'o', markersize = 5, markeredgecolor = "red", markevery = markrate, color = "blue", alpha = 1, linewidth = 0.2, linestyle = "--", label = "V=V(t)" )
ax.legend()
fig.savefig( "/home/b01-103/Desktop/Scripts/graph.png" )
fig.savefig( "/home/b01-103/Desktop/Scripts/graph.svg" )
# mplot.show()
