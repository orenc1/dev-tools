import subprocess, re
def main():
    output = subprocess.run('crc console --credentials'.split(), stdout=subprocess.PIPE).stdout.decode().split('\n')
    for line in output:
        if 'kubeadmin' in line:
            login = re.search("'(.*)'", line).group(1)
    subprocess.run(login.split())

if __name__=='__main__':
    main()
