import subprocess
import os

debian_pkg_manager = "apt"
redhat_pkg_manager = "yum"

def run_command(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return output.decode("utf-8"), error.decode("utf-8"), process.returncode
    except Exception as e:
        return None, str(e), 1

def banner():
    print("Security Measures Checker Script")
    print("Created by w01f @ Pentest Sage\n")

def check_ssh_security():
    print("Checking SSH Security...")
    ssh_output, _, _ = run_command("sshd -T | grep -Eo '^(ciphers|macs|kexalgorithms).*'")
    if "aes128-ctr" in ssh_output and "sha2-256" in ssh_output and "curve25519-sha256@libssh.org" in ssh_output:
        print("SSH Security: Pass")
    else:
        print("SSH Security: Fail")

def check_sudo_user():
    print("Checking Sudo User Account...")
    user_output, _, _ = run_command("whoami")
    if user_output.strip() != "root":
        print("Sudo User Account: Pass")
    else:
        print("Sudo User Account: Fail")

def check_firewall():
    print("Checking Firewall...")
    firewall_output, _, _ = run_command("iptables -L")
    if "DROP" in firewall_output or "REJECT" in firewall_output:
        print("Firewall: Pass")
    else:
        print("Firewall: Fail")

def check_network_services():
    print("Checking Network Services...")
    services_output, _, _ = run_command("netstat -tuln")
    if "LISTEN" in services_output:
        print("Network Services: Pass")
    else:
        print("Network Services: Fail")

def check_fail2ban():
    print("Checking fail2ban...")
    fail2ban_output, _, _ = run_command("fail2ban-client status")
    if "Status: running" in fail2ban_output:
        print("fail2ban: Pass")
    else:
        print("fail2ban: Fail")

def check_selinux():
    print("Checking SELinux...")
    selinux_output, _, _ = run_command("sestatus")
    if "SELinux status: enabled" in selinux_output:
        print("SELinux: Pass")
    else:
        print("SELinux: Fail")

def check_kernel_updates():
    print("Checking Kernel Updates...")
    kernel_output, _, _ = run_command("uname -r")
    print(f"Kernel Version: {kernel_output.strip()}")
    print("Kernel Updates: Check manually")

def check_usb_thunderbolt():
    print("Checking USB and Thunderbolt Ports...")
    usb_output, _, _ = run_command("lsusb")
    thunderbolt_output, _, _ = run_command("lspci | grep -i thunderbolt")
    if usb_output:
        print("USB Ports: Pass")
    else:
        print("USB Ports: Fail")
    if thunderbolt_output:
        print("Thunderbolt Ports: Pass")
    else:
        print("Thunderbolt Ports: Fail")

def check_password_policies():
    print("Checking Password Policies...")
    password_policy_output, _, _ = run_command("cat /etc/security/pwquality.conf")
    if "minlen = 12" in password_policy_output and "minclass = 3" in password_policy_output:
        print("Password Policies: Pass")
    else:
        print("Password Policies: Fail")

def check_suid_guid_binaries():
    print("Checking SUID/SGID Binaries...")
    suid_guid_output, _, _ = run_command("find / -type f \\( -perm -4000 -o -perm -2000 \\)")
    if not suid_guid_output:
        print("SUID/SGID Binaries: Pass")
    else:
        print("SUID/SGID Binaries: Fail")

def check_logging_and_auditing():
    print("Checking Logging and Auditing...")
    auditd_output, _, _ = run_command("systemctl is-active auditd")
    syslog_output, _, _ = run_command("systemctl is-active rsyslog")
    if "active" in auditd_output and "active" in syslog_output:
        print("Logging and Auditing: Pass")
    else:
        print("Logging and Auditing: Fail")

def check_regular_backups():
    print("Checking Regular Backups...")
    backup_output, _, _ = run_command("find /backup -type d -mtime -7")
    if backup_output:
        print("Regular Backups: Pass")
    else:
        print("Regular Backups: Fail")

def check_listening_ports():
    print("Checking Listening Network Ports...")
    ports_output, _, _ = run_command("netstat -tuln")
    if "LISTEN" in ports_output:
        print("Listening Network Ports: Pass")
    else:
        print("Listening Network Ports: Fail")

def check_disk_partitions():
    print("Checking Disk Partitions...")
    partitions_output, _, _ = run_command("df -h")
    if "/tmp" in partitions_output and "/var" in partitions_output and "/home" in partitions_output:
        print("Disk Partitions: Pass")
    else:
        print("Disk Partitions: Fail")

def main():
    banner()

    check_ssh_security()

    check_sudo_user()

    check_firewall()

    check_network_services()

    check_fail2ban()

    check_selinux()

    check_kernel_updates()

    check_usb_thunderbolt()

    check_password_policies()

    check_suid_guid_binaries()

    check_logging_and_auditing()

    check_regular_backups()

    check_listening_ports()

    check_disk_partitions()

if __name__ == "__main__":
    main()
