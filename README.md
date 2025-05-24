# System setup

## About
This repository contains scripts for configuring a server. The scripts automate the setup of essential system configurations.

**Configurations include:**
- Hostname
- Sudo users
- Disabling SSH password login
- Disabling SSH root login
- SSH port

## Installation

To install the package, clone the repository using git:

```bash
git clone https://github.com/infrastructure-blessc/setup-k0s-control-plane setup
```

## Usage

Navigate to the cloned directory and run the installation script with sudo privileges:

```bash
cd setup
sudo bash ./install.sh
```

The script will output the k0s kubeconfig user configurations to the console.

## Configuration

All configurations are defined in the `config.yaml` file.

### System

The `system` section contains system-level configurations, detailed below.

#### Users

**`system.users`** is an array of sudo users, each with the following fields:
- `name`: Username
- `sshkey`: Public SSH key

These users can only log in via SSH using their respective keys.

**Example `system.users` configuration:**
```yaml
system:
  users:
    - name: user1
      sshkey: "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA7..."
    - name: user2
      sshkey: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC..."
```

This configuration creates two sudo users, `user1` and `user2`, with their respective SSH keys.

#### Hostname

**`system.hostname`** specifies the hostname for the node.

**Example `system.hostname` configuration:**
```yaml
system:
  hostname: testhostname-control
```

This sets the node's hostname to `testhostname-control`.

#### SSH

The `system.ssh` section contains SSH settings, currently limited to the SSH port.

##### Port

**`system.ssh.port`** defines the port for SSH connections.

**Example `system.ssh.port` configuration:**
```yaml
system:
  ssh:
    port: 2202
```

With this configuration, SSH connections to the server must use port 2202, e.g.:
```bash
ssh user1@192.168.100.1 -p 2202
```