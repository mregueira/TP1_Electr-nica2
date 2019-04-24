from util_python import read_csv
from util_python import Senial
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from ExpressPlot import ExpressPlot


ExpressPlot.CombinedPlot()\
        .setTitle("Respuesta en frecuencia")\
        .setXTitle("Frecuencia (Hz)")\
        .setYTitle("Amplitud (dB)")\
        .setYTitle2("Grados")\
        .setLogarithmic()\
        .addSpiceBodePlot(
            filename="input/Fuente_SinComp.txt",
            color="red",
            name="Magnitud",
            color2="blue",
            name2="Fase",
            mode=ExpressPlot.BOTH
        )\
        .addDataTipBodePha()\
        .save(filename="output/bode1.png")

#plotAndSave(filename="output/bode1.png")

#plt.show()