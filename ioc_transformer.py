#!/usr/bin/python
"""
simple script to encode or decode an ioc with brackets around the dots
"""
import argparse
import os

def encoder(ioc):
    if os.path.isfile(ioc):
        iocs = []
        with open(ioc,'r') as iocfile:
            for line in iocfile.readlines():
                iocs.append(encoder(line.strip()))
        converted = "\n".join(iocs)

    elif isinstance(ioc, str):
        listed = list(ioc)
        chars  = ['.',':']
        for n,i in enumerate(listed):
            if i in chars:    
                listed[n] = '['+i+']'
        if ioc[0:4] == 'http':
            listed[1] = 'x'
            listed[2] = 'x'
        converted = "".join(listed)

    return converted

def decoder(ioc):
    if os.path.isfile(ioc):
        iocs = []
        with open(ioc,'r') as iocfile:
            for line in iocfile.readlines():
                iocs.append(decoder(line.strip()))
        converted = "\n".join(iocs)
    elif isinstance(ioc,str):
        listed = list(ioc)
        chars  = ['[',']']
        for n,i in enumerate(listed):
            if i in chars:    
                listed.pop(n)

        if ioc[0:4] == 'hxxp':
            listed[1] = 't'
            listed[2] = 't'
        converted = "".join(listed)
    return converted

if __name__ == '__main__':
    parser  = argparse.ArgumentParser(description='ioc encoder and decoder',
                                      version='0.1')
    sub     = parser.add_subparsers(help='commands', dest='cmd')

    # Encode command
    search_parser = sub.add_parser('encode',help='encode ioc')
    search_parser.add_argument('sample', action='store',help='ioc to encode')

    # Decode command
    submit_parser = sub.add_parser('decode',help='Decode ioc')
    submit_parser.add_argument('sample', action='store',help='ioc to decode')

    # Process the user input
    args = parser.parse_args()
    if args.cmd == 'encode':
        result = encoder(args.sample)
    elif args.cmd == 'decode':
        result = decoder(args.sample)
    else:
        result = 'You need to tell me what to do! (encode or decode)'
    print result
