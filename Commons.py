import urllib.request
import re

class Commons:
    '''
    Commons class, contains a number of useful static methods
    '''
    tagRegex = re.compile('<[^>]*>')

    @staticmethod
    def downloadPage(url):
        #time.sleep(3)
        pageRequest = urllib.request.Request(url)
        pageRequest.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0')
        pageOpener = urllib.request.build_opener()
        code = pageOpener.open(pageRequest).read()
        return code