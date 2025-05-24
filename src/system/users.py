import subprocess
import os
from src.utils.logger import log_info


def create_users(users):
    for user in users:
        name = user["name"]
        key = user["sshkey"]

        subprocess.run(["useradd", "-m", "-s", "/bin/bash", "-p", "!", name])
        subprocess.run(["usermod", "-aG", "sudo", name])
        ssh_dir = f"/home/{name}/.ssh"
        os.makedirs(ssh_dir, exist_ok=True)

        with open(f"{ssh_dir}/authorized_keys", "w") as f:
            f.write(key)

        subprocess.run(["chown", "-R", f"{name}:{name}", ssh_dir])
        subprocess.run(["chmod", "700", ssh_dir])
        subprocess.run(["chmod", "600", f"{ssh_dir}/authorized_keys"])

        with open(f"/etc/sudoers.d/99_{name}_nopasswd", "w") as f:
            f.write(f"{name} ALL=(ALL) NOPASSWD:ALL\n")
        subprocess.run(["chmod", "440", f"/etc/sudoers.d/99_{name}_nopasswd"])

        log_info(f"Created user {name}")
