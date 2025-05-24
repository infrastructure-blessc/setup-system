import subprocess

def set_hostname(name):
    subprocess.run(["hostnamectl", "set-hostname", name])
