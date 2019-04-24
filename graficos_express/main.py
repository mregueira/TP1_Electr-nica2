from util_python import read_csv
from util_python import Senial
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from ExpressPlot import ExpressPlot


# ExpressPlot.CombinedPlot()\
#         .setTitle("Respuesta en frecuencia")\
#         .setXTitle("Frecuencia (Hz)")\
#         .setYTitle("Fase")\
#         .setYTitle2("Amplitud (dB)")\
#         .setLogarithmic()\
#         .addSpiceBodePlot(
#             filename="input/Fuente_SinComp.txt",
#             color="red",
#             name="Magnitud",
#             color2="blue",
#             name2="Fase",
#             mode=ExpressPlot.BOTH
#         )\
#         .plot()\
#         .addDataTipBodeMag()\
#         .show() \
#         .save(filename="output/Fuente_SinComp.png")

ExpressPlot.CombinedPlot()\
        .setTitle("Respuesta en frecuencia")\
        .setXTitle("Frecuencia (Hz)")\
        .setYTitle("Fase")\
        .setYTitle2("Amplitud (dB)")\
        .setLogarithmic()\
        .addSpiceBodePlot(
            filename="input/Fuente_ConComp.txt",
            color="red",
            name="Magnitud",
            color2="blue",
            name2="Fase",
            mode=ExpressPlot.BOTH
        ) \
        .plot() \
        .addDataTipBodeMag() \
        .show() \
        .save(filename="output/Fuente_ConComp.png")

#plotAndSave(filename="output/bode1.png")

#plt.show()