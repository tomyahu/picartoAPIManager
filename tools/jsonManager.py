import json
import urllib2

def get_from_url(url):
    '''
    Gets json data from a url
    :param url: the url where the json file is located
    :return: a dictionary with the data
    '''
    json_obj = urllib2.urlopen(url)
    return json.load(json_obj)