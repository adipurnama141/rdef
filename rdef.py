import urllib2
import sys
from xml.dom import minidom


#x = raw_input("Input Word : ")
#print 'Looking definition for word "' + x + '"'

x = sys.argv[1]

url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/" + x + "?key=473f46b5-fd91-4d80-b0d0-dd19502e1022"
f = urllib2.urlopen(url)

proxy_handler = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_handler)
r = opener.open(url)
xml_fetched = r.read()
preprocessed_xml = xml_fetched.replace('<d_link>','|')
preprocessed_xml = preprocessed_xml.replace('</d_link>','|')


xmldoc = minidom.parseString(preprocessed_xml)
itemlist = xmldoc.getElementsByTagName('dt')
for s in itemlist:
	print('   '+s.childNodes[0].nodeValue)


print r.read()