import datetime
import glob
import json
import sys
import time
import xmltodict
import os
from testlog import curr
x = datetime.datetime.now().strftime("%Y%m%d")


def insert(root):
    try:
        list_of_files = glob.glob(root + '/*.xml')
        data = max(list_of_files, key=os.path.getctime)
        print(data)
        fxml = open(data, 'r')
        xml_data = fxml.read()
        fxml.close()
        temp_data = xmltodict.parse(xml_data)
        data = json.dumps(temp_data)
        output = json.loads(data)
        test_data = curr.find({"data": output})
        if test_data is not None:
            pass
        else:
            curr.insert({"date": x, "data": output})

    except Exception as e:
        print(e)


while 1:
    insert(sys.argv[1])
    time.sleep(20)
