import csv

numba=71
for a in range(379):
    f = open("all_link/start_all.py", "a")
    f.write("from all_link.link%s import link%s\n" % (str(numba),str(numba)))
    f.close()
    f = open("all_link/start_all2.py", "a")
    f.write("    link%s()\n" % (str(numba)))
    f.close()
    numba+=1





