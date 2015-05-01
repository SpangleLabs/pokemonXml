from Commons import Commons
from Page import Page
import os

class PagePokemonDb(Page):
    '''
    pokemonDB page object. For retrieving information from a pokemonDB page
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
        cacheFileName = "cache/pokemondb/"+format(dexNum,'03')+".html"
        self.mCode = Commons.loadPage(cacheFileName,link)

    @staticmethod
    def findLink(dexNum):
        'Finds the pokemondb link for this dex number'
        return "http://pokemondb.net/pokedex/"+str(dexNum)