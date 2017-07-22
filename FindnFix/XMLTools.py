# import xml.etree.ElementTree as ET
# from xml.dom import minidom as MD
from lxml import etree


def file_to_tree(xmlFile, remove_blank_text=True, ns_clean=True, remove_comments=True):
    parser = etree.XMLParser(remove_blank_text=remove_blank_text, ns_clean=ns_clean, remove_comments=remove_comments)
    return etree.parse(xmlFile, parser)


def pprint(tree):
    return etree.tostring(tree, pretty_print=True)


# def find_elements(tree, element):
#     return tree.xpath('{0}'.format(element))


def find_elements(tree, element, namespace=None):
    if namespace is None:
        namespace = {}
    return tree.xpath(element, namespaces=namespace)


def find_attributes(tree, element, attribute, namespace=None):
    if namespace is None:
        namespace = {}
    results = []
    for el in find_elements(tree, element, namespace):
        att = el.xpath('./@{0}'.format(attribute))
        results.append((att, el))
    return results


def element_text(element):
    return element.xpath('text()')[0]

