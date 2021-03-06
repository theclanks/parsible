import re
import logging
from datetime import datetime
import time

def parse_asterisk(line):
    rtrnobj = {}
    regex = re.compile("^(\[[\d,\w,\s,:]+\])\ ([A-Z,a-z]+)(\[[0-9]+\])\ ([\w,.]+)\:[\s,\-,\=,>]+([\D,*,\/,\d]+)$")
    regex_channels = re.compile("([A-Z,a-z]+\/[\w,\d,@]+-[\w,\d,\.,\;,-]+)")
    matchobj = regex.search(line)
    if matchobj:
        try:
            rtrnobj["date"] = matchobj.group(1).strip("]").strip("[")
            #logging.debug("Get date, OK!")
            now = datetime.now()
            rtrnobj["date"] = rtrnobj["date"]+" "+str(now.year)
            rtrnobj["date"] = datetime.strptime(rtrnobj["date"], "%b  %d %H:%M:%S %Y")
            rtrnobj["type"] = matchobj.group(2)
            #logging.debug("Get Message, OK!")
            rtrnobj["message_id"] = matchobj.group(3).strip("]").strip("[")
            #logging.debug("Get Message cod, OK!")
            rtrnobj["app"] = matchobj.group(4)
            #logging.debug("Get app, OK!")
            rtrnobj["message"] = matchobj.group(5)
            #logging.debug("Get message, OK!")
            if "message" in rtrnobj:
                matchchannels = regex_channels.findall(rtrnobj["message"])
                if matchchannels:
                    rtrnobj["channels"] = matchchannels


        except IndexError:
            logging.error("Unable parser information in asterisk, some regex group missing")
    else:
	logging.debug("Not value found on regex")

    return rtrnobj
