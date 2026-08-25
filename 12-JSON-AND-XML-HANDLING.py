import os
import xml.etree.ElementTree as xml 
import json


data = {
    "name": "Mauricio Piedra",
    "age": 32,
    "birth_date": "21-8-1994",
    "programming_languages": ["Python"]
}

xml_file = "data.xml"
json_file = "data.json"

# XML

def create_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON

def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

    with open(json_file, "r") as json_data:
        print(json_data.read())

create_json()

os.remove(json_file)

""" 
EXTRA CHALLENGE
* Using the logic for creating the previous files, create a program 
 * capable of reading and transforming the data stored in the XML and JSON 
 * into a single custom class of your language.
 * Delete the files.
 """

create_xml()
create_json()

class Data:

    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    data_from_xml = Data(name, age, birth_date, programming_languages)
    print(data_from_xml.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"], 
        json_dict["age"], 
        json_dict["birth_date"], 
        json_dict["programming_languages"]
    )

    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)