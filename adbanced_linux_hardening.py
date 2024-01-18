import os
import subprocess
import shutil

def clear_screen():
    os.system("clear")

def check_root():
    if not os.geteuid() == 0:
        print("Please run this script as root (sudo).")
        exit(1)

def update_packages():
    try:
        if os.path.isfile("/etc/redhat-release"):
            subprocess.run(["yum", "update", "-y"])
        elif os.path.isfile("/etc/debian_version"):
            subprocess.run(["apt", "update"])
            subprocess.run(["apt", "upgrade", "-y"])
            subprocess.run(["apt", "dist-upgrade", "-y"])
            subprocess.run(["apt", "autoremove", "-y"])
            subprocess.run(["apt", "clean"])
        print("System packages have been updated and upgraded.")
    except Exception as e:
        print(f"Error updating packages: {e}")

def configure_firewall():
    try:
        if os.path.isfile("/etc/redhat-release"):
            subprocess.run(["firewall-cmd", "--permanent", "--zone=public", "--add-service=https"])
            subprocess.run(["firewall-cmd", "--reload"])
        elif os.path.isfile("/etc/debian_version"):
            subprocess.run(["ufw", "enable"])
            subprocess.run(["ufw", "default", "deny"])
        print("Firewall has been enabled and configured.")
    except Exception as e:
        print(f"Error configuring firewall: {e}")

def secure_ssh():
    try:
        subprocess.run(["sed", "-i", 's/^PermitRootLogin yes$/PermitRootLogin no/', "/etc/ssh/sshd_config"])
        subprocess.run(["sed", "-i", 's/^PasswordAuthentication yes$/PasswordAuthentication no/', "/etc/ssh/sshd_config"])
        if os.path.isfile("/etc/redhat-release"):
            subprocess.run(["semanage", "port", "-a", "-t", "ssh_port_t", "-p", "tcp", "22"])
            subprocess.run(["setsebool", "-P", "ssh_can_connect", "1"])
        subprocess.run(["systemctl", "restart", "ssh"])
        print("SSH has been secured by disabling root login and password authentication.")
    except Exception as e:
        print(f"Error securing SSH: {e}")

def set_password_policy():
    try:
        if os.path.isfile("/etc/debian_version"):
            subprocess.run(["apt", "install", "-y", "libpam-pwquality"])
        subprocess.run(["authconfig", "--passalgo=sha512", "--update"])
        subprocess.run(["sed", "-i", '/password\s*requisite\s*pam_pwquality.so/c password requisite pam_pwquality.so retry=3 minlen=14 lcredit=-1 ucredit=-1 dcredit=-1 ocredit=-1 enforce_for_root', "/etc/security/pwquality.conf"])
        print("Password policy has been set to require strong passwords.")
    except Exception as e:
        print(f"Error setting password policy: {e}")

def restrict_su_access():
    try:
        subprocess.run(["chmod", "go-x", "/bin/su"])
        subprocess.run(["chmod", "go-x", "/usr/bin/su"])
        print("Access to 'su' has been restricted.")
    except Exception as e:
        print(f"Error restricting 'su' access: {e}")

def enable_auditing():
    try:
        if os.path.isfile("/etc/debian_version"):
            subprocess.run(["apt", "install", "-y", "auditd"])
        subprocess.run(["systemctl", "enable", "auditd"])
        subprocess.run(["systemctl", "start", "auditd"])
        print("Auditing has been enabled.")
    except Exception as e:
        print(f"Error enabling auditing: {e}")

def main():
    check_root()
    clear_screen()
    print("Advanced Linux Hardening Script by w01f")
    while True:
        print("\nOptions:")
        print("1. Update System Packages")
        print("2. Configure Firewall")
        print("3. Secure SSH")
        print("4. Set Password Policy")
        print("5. Restrict 'su' Access")
        print("6. Enable Auditing")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            update_packages()
        elif choice == "2":
            configure_firewall()
        elif choice == "3":
            secure_ssh()
        elif choice == "4":
            set_password_policy()
        elif choice == "5":
            restrict_su_access()
        elif choice == "6":
            enable_auditing()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
# if u r using as a test make sure run in vm or sandbox
