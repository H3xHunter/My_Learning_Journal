# LiveOverflow Binary Hacking
This is an enourmous course [available on youtube](https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN) about binary exploitation. From beginner to advanced. I personal thanks to the personbehind this course!


### [7-16-2018]  Reversing and Cracking first simple Program - bin 0x05
This is entirely base on the video [Reversing and Cracking first simple Program](https://www.youtube.com/watch?v=VroEiMOJPm8&t=2s)
  - check this [GDB Commands Reference](http://visualgdb.com/gdbreference/commands/)
  - Understand the [registers](https://github.com/H3xHunter/AssemblyJournal/blob/master/register.md)
  - Download [this repository](https://github.com/LiveOverflow/liveoverflow_youtube/tree/master/0x05_simple_crackme_intro_assembler) or use     ```git clone https://github.com/LiveOverflow/liveoverflow_youtube.git```
  - Change the gdb ```set disassembly-flavor intel```
  - use: ``` Disassembly main ```
  - Understand all the [jumps](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow), it is important to understand the flow of the program.
  - In an example: ```0x0000609 <+67> jne 0x400617``` the 617 is the jump address. 
  - Then, execute the program adding break points ```break *main```
    - you can also apply break points to the address like this ```break *0x0000000000400607 ```
  - Then, use ```run``` to run the program
  - With ```si```-step-in you can step inside function or ```ni``` to step-over
    - focus your attention to the instruction address number
    - if some message is printed out write a small note of that 
  - You can modify register value using ``` set $eax=0``` for example.
    - In this way you can skip checks. 
    - Another trick is to change a conditional jump to just jmp.
    
#### Summary:
After checking the jumps and have a good idea of the program structure, you can understand how the program works. Therefore, you can proceed to hardcode a value in the registry or change the check-conditions. Nb: because I checked other videos, I am well aware that this is not always the case or not that straight forward. But for now, it is enough for me to understand the basics how to crack small simple program like in the video. 
      
     
### [7-18-2018] Simple Tools and Techniques for Reversing a binary - bin 0x06
This is entirely base on the video [Reversing and Cracking first simple Program](https://www.youtube.com/watch?v=VroEiMOJPm8&t=2s)
- strings
   - ``` strings *fileName* | grep *fileName*```
- file
  - ```file  *fileName*```
- objdump
  - ```objdump -d -M intel *fileName* > dump.asm | grep j```
- hexdump
  - ``` hexdump -C *fileName* ```
- xxd
  - ``` xxd *fineName* | less ```
- radare2
  - ```r2 -d  *fileName* ```     

#### Radara2
Radare is an open source reversing framework. It comes with a ton of options, functionality, and a somewhat daunting learning curve. I primarily use it for CTF challenges, and I love that I can run it on a terminal along side GDB without requiring a GUI.
A full set of commands [here](https://github.com/radare/radare2/blob/master/doc/intro.md).
- ```
git clone github.com/radare/radare2.git
./sys/install.sh
```
Usage:
- ```
r2 -d *fileName*
   aaa - automaticaly analyze all
   afl - print all functions
   s main - change location
   pdf - print disassembly current fucntion
   VV or V! - visual mode
      - shift-tab           | change main tab
      - shift-r             | change theme
      - shift-s             | step over function
      - p change visual     |
      - ? help              |
      - arrows move around  |
      - :                   | input commands eg: dc

```
Basic workflow:
```
r2 -d *fileName*
  - aaa
  - s main
  - pdf
  - :
  - db <break point>
  - dc 
  - shift-s
```  
   
   
### [07/23/2018] The key generator: Uncrackable Programs? Key validation with Algorithm and creating a Keygen - Part 1/2 - bin 0x07 
In the second video, instead of hardcoding the value of the key the the author of the video produce a simple algorithm that sumup the ascii value to an int sum variable. The available solutions are always to patch the jump, but it is possible to code a keygenerator in python and bruteforce the solution or in this case the solutions, yes because there are multiple combinations that have the same value if summed up. 

   
### [07/24/2018] Smashing the stack: Smashing the Stack for Fun and Profit - setuid, ssh and exploit-exercises.com - bin 0x0B   
In [this](https://www.youtube.com/watch?v=Y-4WHf0of6Y&index=12&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN) video, liveoverflow introduce the challenge [protosstar](https://exploit-exercises.com/) 
- [Current issue : #49 | Release date : 1996-11-08 | Editor : daemon9](http://phrack.org/issues/49/14.html) 
</br>

``` 
Protostar introduces basic memory corruption issues such as buffer overflows, format strings and heap exploitation under “old-style” Linux system that does not have any form of modern exploit mitigiation systems enabled.
```
- Configure a vnet2 on vmware
- Configure kali eth0 or eth1 on auto dhcp

- Download the ISO
- Login: user/user
- activate bash: /bin/bash
- find the ip address of the machine: ip addr
- from Kali: ssh user@<ip protos VM>
  
From here the description of the exercise says:

```
This level introduces the concept that memory can be accessed outside of its allocated region, how the stack variables are laid out, and that modifying outside of the allocated memory can modify program execution.

This level is at /opt/protostar/bin/stack0
```

Stack0 is a file:
- file stack0 -> we find that the file is setuid ELF 32, What is it? 
- man setuid -> if something is a process is open to root privilege it drops it to the user privilege level
- open vim in another ssh-shell and let's find out our privileges
- ps -aux | grep vim -> we run it as user
- cd /opt/protostar/bin/; ./stack0 
- ps -aux | grep stack0 -> we notice it runs as root?? How?
- ls -la | grep stack0 -> rwsr-xr-x  x = every user can execure it, xr = every group, rwsr = read and write and set, when you run it , it runs with the root privileges. 
Let's find other examples:
- whereis sudo -> /usr/bin/sudo
- ls -la /usr/bin/sudo 

So, somehow if I can exploit this setuserid to exploit something like ping or sudo to attach an arbitrary code, I might find a solution. 
Without reading the solution I will read [this paper](https://www.blackhat.com/docs/us-15/materials/us-15-Xu-Ah-Universal-Android-Rooting-Is-Back-wp.pdf) and try to understand, if tomorrow I won't be able to find a solution I will check his solution. 
Should I do it in C or Python? maybe both?!
 
</br>
   
   
   
   
   
   
   
   
   
   
   
   
 ### Reference:
  -  [GDB Commands Reference](http://visualgdb.com/gdbreference/commands/)
      
