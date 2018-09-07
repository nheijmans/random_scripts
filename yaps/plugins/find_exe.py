#!/usr/bin/python
# Copyright (c) 2018 nheijmans
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import logging
import base64
import time
import re
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def find_exe(paste,raw):
    """ decode the base64 encoded paste and return """

    signature   = "TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAA4fug4AtAnNIbgBTM0hVGhpcyBwcm9ncmFtIGNhbm5vdCBiZSBydW4gaW4gRE9TIG1vZGU"
    rule        = "TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAA4fug4AtAnNIbgBTM0hVGhpcyBwcm9ncmFtIGNhbm5vdCBiZSBydW4gaW4gRE9TIG1vZGU[A-z0-9/\+]{1,}"
    result      = None
    try:
        match = re.search(rule, raw)
        if raw[0:155] == signature:
            result = (paste['key'], raw)
        elif match:
            s = match.start()
            e = match.end()
            result = (paste['key']+"_re", raw[s:e])
        if result:
           convert_b64(result)
    except Exception as e:
        logger.debug(" {0} error occurred in func find_exe: {1}".format(str(datetime.now()),e))
        result = None
    finally:
        return 

def convert_b64(paste):
    """ this function expects a tuple, 0=paste_key, 1=raw_text """
    try:
        fn = "samples/{0}_{1}.bin".format(paste[0],int(time.time()))
        with open(fn,'wb') as ofile:
            ofile.write(base64.decodestring(paste[1]))
        logger.info(" {0} executable found in paste {1}".format(str(datetime.now()),paste[0]))
    except Exception as e:
        logger.debug(" {0} error occurred in func convert_base64: {1}".format(str(datetime.now()),e))

    finally:
        return 
