from Commons import Commons
import re
from PageGeneric import PageGeneric

class PageBulbapediaEdit(PageGeneric):
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
        try:
            cacheFile = open("cache/bulbapedia_edit/"+format(dexNum,'03')+".html","rb")
            self.mCode = cacheFile.read()
        except:
            self.mCode = Commons.downloadPage(link)
            open("cache/bulbapedia_edit/"+format(dexNum,'03')+".html","wb").write(self.mCode)

    @staticmethod
    def findLink(dexNum):
        'Finds the bulbapedia edit link for this dex number'
        listPage = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
        listCode = Commons.downloadPage(listPage)
        linkRegex = re.compile(format(dexNum,'03')+"[\s]</td>[\s]<td>[\s]<a href=\"([^\"]*)")
        linkMatch = linkRegex.search(listCode)
        if(linkMatch is None):
            raise Exception("cannot find link")
        pageLink = "http://bulbapedia.bulbagarden.net"+linkMatch.group(1)
        editLink = pageLink.replace("/wiki/","/w/index.php?title=")+"&action=edit"
        return editLink
        