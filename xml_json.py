import xmltodict
import json
import os

root = "xml"
save = "xml_to_json"
dirs = os.listdir(root)
for file in dirs:
    file_name = file.split(".")
    xml=open(os.path.join(root,file),'r',encoding='UTF-8')
    xml_str=xml.read()

    xml_json=xmltodict.parse(xml_str)     #存储json格式下的文本内容
    xml_json=json.dumps(xml_json,indent=4)

    with open(os.path.join(save,file_name[0]+'.json'),'w') as f:
        f.write(xml_json)

