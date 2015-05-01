import urllib.request


class Commons:
    '''
    Commons class, contains a number of useful static methods
    '''

    @staticmethod
    def downloadPage(url):
        #time.sleep(3)
        pagerequest = urllib.request.Request(url)
        pagerequest.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0')
        pageopener = urllib.request.build_opener()
        code = pageopener.open(pagerequest).read()
        return code