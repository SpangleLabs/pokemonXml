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
        cacheFileName = "cache/veekun/"+format(dexNum,'03')+".html"
        self.mCode = Commons.loadPage(cacheFileName,link)

    @staticmethod
    def findLink(dexNum):
        'Finds the page link for this dex number'
        if(dexNum==413):
            return "http://veekun.com/dex/pokemon/wormadam"
        if(dexNum==555):
            return "http://veekun.com/dex/pokemon/darmanitan"
        if(dexNum==648):
            return "http://veekun.com/dex/pokemon/meloetta"
        bulbaEditObject = PageBulbapediaEdit(dexNum)
        pokemonName = bulbaEditObject.getTemplateValue("pokefordex")
        linkVeekun = "http://veekun.com/dex/pokemon/"+pokemonName
        linkVeekun = linkVeekun.replace("nidoran(f)","nidoran%E2%99%80")
        linkVeekun = linkVeekun.replace("nidoran(m)","nidoran%E2%99%82")
        linkVeekun = linkVeekun.replace("mr_mime","mr.%20mime")
        linkVeekun = linkVeekun.replace("mime_jr","mime%20jr.")
        linkVeekun = linkVeekun.replace("flabebe","flab%C3%A9b%C3%A9")
        linkVeekun = linkVeekun.replace("meowstic-f","meowstic")
        return linkVeekun