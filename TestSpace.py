import Beregningsfunksjoner as Bf
import Transaksjon as T
import DataPlots as Dp
import Matriser as M
import Algoritmer as A

k = 7
d = 2

punkter = Dp.genererData(antallDimensjoner=d, antallKlynger=k, tilfeldig = True)

centroids = A.KMeans(punkter, k, d)


Dp.plotDataPunkter(punkter, centroids)
