
import os
import re

def file_change(fname, web_addr):
    r = ur'upstream'  
    r1 = ur'}'
        
    old = open(fname).readlines()
    lines = 0
    begin = False
    del_lines = []
    for s in old:
        if begin:
            if re.search(r1,s):
                begin = False
            del_lines.append(lines)
        if re.search(r, s):
            begin = True
        
        lines += 1
        
    for i in del_lines:
        del old[del_lines[0]]
        
    web_list = web_addr.split(',')
    s1 = 0
    for s in web_list:
        web_list[s1]= '        server ' + s + ';\n'
        s1 += 1
    
    web_list.append('      }\n')
        
    new_list = []  
    for s in old:
        new_list.append(s)
        if re.search(r, s):
            for ss in web_list:
                new_list.append(ss)
        
    fp = open(fname,'w')
    for s in new_list:
        fp.write(s)
    
    fp.close()
    
if __name__ == '__main__':       
    web_addr = os.getenv('WEB_ADDR')
    if web_addr:
    	file_change('/etc/nginx/nginx.conf', web_addr)
