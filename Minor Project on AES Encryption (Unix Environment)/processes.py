import os
import subprocess
import time

while True:
   ps = subprocess.Popen(['ps', 'aux'])
   time.sleep(5)    
