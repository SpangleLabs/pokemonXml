

class Page:
    '''
    generic page object, template for others.
    '''
    mDexNum = None  #(National) Pokedex number of pokemon
    mLink = None    #Page link
    mCode = None    #Code of page


    def __init__(self,dexNum,link=None):
        '''
        Constructor
        '''
        raise NotImplementedError
#        self.mDexNum = dexNum
#        if(link is None):
#            link = self.findLink(dexNum)
#        self.mLink = link
#        cacheFileName = "cache/bulbapedia/"+format(dexNum,'03')+".html"
#        self.mCode = Commons.loadPage(cacheFileName,link)

    @staticmethod
    def findLink(dexNum):
        'Finds the page link for this dex number'
        raise NotImplementedError
    
    def getDexNum(self):
        return self.mDexNum