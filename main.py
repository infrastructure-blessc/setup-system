import yaml
import time
from src.utils.logger import log_step
from src.system import users, hostname, ssh
from src.k0s import install

with open("config.yaml") as f:
    config = yaml.safe_load(f)

log_step("🧑 Adding system users")
users.create_users(config["system"]["users"])

log_step("🖥 Setting hostname")
hostname.set_hostname(config["system"]["hostname"])

log_step("🔐 Configuring SSH")
ssh.configure_ssh(config["system"]["ssh"])

log_step("✅ Configuration complete. Reboot will now be handled by install.sh.")
time.sleep(5)