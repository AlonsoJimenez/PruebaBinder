from IPython.display import HTML
from IPython.display import display

# Tomado de https://stackoverflow.com/questions/31517194/how-to-hide-one-specific-cell-input-or-output-in-ipython-notebook
tag = HTML('''<script>
code_show=false; 
function code_toggle() {
    if (code_show){
        $('div.cell.code_cell.rendered.selected div.input').hide();
    } else {
        $('div.cell.code_cell.rendered.selected div.input').show();
    }
    code_show = !code_show
} 

$( document ).ready(code_toggle);
</script>

Para mostrar/ocultar código presione <a href="javascript:code_toggle()">aquí</a>.''')


###########################################################################################################################


from ipywidgets import interactive
import ipywidgets as widgets
from IPython.display import display 
import numpy as np
import matplotlib.pyplot as plt


def CalculoVelocidad (arregloTiempo, velInicial, aceleración):
    velocidad = velInicial + aceleración * arregloTiempo
    return velocidad

def CalculoPosición (posInicial, arregloTiempo, velInicial, aceleración):
    posición = posInicial + velInicial * arregloTiempo + 1/2 * aceleración * arregloTiempo ** 2
    return posición


def Velocidad():
   
    display(tag)    
   

    def GraficoInteractivoVelocidad (velInicial, aceleración,tiempo):

      arregloTiempo = np.linspace (0, tiempo, 20)

      velocidadActual = CalculoVelocidad (arregloTiempo, velInicial, aceleración)

      fig, ax = plt.subplots (dpi=120)

      ax.set_xlabel('Tiempo $(s)$')
      ax.set_ylabel('Velocidad $(m/s)$')
      plt.xlim (0, 35)
      plt.ylim (-50, 50)
      ax.plot (arregloTiempo, velocidadActual)
      ax.set_title('Velocidad de una partícula en una dimensión')

      plt.grid ()

      plt.show()

      return

    velEtiqueta = widgets.Label (value="Velocidad Inicial $(m/s)$:")
    velSlider = widgets.IntSlider(min=-15.0, max=15.0, step=1.0, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.FloatSlider(min=-1, max=1, step=0.1, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=30, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=30,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoVelocidad, {'velInicial':velSlider, 
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)
    


###########################################################################################################################


def Posición():
    
    display(tag)

    def GraficoInteractivoPosición(posInicial, velInicial, aceleración,tiempo):

      arregloTiempo = np.linspace (0, tiempo, 20)

      posiciónActual = CalculoPosición (posInicial, arregloTiempo, velInicial, aceleración)

      fig, ax = plt.subplots (dpi=120)

      ax.set_xlabel('Tiempo $(s)$')
      ax.set_ylabel('Posición $(m)$')
      plt.xlim (0, 35)
      plt.ylim (-50, 50)
      ax.plot (arregloTiempo, posiciónActual)
      ax.set_title('Posición de una partícula en una dimensión')

      plt.grid ()

      plt.show()

      return


    posEtiqueta = widgets.Label (value="Posición Inicial $(m)$:")
    posSlider = widgets.IntSlider(min=-10.0, max=10.0, step=1.0, value=0.0)
    cajaPosición = widgets.HBox([posEtiqueta, posSlider])

    velEtiqueta = widgets.Label (value="Velocidad Inicial $(m/s)$:")
    velSlider = widgets.FloatSlider(min=-0.1, max=0.1, step=0.01, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.FloatSlider(min=-0.1, max=0.1, step=0.01, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=30, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=30,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoPosición, {'posInicial':posSlider,
                                                                  'velInicial':velSlider,
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaPosición, cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)


###########################################################################################################################


def Aceleración ():
    
    display(tag)
    
    def GraficoInteractivoPosición(posInicial, velInicial, aceleración,tiempo):
      arregloTiempo = np.linspace (0, tiempo, 20)
      aceleraciónActual = np.ones (20) * aceleración    

      fig, ax = plt.subplots (dpi=120)

      ax.set_xlabel('Tiempo $(s)$')
      ax.set_ylabel('Aceleración $(m/s^2)$')
      plt.xlim (0, 35)
      plt.ylim (-10, 10)
      ax.plot (arregloTiempo, aceleraciónActual)
      ax.set_title('Aceleración de una partícula en una dimensión')

      plt.grid ()

      plt.show()

      return


    posEtiqueta = widgets.Label (value="Posición Inicial $(m)$:")
    posSlider = widgets.IntSlider(min=-10.0, max=10.0, step=1.0, value=0.0)
    cajaPosición = widgets.HBox([posEtiqueta, posSlider])

    velEtiqueta = widgets.Label (value="Velocidad Inicial $(m/s)$:")
    velSlider = widgets.IntSlider(min=-50, max=50, step=1, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.IntSlider(min=-5, max=5, step=1, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=30, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=30,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoPosición, {'posInicial':posSlider,
                                                                  'velInicial':velSlider,
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaPosición, cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)
    
    
###########################################################################################################################


def GraficasVarias ():
    
    display (tag)
    
    def GraficoInteractivoGeneral(posInicial, velInicial, aceleración,tiempo):

      arregloTiempo = np.linspace (0, tiempo, 20)

      posiciónActual = CalculoPosición (posInicial, arregloTiempo, velInicial, aceleración)
      velocidadActual = CalculoVelocidad (arregloTiempo, velInicial, aceleración)
      aceleraciónActual = np.ones (20) * aceleración

      fig, (ax1, ax2, ax3) = plt.subplots (1, 3, figsize = (20,7), dpi= 120, sharex = True)

      ax1.set_xlabel('Tiempo $(s)$')
      ax1.set_ylabel('Posición $(m)$')
      ax1.plot (arregloTiempo, posiciónActual)
      ax1.set_xlim([0,35]) 
      ax1.set_ylim([-50,50])      
      ax1.grid ()
        
      ax2.set_xlabel('Tiempo $(s)$')
      ax2.set_ylabel('Velocidad $(m/s)$')
      ax2.plot (arregloTiempo, velocidadActual) 
      ax2.set_xlim([0,35])
      ax2.set_ylim([-5,5]) 
      ax2.grid ()
    
      ax3.set_xlabel('Tiempo $(s)$')
      ax3.set_ylabel('Aceleración $(m/s^2)$')
      ax1.set_xlim([0,35])
      ax3.set_ylim([-0.2, 0.2]) 
      ax3.plot (arregloTiempo, aceleraciónActual)        
      ax3.grid ()
    
      plt.show()

      return


    posEtiqueta = widgets.Label (value="Posición Inicial $(m)$:")
    posSlider = widgets.IntSlider(min=-10.0, max=10.0, step=1.0, value=0.0)
    cajaPosición = widgets.HBox([posEtiqueta, posSlider])

    velEtiqueta = widgets.Label (value="Velocidad Inicial $(m/s)$:")
    velSlider = widgets.FloatSlider(min=-0.1, max=0.1, step=0.01, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.FloatSlider(min=-0.1, max=0.1, step=0.01, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=30, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=30,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoGeneral, {'posInicial':posSlider,
                                                                  'velInicial':velSlider,
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaPosición, cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)