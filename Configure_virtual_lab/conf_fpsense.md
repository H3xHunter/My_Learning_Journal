## Steps:
#### In fpsense VM:
- Network adapters:
  - NAT
  - LAN segment
- follow the standrdard setup
#### In the linux machine:
 - Add LAN segment in the VMware setting
 - [configure the network interface file](https://lists.debian.org/debian-user/2014/02/msg01362.html):
 ```
   auto eth1
   allow-hotplug eth1
   iface eth1 inet dhcp
   ```
   - in wired setting:
     - ipv4: Automatic DHCP
 - go to: 192.168.1.1  admin/fpsense (change it)
  - system
    - Package Manager
      - Open-VM-Tools
    - update


## How to Fix "Wired Unmanaged" error in Debian or Kali Linux:
[How to Fix "Wired Unmanaged" ](https://www.youtube.com/watch?v=rZeeAQxTJUs)
