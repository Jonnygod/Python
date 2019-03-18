import time
import codecs
import json

class PipelineJson(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today+".json"
        with codecs.open(fileName,'a','utf-8') as fp:
            jsonStr = json.dumps(dict(item))
            fp.write("%s \r\n" %jsonStr)
        print("Json读写完成")
        fp.close()
        return item