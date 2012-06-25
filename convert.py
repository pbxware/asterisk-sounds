#!/usr/bin/python

import sys, commands

FORMAT = sys.argv[1]
files = commands.getoutput('find ./ -name \'*mp3\'').split('\n')

if len(sys.argv) == 2:
    for i in files:
        out_name = i.replace('mp3', FORMAT)
        if FORMAT == 'gsm':
            cmd = 'sox "%s" -r 8000 -c1 "%s" resample -ql' % (i, out_name)
        elif FORMAT == 'wav':
            cmd = 'sox "%s" -r 8000 -e signed -c 1 "%s"' % (i, out_name)
	print cmd, commands.getoutput(cmd)
elif len(sys.argv) == 3:
    out_name = sys.argv[2].replace('mp3', FORMAT)
    if FORMAT == 'gsm':
        cmd = 'sox "%s" -r 8000 -c1 "%s" resample -ql' % (sys.argv[2], out_name)
    elif FORMAT == 'sln':
        cmd = 'sox "%s" -t raw -r 8000 -s -w -c 1 "%s"' % (sys.argv[2], out_name)
    print cmd, commands.getoutput(cmd)


