from Commons import Commons
from Page import Page

class PagePsypokes(Page):
    '''
    psypokes page object. For retrieving information from a psypokes page
    '''
    mDexNum = None  #(National) Pokedex number of pokemon
    mLink = None    #Page link
    mCode = None    #Code of page


    def __init__(self,dexNum,link=None):
        '''
        Constructor
        '''
        self.mDexNum = dexNum
        if(link is None):
            link = self.findLink(dexNum)
        self.mLink = link
        try:
            cacheFile = open("cache/psypokes/"+format(dexNum,'03')+".html","rb")
            self.mCode = cacheFile.read()
        except:
            self.mCode = Commons.downloadPage(link)
            open("cache/psypokes/"+format(dexNum,'03')+".html","wb").write(self.mCode)

    @staticmethod
    def findLink(dexNum):
        'Finds the psypokes link for this dex number'
        return "http://www.psypokes.com/dex/psydex/"+format(dexNum,'03')+"/general"