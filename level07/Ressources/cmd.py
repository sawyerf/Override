import subprocess
import re

cmd = subprocess.Popen("python script.py | ./level07", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in cmd.stdout.readlines():
	if b'data[' in line and b'is 0' not in line:
		nb = re.findall('is ([0-9]*)', line.decode())[0]
		idx = re.findall('data\[([0-9]*)\]', line.decode())[0]
		print(idx, ':', hex(int(nb)))

