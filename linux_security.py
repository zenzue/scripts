import subprocess

def display_banner():
    banner = """
    Linux Security Measures Checker
    Created by w01f @ Pentest Sage
    """
    print(banner)
    
def command_exists(command):
    try:
        subprocess.check_output(f"command -v {command}", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def print_pass(message):
    print(f"\033[92m[+] {message}: PASSED\033[0m")

def print_fail(message):
    print(f"\033[91m[-] {message}: FAILED\033[0m")

security_measures = [
    ("Secure Shell (SSH) Protocol", "ssh -V", "OpenSSH"),
    ("Dedicated Sudo User Account", "sudo -l", "User alias"),
    ("Basic Firewall (iptables)", "iptables --list", "Chain INPUT"),
    ("Disabled Unneeded Network Services", "systemctl list-units --type=service --state=active", "enabled"),
    ("Fail2ban Installed and Configured", "fail2ban-client status", "Status"),
    ("Security Enhanced Linux (SELinux)", "sestatus", "SELinux status"),
    ("Kernel and Software Updates", "sudo apt update && sudo apt list --upgradable", "upgradable"),
    ("Disabled USB and Thunderbolt Ports", "lsusb", "List of USB devices"),
    ("Strong Password Policies", "sudo grep '^password' /etc/security/pwquality.conf", "minlen"),
    ("Restrict Use of Previous Passwords", "grep 'remember' /etc/security/pwquality.conf", "remember"),
    ("Purged Unnecessary Packages", "dpkg -l", "Package"),
    ("Password Aging Configuration", "sudo grep '^PASS_MAX_DAYS' /etc/login.defs", "PASS_MAX_DAYS"),
    ("Disabled Unneeded SUID/SGID Binaries", "sudo find / -type f -perm /6000", "SUID/SGID binaries"),
    ("Logging and Auditing Configuration", "ls /var/log/", "Log files"),
    ("Regular Backups", "crontab -l", "Cron jobs"),
    ("Listening Network Ports", "netstat -tuln", "LISTEN"),
    ("Separate Disk Partitions", "df -h", "Mounted on")
]

display_banner()

for measure, command, expected_output in security_measures:
    if command_exists(command):
        print_pass(measure)
    else:
        print_fail(measure)
# Created by w01f @ Pentest Sage
