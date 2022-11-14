from preicfesapp.models import Pregunta, Respuesta, Quiz

"""
txt Pedro está estudiando si la energía eólica se puede utilizar en un determinado punto de la Guajira, y encuentra que la velocidad mínima del viento para que esta funcione es de 5 m/s. Él tiene la hipótesis de que en ese lugar la velocidad oscila entre 8 m/s y 11 m/s durante todo el año. ¿Qué diseño experimental permite analizar la hipótesis de Pedro?
A. Se debe evaluar la velocidad del viento una sola vez en varios puntos de la Guajira.
B. Se debe instalar un molino de viento en el punto y determinar si funciona o no.
C. Se debe evaluar la velocidad del viento varias veces al día durante un solo día.
D. Se debe evaluar la velocidad del viento varias veces al día durante diferentes épocas del año.

ctx Antes de 1850, se creía que la evolución de los seres vivos se daba por la capacidad de cada individuo para cambiar, en respuesta a las nuevas condiciones del medio. Por ejemplo, las jirafas primitivas tenían el cuello corto, pero, para reducir la competencia por el alimento, alargaron su cuello para tomar las hojas que estaban en la parte alta de los árboles. En 1859, se planteó que cada jirafa no podía alargar su cuello, sino que las jirafas que tuvieran cuellos un poco más largos eran las que sobrevivían, se reproducían y heredaban esa característica a su descendencia.
txt Con base en lo anterior, ¿cuál de los siguientes aspectos pudo dar evidencia para cambiar la idea sobre la evolución de las jirafas?
A. Se realizó una serie metódica de observaciones a varias generaciones de jirafas.
B. Se fotografió a un grupo de jirafas de cuello largo comiendo hojas de las copas en 1859.
C. Se hicieron disecciones de una pareja de jirafas para estudiar sus órganos.
D. Se comparó el ADN de un grupo de jirafas primitivas con el de un grupo de jirafas actuales.
"""

filename = 'texto.txt'

def process_file_lines():
    """ Procesa una lista de lineas del archivo de texto """
    f = open(filename)
    dd = {'A. ': True, 'B. ': True, 'C. ': True, 'D. ': True}
    ctx = False
    for line in f:
        if line.startswith('ctx'):
            pregunta = Pregunta(contexto=line[4:])
            ctx = True
            continue
        if line.startswith('txt') and ctx == True:
            pregunta.texto = line[4:]
            ctx = False
            continue
        if line.startswith('txt'):
            pregunta = Pregunta(texto=line[4:])
            continue
        if dd.get(line[:3], False):
            print(line[:3])
            if line[:3] == 'A. ':
                pregunta.save()
            respuesta = Respuesta(texto=line[3:], pregunta=pregunta)
            respuesta.save()
            if line[:3] == 'D. ':
                ctx = False
    print('Done...')
    f.close()

