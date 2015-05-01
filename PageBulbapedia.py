from Commons import Commons

class PageBulbapedia(object):
    '''
    bulbapedia page object. For retrieving information from a bulbapedia page
    '''
    mDexNum = None  #(National) Pokedex number of pokemon
    mLink = None    #Page link
    mCode = None    #Code of page


    def __init__(self,dexNum,link):
        '''
        Constructor
        '''
        try:
            cacheFile = open("cache/bulbapedia/"+format(dexNum,'03')+".html","rb")
            self.mCode = cacheFile.read()
        except:
            self.mCode = Commons.downloadPage(link)
            open("cache/bulbapedia/"+format(dexNum,'03')+".html","wb").write(self.mCode)