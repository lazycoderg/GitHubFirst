import os,base64

num = os.urandom(32)

key = base64.b64encode(num)
