from Commons import Commons
import re
from Page import Page
import os

class PageBulbapediaEdit(Page):
    '''
    bulbapedia edit page object. For retrieving information from a bulbapedia edit page
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
        cacheFileName = "cache/bulbapedia_edit/"+format(dexNum,'03')+".html"
        self.mCode = Commons.loadPage(cacheFileName,link)

    @staticmethod
    def findLink(dexNum):
        'Finds the bulbapedia edit link for this dex number'
        listPage = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
        listCode = Commons.loadPage("cache/bulbapedia_list_page.html",listPage)
        linkRegex = re.compile(format(dexNum,'03').encode()+b"[\s]</td>[\s]<td>[\s]<a href=\"([^\"]*)")
        linkMatch = linkRegex.search(listCode)
        if(linkMatch is None):
            raise Exception("cannot find link")
        pageLink = "http://bulbapedia.bulbagarden.net"+linkMatch.group(1).decode()
        editLink = pageLink.replace("/wiki/","/w/index.php?title=")+"&action=edit"
        return editLink
    
    def getTemplateValue(self,templateValue):
        templateRegex = re.compile(b"^[\s]*"+templateValue.encode()+b"=([^|{]*)(\||{)",re.MULTILINE)
        templateSearch = templateRegex.search(self.mCode)
        if(templateSearch is None):
            return None
        return templateSearch.group(1).strip().decode()