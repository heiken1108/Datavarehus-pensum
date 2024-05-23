import Beregningsfunksjoner as Bf
import Transaksjon as T
import DataPlots as Dp
import Matriser as M
import Algoritmer as A

items, transaksjoner = T.GenererTransaksjon(6, 5, True)

T.printTransaksjoner(A.Apriori_Itemset_Generator(items, transaksjoner, 3))