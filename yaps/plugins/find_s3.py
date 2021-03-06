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

import re
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def find_s3(paste,raw):
    try:
        pttrn = "https?:\/\/s3\.amazonaws\.com[\/A-z0-9\/-]+\/"
        matches = re.findall(pttrn,raw)
        lines = []
        date = datetime.now()
        for m in matches:
            l = "{0},{1},{2}\n".format(date,paste['key'],str(m))
            lines.append(l)

        if len(lines) > 0:
            with open('s3_buckets.csv','a') as ofile:
                for l in lines:
                    ofile.write(l)
            logger.info(" {0} s3 bucket found in paste {1}".format(len(lines),paste['key']))
    except Exception as e:
        logger.debug(" {0} error occurred in func find_onion: {1}".format(str(datetime.now()),e))
    finally:
        return
