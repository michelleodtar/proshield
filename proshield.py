import subprocess
import os


class ProShield:
    def __init__(self):
        self.rules = [
            {
                "name": "Block All Inbound Connections",
                "command": "netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound"
            },
            {
                "name": "Enable Firewall Logging",
                "command": "netsh advfirewall set allprofiles logging filename %systemroot%\\system32\\LogFiles\\Firewall\\pfirewall.log"
            },
            {
                "name": "Set Logging Max Size",
                "command": "netsh advfirewall set allprofiles logging maxfilesize 16384"
            },
            {
                "name": "Enable Outbound Connections",
                "command": "netsh advfirewall set allprofiles firewallpolicy allowoutbound"
            }
        ]

    def apply_rule(self, rule):
        try:
            print(f"Applying rule: {rule['name']}")
            subprocess.run(rule['command'], check=True, shell=True)
            print(f"Successfully applied: {rule['name']}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to apply rule {rule['name']}: {e}")

    def enhance_firewall(self):
        for rule in self.rules:
            self.apply_rule(rule)

    def start(self):
        print("ProShield: Enhancing Windows Firewall settings...")
        self.enhance_firewall()
        print("ProShield: Firewall settings have been enhanced.")


if __name__ == "__main__":
    if os.name == 'nt':
        pro_shield = ProShield()
        pro_shield.start()
    else:
        print("ProShield is designed to run on Windows systems only.")