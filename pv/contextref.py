import re

class ContextRef(object):

    def __init__(self, xbrl):
        self.xbrl = xbrl

    @classmethod
    def processtag_period(self,tag):
        #print(tag.period)
        if(tag.period.startdate) == None:
            print(tag.period.instant)
        else:
            print(tag.period.startdate)
            print(tag.period.enddate)

    @classmethod
    def format(self,refs):
        for idx,ref in enumerate(refs):
            print("\n")
            print(idx,"\n")
            self.processtag_period(ref)
            #print(ref)
            #print(ref.period)
            #print(ref.period.startdate)

    @classmethod
    def getContextTags(self,xbrl):
        doc_root = ""
        context_tags = xbrl.find_all(name=re.compile(doc_root + "context",
                                        re.IGNORECASE | re.MULTILINE))
        return(context_tags)
