#coding=utf-8
# only for linux
import subprocess
import sys
import os

local_path = os.path.split(os.path.abspath(__file__))[0]

svr_path = local_path 
tornado_svr = "main.py"
logfile="applog.log"
#bind_ip_addr = '' #127.0.0.x
port=8080


def start():
    cmd = "python %s --port=%d  --log_file_prefix=%s" %(tornado_svr , port , logfile)
    subprocess.Popen(cmd , shell=True , cwd=svr_path) # start child program
    print '\n'.join( get_process( tornado_svr ) )


def stop():
    for line in get_process(tornado_svr):
        pid = int(line.split(None, 2)[1])
        os.kill(pid, 9)

def get_process( name ):
    p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    res = []
    for line in out.splitlines():
        if name in line:
           res.append( line )
    return res


if __name__ == '__main__':
   cmd = sys.argv[1]
   globals()[cmd]()