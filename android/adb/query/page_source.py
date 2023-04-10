import os
import subprocess
import xml.etree.ElementTree as ET


def PageSource():
    # Run external adb exe file and dump uiautomator page source
    cmd = "adb shell uiautomator dump"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    process.wait()

    # Pull xml and parse it into object in python
    cmd = "adb pull /sdcard/window_dump.xml"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    process.wait()

    # Parse xml into object in python
    obj = ET.parse('window_dump.xml').getroot()
    os.remove('window_dump.xml')
    return _ParseElement(obj)

def _ParseElement(element):
    obj = {}
    obj['tag'] = element.tag
    obj['text'] = element.text
    obj['attrib'] = element.attrib
    obj['children'] = [_ParseElement(e) for e in element]
    return obj
