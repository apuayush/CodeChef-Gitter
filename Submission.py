from GitterClasses import *

# submission class


class Submission:

    def __init__(self, sid, verdict, link, lang, contestcode, pcode):
        self.sid = sid
        self.verdict = verdict
        self.link = link
        self.lang = lang
        self.contestcode = contestcode
        self.pcode = pcode

    def fetchAndSave(self, i):
        print 'Fetching ' + self.contestcode + '/' + self.pcode + '_' + str(i) + ' in ' + self.lang
        OK = False
        while OK is False:
            try:
                response = urllib2.urlopen(self.link)  # open webpage
                print 'Success'
                OK = True
            except urllib2.HTTPError as e:
                print 'Failure.\nAn HTTP error occured : ' + str(e.code)
                print 'Refetching..'

        html = response.read()
        if i != 0:
            opfile = open(
                Config.githubRepo + '/' + self.contestcode + '/' + self.pcode + '_' + str(
                    i) + '_' + str(
                        self.sid) + self.getExtension(
                            self.lang),
                 'w')
        else:
            opfile = open(
                Config.githubRepo + '/' + self.contestcode + '/' + self.pcode + '_' + str(
                    i) + '_' + str(
                        self.sid) + self.getExtension(
                            self.lang),
                 'w')
        opfile.write(HTMLParser.HTMLParser().unescape(html)[5:-6])
        pass


    def getExtension(self, lang):
    	Ext = {
    	'JAVA': '.java',
    	'PYTH': '.py',
    	'python3': '.py',
    	'python2': '.py',
    	'C++': '.cpp',
    	'c++': '.cpp',
    	'cpp': '.cpp',
    	'c': '.c',
    	'C': '.c'
    	}

        return Ext[lang]
