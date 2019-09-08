import re

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n") or x.endswith("\r"): return x[:-1]
    return x

inf = open("include/config.h.in", "r")
print "Opened in file"

outf = open("include/config.h.in.2", "w")
print "Opened out file"

for l in inf:
    p = re.compile('(?<=#cmakedefine ).*$')
    m = p.search(l)
    if m != None:
        s = m.group()
        outf.write(chomp(l) + " @" + s + "@\n")
    else:
        outf.write(l)
    print(l)



inf.close()
print "Closed in file"
outf.close()
print "Closed out file"
