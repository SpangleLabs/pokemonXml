from PageBulbapedia import PageBulbapedia
from PageBulbapediaEdit import PageBulbapediaEdit
from PagePokemonDb import PagePokemonDb
from PagePsypokes import PagePsypokes
from PageSerebii import PageSerebii
from PageVeekun import PageVeekun
import time

timeStart = time.time()

for dexNum in range(1,722):
    timeNow = time.time()
    print(format(int(timeNow-timeStart),'05')+"s: starting "+str(dexNum))
    pageBulba = PageBulbapedia(dexNum)
    pageBulbaEdit = PageBulbapediaEdit(dexNum)
    pagePkmnDb = PagePokemonDb(dexNum)
    pagePsy = PagePsypokes(dexNum)
    pageSere = PageSerebii(dexNum)
    pageVee = PageVeekun(dexNum)
    
