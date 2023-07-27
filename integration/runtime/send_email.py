from xml.etree.ElementTree import Element, ElementTree, tostring
import requests

# 1.) Convert JSON string to XML string
def json_to_xml(json_string):
    """
    :param json_data:json data
    :return:xml data
    """
    root = Element('root')
    for key, value in json_string.items():
        if isinstance(value, dict):
            sub_root = Element(key)
            root.append(sub_root)
            json_to_xml(value, sub_root)
        else:
            root.set(key, value)
    return tostring(root, encoding='utf-8')
# 2.) Send XML string with HTTP POST
def send_xml_to_server(xml_data):
    """
    :param xml_data: xml data
    :return:
    """
    url = "http://localhost:8080/xml"
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url, data=xml_data, headers=headers)
    return response
# <<Amazon CodeWhisperer generated code goes here>>

def handler(event, context):

    # call method 1.) with var "event" to convert json to xml
    xml_data = json_to_xml(event)
    # call method 2.) to post xml
    response = send_xml_to_server(xml_data)
    return {
        'statusCode': 200,
        "message": "Success!"
    }
