import json
import jsonpath_ng as jp


def testJsonPathNg():
    datafile="./store.json"
    with open(datafile, 'r') as json_file:
        jsdata = json.load(json_file)
   
    #print(jsdata['store']['book'][0]['title'])
    #str1=jsonPath.parse(jsdata, "$..author").toJSONString()
    jpjp.JSONPath()


if __name__ == "__main__":
    testJsonPathNg()
