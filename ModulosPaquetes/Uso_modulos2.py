#esta linea se podria simplificar:
from Paquetes.calculos.basicos.operaciones_basicas import *

## vemos como podemos utilizar los paquetes con modulos. Como vemos si queremos 
## utilizar redondea() no podemos porque no forma parte del sub-paquete basicos 
## en el modulo operaciones_basicas ni tiene en su interior una funcion redondea()
## igualmente potencia()


redondear(32.7)

multiplicar(5, 94)

potencia(5,2)
