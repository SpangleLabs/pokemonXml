import urllib.request
import re
import os

class Commons:
    '''
    Commons class, contains a number of useful static methods
    '''
    tagRegex = re.compile('<[^>]*>')

    @staticmethod
    def downloadPage(url):
        #time.sleep(3)
        print("Downloading "+url)
        pageRequest = urllib.request.Request(url)
        pageRequest.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0')
        pageOpener = urllib.request.build_opener()
        code = pageOpener.open(pageRequest).read()
        return code
    
    @staticmethod
    def loadPage(cacheFileName,url):
        try:
            cacheFile = open(cacheFileName,"rb")
            code = cacheFile.read()
        except:
            code = Commons.downloadPage(url)
            for dirName in ["/".join(cacheFileName.split("/")[:x]) for x in range(1,len(cacheFileName.split("/")))]:
                try:
                    os.mkdir(dirName)
                except:
                    pass
            open(cacheFileName,"wb").write(code)
        return code
        