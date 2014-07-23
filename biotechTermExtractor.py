# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#oggpnosn
#hkhr

# <codecell>


# <codecell>

from urllib import urlencode
from urllib2 import urlopen, Request
import string
from scrapy.selector import Selector
from urllib2 import HTTPError
import json 
from threading import Thread

# <codecell>

#utility

documentList = []
fob = open("biotechTermsTest.json","w")
noOfThreads = 6
interval = 4000/noOfThreads
# <codecell>
documentList = []
documentListComponents = []
for i in range(noOfThreads):
    documentListComponents.append([])

def extractor(index):
    for i in range(interval*index,interval*(index+1)):
        try:
            htmlContentResponse = urlopen("http://biotechterms.org/sourcebook/saveidretrieve.php3?id=%s"%(str(i)))
            if htmlContentResponse.code == 200:
                htmlContent = htmlContentResponse.read()
                selector = Selector(text = htmlContent)
                document = {}
                title = selector.xpath("/html/body/table[2]/tr/td[2]/b/text()").extract()[0]
                document["title"] = title
                definition = selector.xpath("/html/body/table[2]/tr/td[2]").extract()[0]
                i1 = definition.index("<br>")
                i2 = i1 + definition[i1+4:].index("<br>") + 4 
                definition = definition[i1+4:i2]
                document["definition"] = definition
                linksTo = selector.xpath("/html/body/table[2]/tr/td[2]/a/text()").extract()
                document["linksTo"] = linksTo
                linksFrom = selector.xpath("/html/body/table[3]/tr/td[2]/a/text()").extract()
                document["linksFrom"] = linksFrom
                print "Extracted %s"%(document["title"]) 
                documentListComponents[index].append(document)
        except:
            pass

# <codecell>

threads = []
for i in range(noOfThreads):
    threads.append(Thread(target = extractor, args = (i)))

for i in range(noOfThreads):
    threads[i].start()

for i in range(noOfThreads):
    threads[i].join()

for i in range(noOfThreads):
    documentList.extend(documentListComponents[i])

json.dump(documentList, fob)

# <codecell>


