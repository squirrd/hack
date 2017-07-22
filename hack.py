import os
import sys
import re

# Application Imports
import FindnFix
from FindnFix import OSTools as OSTools
from FindnFix import XMLTools as XMLTools
from FindnFix import JavaTools as JavaTools


tree_01 = XMLTools.file_to_tree('/opt/tomcat-inst02/webapps/manager/WEB-INF/web.xml')
tree_02 = XMLTools.file_to_tree('/opt/tomcat-inst02/conf/server.xml')

# print XMLTools.pprint(tree_01)

element = '//Connector'
results = XMLTools.find_elements(tree_02, element)
for r in results:
    print XMLTools.pprint(r)

print '== Find attributes(3 args)'
element = '//Connector'
attribute = 'redirectPort'
for r1,r2 in XMLTools.find_attributes(tree_02, element, attribute): #, namespace=None):
    print r1, XMLTools.pprint(r2)


element = './/d:error-page'
namespace={'d' : 'http://java.sun.com/xml/ns/javaee'}
elements = XMLTools.find_elements(tree_01, element, namespace)
for el in elements:
    print XMLTools.pprint(el)

print '== Find Elements =========='
element = './/d:error-page[d:exception-type="java.lang.Throwable"]/d:location'
namespace={'d' : 'http://java.sun.com/xml/ns/javaee'}
elements = XMLTools.find_elements(tree_01, element, namespace)
print elements
for el in elements:
    print XMLTools.pprint(el)
    print XMLTools.element_text(el)
