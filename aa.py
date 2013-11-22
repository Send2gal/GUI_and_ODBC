import os
a = "a5:00:a5:00:00:00:05:8f"
path = "SU-"+a.replace(":","")[-4:]
try:
    os.mkdir("c:\\temp\\" +path)
except:
    pass