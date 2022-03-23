import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

frecuencia_muestreo = 44100
frecuencia = 250
tiempos = np.linspace(0.0, 1.0, frecuencia_muestreo)
amplitud = np.iinfo(np.int16).max

ciclos = frecuencia * tiempos

fracciones, enteros = np.modf(ciclos)
data = fracciones

data = fracciones - 0.5

data = np.abs(data)

data = data - data.mean()

alto, bajo = abs(max(data)), abs(min(data))
data = amplitud * data / max(alto, bajo)

plt.figure()
plt.plot(tiempos, data)
plt.show()

write("triangular.wav",
    frecuencia_muestreo, data.astype(np.int16))

cantidad_muestras = len(data)
periodo_muestreo = 1.0 / frecuencia_muestreo
transformada = np.fft.rfft(data)
frecuencias = np.fft.rfftfreq(cantidad_muestras, periodo_muestreo)

plt.figure()
plt.plot(frecuencias, np.abs(transformada))
plt.show()