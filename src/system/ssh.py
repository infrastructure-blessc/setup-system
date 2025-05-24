import re
from src.utils.logger import log_info

def configure_ssh(ssh_config):
    port = ssh_config["port"]
    with open("/etc/ssh/sshd_config", "r") as file:
        content = file.read()

    content = re.sub(r"^#?PasswordAuthentication.*", "PasswordAuthentication no", content, flags=re.M)
    content = re.sub(r"^#?PermitRootLogin.*", "PermitRootLogin no", content, flags=re.M)
    content = re.sub(r"^#?Port\s+\d+", f"Port {port}", content, flags=re.M)

    with open("/etc/ssh/sshd_config", "w") as file:
        file.write(content)

    import subprocess
    subprocess.run(["systemctl", "restart", "ssh"])
    log_info("SSH configured")
