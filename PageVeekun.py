from Commons import Commons
from Page import Page
from PageBulbapediaEdit import PageBulbapediaEdit
import os

class PageVeekun(Page):
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
        self.mDexNum = dexNum
        if(link is None):
            link = self.findLink(dexNum)
        self.mLink = link
        try:
            cacheFile = open("cache/veekun/"+format(dexNum,'03')+".html","rb")
            self.mCode = cacheFile.read()
        except:
            self.mCode = Commons.downloadPage(link)
            try:
                os.mkdir("cache/")
            except:
                pass
            try:
                os.mkdir("cache/veekun/")
            except:
                pass
            open("cache/veekun/"+format(dexNum,'03')+".html","wb").write(self.mCode)

    @staticmethod
    def findLink(dexNum):
        'Finds the page link for this dex number'
        bulbaEditObject = PageBulbapediaEdit(dexNum)
        pokemonName = bulbaEditObject.getTemplateValue("pokefordex")
        linkVeekun = "http://veekun.com/dex/pokemon/"+pokemonName
        return linkVeekun