import re

txt = "holha bohn dia"
txt = "avui estas be?"
n_txt = list(txt)
x = re.search("(^\w)\w+\s(\w)\w+\s(\w)", txt)

print (txt)
print (n_txt)
print (x.groups())

print ()
h = str(x.group(1))
index_h = txt.index(h)
print (x.group(1))
print (index_h)

b = str(x.group(2))
index_b = txt.index(b)
print (x.group(2))
print (index_b)

d = str(x.group(3))
index_d = txt.index(d)
print (x.group(3))
print (index_d)

print ()
n_txt[index_h] = h.upper()
n_txt[index_b] = b.upper()
n_txt[index_d] = d.upper()
txt = "".join(n_txt)
print (n_txt)
print (txt)