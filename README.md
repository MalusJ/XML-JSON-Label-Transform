# LabelTransform

该项目用于将图片标签的不同形式（xml与json）进行互相转换

# 文件介绍

<xml_json.py>和<json_xml.py>：分别为“将xml格式标注转换为json格式标注”和“将json格式标注转换为xml格式标注”的程序

<picutres>：用于存储被标签的图片

<xml>和<json>：用于存储“需要被转换的xml标签”与“需要被转换的json标签”

<xml_to_json>和<json_to_xml>：用于存储“转换过后得到的json标签”与“转换过后得到的xml标签”

## 安装指南

需要用到的module xmltodict已经安装在<venv>的虚拟运行环境中了

如果不能运行可以用[pip](https://pip.pypa.io/en/stable/)安装

在cmd界面cd到venv/Scripts文件夹中然后输入指令

```bash
pip install xmltodict
```
## 标注指南

所有xml的标注文件由[labelImg]（https://tzutalin.github.io/labelImg/）制作

所有json的标准文件由[LabelImage](https://rachelcao277.github.io/LabelImage/)制作


## 使用方法

xml转json： 文件放入<xml>中运行<xml_json.py> 在<xml_to_json>中得到同名json文件

json转xml： 文件放入<json>中运行<json_xml.py> 在<json_to_xml>中得到同名xml文件



code by Malus
