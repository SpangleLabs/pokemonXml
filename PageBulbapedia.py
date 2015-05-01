from Commons import Commons
import re

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
    
    def getAnimeDexEntries(self):
        animeDexRegex = re.compile('<h3><span[^>]*>[^<]*dex entries</span></h3>(.*?)<h3>',re.DOTALL|re.IGNORECASE)
        animeDexEntryRegex = re.compile('<td> *<a[^>]*>([A-Z]+[0-9]+)</a>[^<]*</td>[^<]*<td> *<strong class="selflink">[^<]*</strong>[^<]*</td>[^<]*<td>[^<]*</td>[^<]*<td>(.*?)</td>',re.DOTALL|re.IGNORECASE)
        tagRegex = Commons.tagRegex
        animeDexSearch = re.search(animeDexRegex,self.mCode)
        if(animeDexSearch is None):
            print("no anime dex section")
            continue
        animeDexCode = animeDexSearch.group(1)
        outputList = []
        for animeDexEntrySearch in re.finditer(animeDexEntryRegex,animeDexCode):
            animeDexDict = {}
            animeDexDict['episode'] = animeDexEntrySearch.group(1)
            animeDexDict['entry'] = tagRegex.sub('',animeDexEntrySearch.group(2)).strip()
            outputList.append(animeDexDict)
        return outputList
