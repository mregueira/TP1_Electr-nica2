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

# ExpressPlot.CombinedPlot()\
#         .setTitle("Respuesta en frecuencia")\
#         .setXTitle("Frecuencia (Hz)")\
#         .setYTitle("Fase")\
#         .setYTitle2("Amplitud (dB)")\
#         .setLogarithmic()\
#         .addSpiceBodePlot(
#             filename="input/Fuente_ConComp.txt",
#             color="red",
#             name="Magnitud",
#             color2="blue",
#             name2="Fase",
#             mode=ExpressPlot.BOTH
#         ) \
#         .plot() \
#         .addDataTipBodeMag() \
#         .show() \
#         .save(filename="output/Fuente_ConComp.png")

ExpressPlot.CombinedPlot()\
        .setTitle("Caraterística Io - Vo")\
        .setXTitle("Io (A)")\
        .setYTitle("Vo (V)")\
        .addExcelPlot(
                filename="input/CaracteristicaVoIo_Medido.xlsx",
                fieldX="Io",
                fieldY="Vo",
                color="blue",
                name="Medido"
        )\
        .addExcelPlot(
                filename="input/CaracteristicaVoIo_Simulado.xlsx",
                fieldX="Io",
                fieldY="Vo",
                color="red",
                name="Simulado"
        )\
        .addExcelPlot(
                filename="input/CaracteristicaVoIo_Teorico.xlsx",
                fieldX="Io",
                fieldY="Vo",
                color="green",
                name="Teórico"
        )\
        .plot()\
        .addDataTip(
                titleX="Io",
                titleY="Vo",
                unitX="A",
                unitY="V"
        )\
        .show()\
        .save(filename="output/Caracteristica_iovo.png")
#plotAndSave(filename="output/bode1.png")

#plt.show()