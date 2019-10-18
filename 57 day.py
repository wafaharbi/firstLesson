# ____________ 57 day _____________ #

#Python Regular Expression

import re

txt = "The rain in Spain"
x =  re.search("^The.*Spain$", txt)

if (x):
    print("yes ! we match")
else:
    print("Not match")
