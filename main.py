from all_link.start_all import start_all
from mysqls.pandasql import Links,deleteWhere,deleteAll
import fileinput
print("DO YOU WANT TO SCRAPE (y/N):")
for line in fileinput.input():
    if line.rstrip().lower() == "y":
        deleteAll()
        from all_link.link141 import link141
        link141()
    else:
        break



# deleteWhere(LA_name="County Durham")
# start_all()






















