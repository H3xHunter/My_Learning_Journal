# Update** 2020 blog continues [here](https://github.com/H3xFiles/malwareanalysis_journal/blob/master/february2020.md)

# Captain's Log, stardate 3E2252

For few years I have been interested in cybersecurity, but lately I decided to go more into the reverse engineering and malware analysis. I am trying to follow [how to learn anything of Josh Kaufman](https://www.youtube.com/watch?v=5MgBikgcWnY). During my late night youtube zapping, I found this video from the DEFCON18 with the title [My life as spyware developer](https://www.youtube.com/watch?v=k2mdUcOXW6I). 

##### The journal is based on the idea of gamification, the contenent is serious, but I am not. At the end of each day I have a treasure chest where I add all the links I do believe interesting like when you play MMORPG.(for the horde!!) The content of the chest is usually related to security, but not fit in the scope of this journal.<u> But beware that this journal or any other of my journals should be considered as a guide of any sort (maybe spiritual if you really need it) </u>.

<hr>

### Fast links to my notes:
- [Guide to configure a simple VM LAB](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_virtual_lab.md)
- [Introduction to malware analysis: basic analysis](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/reverse_eng.md)
- [CYBRARY-malware_analysis-module](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/tree/master/Notes/cybrary_courses/malware_analysis_reverse_engineering)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45">  07/04/2018 - THE BEGINNING
- [x] [Reversing and Cracking first simple Program](https://www.youtube.com/watch?v=VroEiMOJPm8) 
 - [x] [MMORPG Bot Reverse Engineering and Tracking](https://www.youtube.com/watch?v=irhcfHBkfe0)
 - [x]  [Reverse-Engineering — Crack / Patch Program 1](https://www.youtube.com/watch?v=3d5Ler_8cHg)
- [x]  [Reverse-Engineering — Crack / Patch Program 2](https://www.youtube.com/watch?v=wq6fk5oDbVg)
 - [x]  [C++ Game Hacking Tutorial Ep.1 Reading/Writing Memory](https://www.youtube.com/watch?v=zFUHrg-wdmo)
- [x]  [How to Reverse Engineer Software and Create Keygen](https://www.youtube.com/watch?v=3D5FOPOkE5Y)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/05/2018 - SEEMS A SLOW DAY
- [x] [Introduction to Malware Analysis](https://www.youtube.com/watch?v=D4pc63SeHxI)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/06/2018 - DOUBLING DOWN ON THINGS DONE FOR THE DAY
- [x] [Setup virtual enviroment](https://fumalwareanalysis.blogspot.com/2011/08/malware-analysis-tutorial-reverse.html)

* Several problems encountered trying to export this VM to another computer.
* VirtualBox is having massive issue with the host-only on a specific machine I have.
* It is a very long and annoying process.
* [To solve host-only issue of virtualbox I am converting my VM into an ova and using it on Vmware.](https://www.howtogeek.com/125640/how-to-convert-virtual-machines-between-virtualbox-and-vmware/)

- [x] [Hex Editing - Introduction](https://www.youtube.com/watch?v=s58tqRiJqaw)
- [x] [HEX editing to bypass AntiVirus](https://www.youtube.com/watch?v=tESLASgC4fE)
- [x] [Modifying Compiled C Programs in Hex Editors](https://www.youtube.com/watch?v=UCJmPppNB58)
- [x] [Disguising Payload EXE Files as JPG Picture Files (or any extension) using WinRAR 4.2 Exploit](https://www.youtube.com/watch?v=ARRI4ZVHz5E)

#### Some extra fun for the day:
- [x] [Hiding JavaScript in Picture Files for XSS](https://www.youtube.com/watch?v=memPcI94YGA)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/07/2018 - VERY THEORETICAL DAY INIT
Currently watching more videos about the foundamentals rather than straight into the malware analysis courses. I want to become pretty good with gdb.
- [x] [Malware Theory - Basic Structure of PE Files](https://www.youtube.com/watch?v=l6GjU8fm8sM&list=PLynb9SXC4yETaQYYBSg696V77Ku8TOM8-)
- [x] [Syscalls, Kernel vs. User Mode and Linux Kernel Source Code - bin 0x09
](https://www.youtube.com/watch?v=fLS99zJDHOc)
- [ ] [LiveOverflow Binary Hacking](https://youtu.be/iyAyN3GFM7A)

#### NEW material found!
* https://microcorruption.com/login

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/08/2018 - VM PROBLEMS ARE IN THE AIR
The biggest problem now is the VM and the computer, I don't have a computer capable of running a VM in a smooth way and still having problem with virtualbox. 
- [x] [zeltser.com/malware-analysis-webcast/](https://zeltser.com/malware-analysis-webcast/)
- [x] [Obfuscation](https://www.youtube.com/watch?v=FC7wt6mJsKw)
- [ ] [Learn memory dump analysis](https://www.youtube.com/watch?v=-8f8avZ2V7s)

#### small project of the day
- [Spoof DNS on a LAN to Redirect Traffic to Your Fake Website](https://null-byte.wonderhowto.com/how-to/hack-like-pro-spoof-dns-lan-redirect-traffic-your-fake-website-0151620/)


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/09/2018 - JUMPING THE FENCE, C HERE I COME
Today I focus more on programming in C after watching couple of videos that inspired me. I am currently working on a small crack.me program to give to my good friend to test him and test me. 
- [x] [Key validation with Algorithm and creating a Keygen](https://www.youtube.com/watch?v=qS4VWL5R_OM&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=8) - this video inspired me to write my crack.me program that I am currently developing in C.
- [x] [DEFCON 18: Trolling Reverse Engineers with Math: Ness It hurts](https://www.youtube.com/watch?v=OqFVzkuorAA&t=1s)

- [x] [DEF CON 17 Obfuscation Top-down approach By Sean Taylor](https://www.youtube.com/watch?v=WV6pHQxKSk0)

- [ ] [HEAP EXPLOITATION - SAFE UNLINK EXPLANATION](https://de-me.org/videos/video-LgpWja_zDh8.html) - Interesting video but very long.

- [The International Obfuscated C Code Contest](https://www.ioccc.org/)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/10/2018 - THEORY DAY 02 STRIKE BACK
Yesterday I finished the crackme program, with some finishing touch. 
- [ ] [HACKCONCTF STARTED FROM THE BOTTOM](https://de-me.org/videos/hackconctf-started-from-the-bottom-Z1eV-1fWwK0.html) - need to see it tonight
- [ ] [Pwnable.kr](http://pwnable.kr/index.php) - not explored yet
- [x] [Malware Obfuscation](https://www.youtube.com/watch?v=FC7wt6mJsKw)
- [x] [Offensive Computer Security 2014 - Lecture 10 (Part 1 Advanced Fuzzing Topics)](https://www.youtube.com/watch?v=kWmyGZsFc2c) - interesting but a little bit too far from my personal objective of this month.
- [x] Create a page about [Tainted analysis](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Notes/taintanalysis.md)
- [x] Create a page about [type of viruses](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Notes/viruses.md)
- Trying to solve level: Sydney in microcorruption
 
### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/11/2018 - MADNESS FROM THE CABLES(LESS)
Start with the [CYBRARY videos](https://www.cybrary.it/course/malware-analysis/) about malware analysis. 
- [Note1: Introduction](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Notes/cybrary_courses/malware_analysis_reverse_engineering/CYBRARY-malware_analysis-module_1.md)
- [Note2: Setup VM](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Notes/cybrary_courses/malware_analysis_reverse_engineering/CYBRARY-malware_analysis-module_2.md)
#### notes:
- autoconfig VM to automatize installing of softwares and config

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/12/2018 - NO SERIOUSLY WHAT I DID TODAY?!?
Keep going with [malware analysis course](https://www.cybrary.it/course/malware-analysis/).
And setting up the 2 VM.
- Thinking about to opening a hackLab on my boat, it is the most Dutch thing i can think of. 
   - Retrieve my old computer 
   - Find people to join it

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 07/13/2018 - WHOOO PRODUCTIVE DAY I FEEL IT!
The issue are not resolved yet, seems quite hard to find clear material how to do it. Even if it is pretty simple in theory seems not so much in practice, I assume the number of multiple configuration provide a certain degree of variability among all the possible solutions to this challenge. So, currently I did not have time to continue with the microcontroller CTF game or anything else. :(
- [x] [Getting Started Analyzing Malware Infections](https://app.pluralsight.com/library/courses/analyzing-malware-infections-getting-started) - too simple. 
- [x] [Create Virtual Pen Test Lab with VMware Workstation](https://www.youtube.com/watch?v=DqfpyMIIImE)
- [Vulnhub](https://www.vulnhub.com/) provide materials that allows anyone to gain practical 'hands-on' experience in digital security, computer software & network administration. 
- [Ifconfig: 7 Examples To Configure Network Interface](https://www.thegeekstuff.com/2009/03/ifconfig-7-examples-to-configure-network-interface)
- [Linux ifconfig command](https://www.computerhope.com/unix/uifconfi.htm)
- <img src="https://orig07.deviantart.net/7628/f/2014/004/f/0/fool_emoji_11__hurray_for_you_and_me___v1__by_jerikuto-d6x6ikf.gif" width="50" height="45"> FOUND A SOLUTION: [Enabling File and Printer sharing checkbox solved my issue.](https://social.msdn.microsoft.com/Forums/azure/en-US/ad5db362-52cf-4b6b-8f53-e31bcf367ea1/virtual-machines-cannot-ping-each-other-within-same-virtual-network?forum=WAVirtualMachinesVirtualNetwork)
- Wrote a small guide how to [setup a VM](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_virtual_lab.md)
- [NetworkConfigurationCommandLine](https://help.ubuntu.com/community/NetworkConfigurationCommandLine)

</br>
Now I need to simulate the internet services with <a href="http://www.inetsim.org/documentation.html">Inetsim</a> a current problem is inetsim does not render any page, so I am not sure it is working properly. 

- [Set up your own malware analysis lab with VirtualBox, INetSim and Burp](https://blog.christophetd.fr/malware-analysis-lab-with-virtualbox-inetsim-and-burp/#INetSim)

-  Several inetsim tutorials like this one [How to Create a Malware Analysis Lab - VirtualBox](https://www.youtube.com/watch?v=proAnW3TvSs) show that you need inetsim and [fakeDNS](https://github.com/REMnux/distro), but it seems that the new version of inetsim do not need the extra fakeDNS script. And as suspected the problem was in the config file: [This video does the trick](https://www.youtube.com/watch?v=BGhZ0o0s7eM&t=656s) at 2:15 I can finally go to rest! 

Line added to the config file:
``` 
  service_bind_address <ip linux machine>
```
```
  dns_default_ip <ip linux machine>
```

#### treasures of the day aaar!
- [ ] [Real-world Decompilation with IDA Pro - Part 1: Introduction
](https://www.youtube.com/watch?v=vb18UVF4a_o)
- [ ] [The Internet's Own Boy: The Story of Aaron Swartz](https://youtu.be/M85UvH0TRPc)


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/14/2018 - Saturday be like!

- [ ] write a small guide how to virtualize entire OS (maybe I can analyze an entire OS?!? <img src="http://gifimage.net/wp-content/uploads/2017/07/dr-evil-laugh-gif-1.gif" width="80" height="50">)
   - [Convert your existing Windows System into a Virtual Machine](https://www.youtube.com/watch?v=cF8GtaEXZc4)
   - [How to convert a physical PC into a Virtual Machine](https://www.youtube.com/watch?v=Hl7Dkb6Ajvo)
   - [Converting a physical machine into a virtual machine using Converter Standalone](https://www.youtube.com/watch?v=M2vSRXZBlFU)
   
- [x] Adding a router to my lab setup
  - [Sophos](https://www.sophos.com/en-us/products/free-tools/sophos-utm-home-edition.aspx)?
  - ClearOS?
  - [Simplewall](http://www.simplewallsoftware.com/simplewall-sophos-clearos/)?
  - pfsense?
  - [opnsense](https://opnsense.org/)
  
 - [The Hunt For the Ultimate Free Open Source Firewall Distro](https://www.mondaiji.com/blog/other/it/10175-the-hunt-for-the-ultimate-free-open-source-firewall-distro)
 - [distrowatch%s=firewall](https://distrowatch.com/search.php?ostype=All&category=Firewall&origin=All&basedon=All&notbasedon=None&desktop=WebUI&architecture=All&package=All&rolling=All&isosize=All&netinstall=All&language=All&defaultinit=All&status=Active#simple)

#### treasures of the day aaar!
- [ ] [Shenzhen: The Silicon Valley of Hardware (Full Documentary)](https://www.youtube.com/watch?v=SGJ5cZnoodY)
- [ ] [Where Cybercrime Goes to Hide](https://www.youtube.com/watch?v=CashAq5RToM)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/15/2018 - Sunday!
fpsense is up and running in the VM, I used these videos:  
- [How to install pfsense on a virtual machine in vmware workstation](https://www.youtube.com/watch?v=6HYEvSylk1E)
- [Installing PFSense as a router for our lab](https://www.youtube.com/watch?v=A_n4TdwTUC4)
- [pfsense Firewall Setup and Features in Depth Version 2.4](https://www.youtube.com/watch?v=RrQrt8r_uYg&t=1624s)
- [How To Setup OpenVPN For Remote Access On pfsense](https://www.youtube.com/watch?v=7rQ-Tgt3L18)
- wrote this [fpsense Setup guide](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_fpsense.md)

Time for an IDS ....
[Setting up Snort On pfsense](https://www.youtube.com/watch?v=-GgqYq5-EBg)
  
#### treasures of the day aaar!
 Keyword of the day: [OSINT](https://inteltechniques.com/podcast.html).
 - http://liveoverflow.com/binary_hacking/reverse_engineering.html
 - http://asecuritysite.com/subjects/

    
### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/16/2018 - Monday back to MWA.

After a small deviation in networking and VM, today I back on MWA, I am going to rewatch watch what I think so are the 2 most important series of videos I found in this journey so far:
- [Reversing and Cracking first simple Program - bin 0x05](https://www.youtube.com/watch?v=VroEiMOJPm8&t=2s)
- [Introduction to Malware Analysis](https://www.youtube.com/watch?v=_Mz8Pu-4WVw) or in general all his [videos](https://www.youtube.com/user/billatnapier/search?query[=malwa]re) on the topic

In this week I wondered around the topic, setup the VM and got to know the tools now, It's time to take some serious notes about reversing engineering too. So, [here my reverse engineering notes](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/reverse_eng.md).

This video is in my [x86_64 journal](https://github.com/H3xHunter/AssemblyJournal), but I do believe I really need to watch it again.
- [ ] [x86 Assembly Crash Course](https://www.youtube.com/watch?v=75gBFiFtAb8)
  
Today I have lootted so many links!!! 
#### treasures of the day aaar!
  - [GDB Command Reference](http://visualgdb.com/gdbreference/commands/)
  - [Simple reversing challenge and gaming the system - BruCON CTF part 1](https://www.youtube.com/watch?time_continue=380&v=bqaZBeZ4zf0)
  - [Deobfuscating xor’ed strings](http://www.hexblog.com/?cat=3)
  - [Wiki-like CTF write-ups repository](https://github.com/ctfs)
  - [MatesCTF Final 2017](https://www.youtube.com/watch?v=zSD00S44dNY&list=PLO1bkZvP08LZtXqlzq3fho1QkCU1O6JXJ)
  - [Practice CTF List ](http://captf.com/practice-ctf/)
  - [Reverse engineering the HITB binary 100 CTF challenge](https://cedricvb.be/)
  - [CTF Field Guide](https://trailofbits.github.io/ctf/) 
  - [skullsecurity.org/Assembly](https://wiki.skullsecurity.org/Assembly)
  - [skullsecurity.org/Category Archives: Reverse Engineering](https://blog.skullsecurity.org/category/reverse_engineering)
  - [An Introduction To CTFs](https://hackmy.world/projects/tutorial.php#assembly)
  - [CTF-Workshop](https://github.com/kablaa/CTF-Workshop)
  - [Smashing the Stack for Fun & Profit : Revived]( https://avicoder.me/2016/02/01/smashsatck-revived/)
  - [CTF Series : Binary Exploitation](https://bitvijays.github.io/LFC-BinaryExploitation.html#)
  - [Getting Practice at Binary CTF Problems](http://fuzyll.com/2017/getting-practice-at-binary-ctf-problems/)
  - [Archive for the ‘Binary Exploitation’ Category BLOG EUPHORIA](https://shankaraman.wordpress.com/category/ctf/binary-exploitation/)
  - [trapkit.de/books/index.html](http://www.trapkit.de/books/index.html)
  - [https://www.hackthis.co.uk/](https://www.hackthis.co.uk/)
  - [Exploit writing tutorial part 1 : Stack Based Overflows CORELEAN TEAM](https://www.corelan.be/index.php/2009/07/19/exploit-writing-tutorial-part-1-stack-based-overflows/)
  - [CNIT 127: Exploit Development](https://samsclass.info/127/127_F15.shtml#lecture) || Massive!
  - [Windows Exploit Development – Part 1: The Basics](https://www.securitysift.com/windows-exploit-development-part-1-basics/)
  - [beginner to exploit a simple vulnerability on modern Windows](http://0xdabbad00.com/2012/12/09/hurdles-for-a-beginner-to-exploit-a-simple-vulnerability-on-modern-windows/)
  - [Binary-Reading-List](https://github.com/firmianay/Binary-Reading-List) 
  - [Jumping into exploit development](https://sneakerhax.com/jumping-into-exploit-development/)
  - [University of Genova Introduction to reverse engineering and exploitation of binary programs](http://csec.it/events/phd-course-binaries/)
  - [manoharvanga.com/hackme](http://manoharvanga.com/hackme/)
  - [Reversing ELF 64-bit LSB executable, x86-64 ,gdb](https://reverseengineering.stackexchange.com/questions/3815/reversing-elf-64-bit-lsb-executable-x86-64-gdb)
  - [fuzzysecurity Tutorials » Introduction to Exploit Development](http://www.fuzzysecurity.com/tutorials/expDev/1.html)
  - [The best resources for learning exploit development](http://www.pentest.guru/index.php/2016/01/28/best-books-tutorials-and-courses-to-learn-about-exploit-development/) || Soooooo .... many links!


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/17/2018 - Tuesday chill.
Keep working on the basics [reverse engineering notes](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/reverse_eng.md).
- [x] [ObjDump Static Analysis](https://www.youtube.com/watch?v=x5GtjqmdIeM)
- [x] [Simple Tools and Techniques for Reversing a binary - bin 0x06](https://www.youtube.com/watch?v=3NTXFUxcKPc)
From yesterday i am reading [https://hackmy.world/projects/tutorial.php#assembly](https://hackmy.world/projects/tutorial.php#assembly), [Assembly Language Tutorial](https://wiki.skullsecurity.org/index.php?title=Fundamentals)

#### Basic linux tools:
- gdb
- objdump ```objdump -d -M intel <input file name> > dump.asm```
- file    ```file a.out```
- strings ```strings | grep somethng```

#### P.e.d.a
- [Python Exploit Development Assistance for GDB](https://github.com/longld/peda)
- [Linux Interactive Exploit Development
with GDB and PEDA](http://ropshell.com/peda/Linux_Interactive_Exploit_Development_with_GDB_and_PEDA_Slides.pdf)

#### Installation
```
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
```

#### treasures of the day aaar!
- [STACK OVERFLOWS - PRIMER](https://free.codebashing.com/free-content/cplus/c_stack_p1#/lesson/stack%20overflows/objectives?_k=hqlzvq) || the best interactive buffer overflow explanation ever period.
- Find a book titled "Reversing: Secrets of Reverse Engineering"
- [twitch channel finding 0-day live](https://www.twitch.tv/zerotozeroday)
- [chat #zerotozeroday](https://discordapp.com/channels/460225038927527937/460225039468462081)
- [Using IDAPython to Make Your Life Easier: Part 1](https://researchcenter.paloaltonetworks.com/2015/12/using-idapython-to-make-your-life-easier-part-1/)


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/17/2018 - Into the byte.

- [x] explore rexmux -  not impressed
- [x] explore Flare VM - 
- [x] finish episode 0x06 and 0x07 

- continuing to write the [introduction to malware analysis: basic analysis](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/reverse_eng.md)


#### treasures of the day aaar!
- [R4ndom’s Beginning Reverse Engineering Tutorials - Ollydbg](https://legend.octopuslabs.io/sample-page.html)
- [REcon](https://recon.cx/2015/archive.html) 
  - REcon is a computer security conference held annually in Montreal, Canada. It offers a single track of presentations over the span of three days with a focus on reverse engineering and advanced exploitation techniques.
- [A curated list of awesome reversing resources](https://github.com/wtsxDev/reverse-engineering)


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/18/2018 - ELFs are dorky, Elves are cool
It's 1:21 in the morning and my cup is filled with warm coffee. Let's start the day with [Boxstarter](https://boxstarter.org/), that it is actually something I was looking for and I randomly found it, because I checked the an address on the page of Flare VM. This is what is actually is: </br>
```Repeatable, reboot resilient windows environment installations made easy using Chocolatey packages. When its time to repave either bare metal or virtualized instances, locally or on a remote machine, Boxstarter can automate both trivial and highly complex installations. You can use Boxstarter to install a complete environment or install a small set of tools and windows settings with absolutely no software pre installed and configuration scripts stored in a gist.```
</br>
 <img src="https://nostarch.com/sites/default/files/styles/uc_product_full/public/GTFO_cover_new.png" width="300" height="450" align="right"> 

Sometime later on tonight ... I found this book "PoC or GTFO By Manul Laphroaig", it is a strange book, it is technical, but feel different from the rest, I felt more like I found a dusty book forgotten in a corner of some library.
[hackaday.com](https://hackaday.com/2017/08/14/bibles-you-should-read-poc-gtfo/) calls it a bible.
``` "For the last few years, Pastor Manul Laphroaig and friends have been publishing the International Journal of PoC || GTFO. This is a collection of papers and exploits, submitted to the Tract Association of PoC || GTFO, each of which demonstrates an interesting exploit, technique, or software toy in the field of electronics. Imagine, if 2600 or Dr. Dobb’s Journal were a professional academic publication. Add some whiskey and you have PoC || GTFO." ``` </br>
But if you do not want to spend 30$ the journal entries are publically available to be read online here: [International Journal of Proof-of-Concept or Get The Fuck Out (PoC||GTFO or PoC or GTFO)
](https://www.alchemistowl.org/pocorgtfo/) or buy [the bible](https://nostarch.com/gtfo) 
</br> 
But let's rollback a second,before I found that book because I was watching [ Finding a Parser Differential in loading ELF](https://www.youtube.com/watch?v=OZvc-c1OLnM&t=0s&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=10). 
Basically the idea is flipping a bit you might confuse the debugger/disassembler to not recognize the file,but it does not always work. 
- [ ] find more material on Parser Differential (Me the next morning: check for fuzzing old me)
</br>
After few (interstellar) jumps I came to the conclusion that I need to understand better what is fuzzing.</br>
 What is fuzzing? Acrroding to Urban dictionary ... I am confused ... 

- ```Fuzzing verb.  Fuzzing is caused by the lack of blood flow in a particular area thereby producing a vibrating sensation. Fuzzing is most common on the face and hands and may cause light-headiness. Common causes of Fuzzing may be alcohol, a weed-induced high or a rush of adrenaline.```

mmm, Urban dictionary might be not a techinical source of information ... , noted. </br> 
So, I searched a little bit more, and I found this explanation 
- ```Fuzzing is a powerful strategy to find bugs in software. The idea is quite simple: Generate a large number of randomly malformed inputs for a software to parse and see what happens. If the program crashes then something is likely wrong. While fuzzing is a well-known strategy, it is surprisingly easy to find bugs, often with security implications, in widely used software. Memory access errors are the errors most likely to be exposed when fuzzing software that is written in C/C++. While they differ in the details (stack overflow, heap overflow, use after free, ...), the core problem is often the same: A software reads or writes to wrong memory locations.```

Then, I found this tutorial [Tutorial - Beginner's Guide to Fuzzing](https://fuzzing-project.org/tutorial1.html) and of course could not miss the [awesome fuzzy list](https://github.com/secfigo/Awesome-Fuzzing), there is an awesome list for anything. The material is really a lot online, even a nice [coursera video](https://www.coursera.org/lecture/software-security/fuzzing-VgyOn). But, because I do prefer short guide here a [15 minute guide to fuzzing](https://www.mwrinfosecurity.com/our-thinking/15-minute-guide-to-fuzzing/)

But the best part of tonight was here to come, while I was searching fuzzing a totally random journal came to my attention.
<a href="https://books.google.nl/books?id=RNoRAAAAYAAJ&lpg=PA632&ots=drUd_ONV0n&dq=fuzzling%20the%20elf%20file&pg=PA632&ci=38%2C22%2C947%2C229&source=bookclip"><img src="https://books.google.nl/books/content?id=RNoRAAAAYAAJ&pg=PA632&img=1&zoom=3&hl=en&sig=ACfU3U0c8pWkhQsuiMczMWwxjzaErTGCQg&ci=38%2C22%2C947%2C229&edge=0"/></a></br>
So, I digged a little bit and here is what I found out:
</br>
```The Gentleman's Magazine was founded in London, England, by Edward Cave in January 1731. It ran uninterrupted for almost 200 years, until 1922.``` </br>And the piece of that journal that came to my attention date Dec 31, 1737 Publisher F. Jefferies. This is what I call net-treasure hunting. 

Almost 3:00 AM, time almost to go to bed after reading the 15 min guide to fuzzing. ( I hope it takes less)
</br>
4:30 in the afternoon, my brain is still tired from last night, today I am going to focus on reading the first article 
- [x] [International Journal of PoC k GTFO
Issue 0x00, ](https://www.alchemistowl.org/pocorgtfo/pocorgtfo00.pdf)

</br>

``` I met a professor of arcane degree
  Who said: Two vast and handwritten parsers
  Live in the wild. Near them, in the dark
  Half sunk, a shattering exploit lies, whose frown,
  And wrinkled lip, and sneer of cold command,
  Tell that its sculptor well those papers read
  Which yet survive, stamped on these lifeless things,
  The hand that mocked them and the student that fed:
  And on the terminal these words appear:
  "My name is Turing, wrecker of proofs:
  Parse this unambigously, ye machine, and despair!"
  Nothing besides is possible. Round the decay
  Of that colossal wreck, boundless and bare
  The lone and level root shells fork away.
    -- Inspired by Edward Shelley 

```

#### treasures of the day aaar!
- https://www.nuget.org/
- Once Upon an Algorithm: How Stories Explain Computing


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7-20-2018 Friday
</br> 

In these two days I focused on fuzzing and the theory of differential debugging. Few points that I want to focus on is static analysis and to do that I want to read the assembly64 book.
- [ ] need to find some project to play with the syscall in python and in C
</br>
TODO:
- start to read this[this book ](http://www.egr.unlv.edu/~ed/assembly64.pdf) this evening
- read [this tutorial about fuzzing](https://fuzzing-project.org/tutorial1.html) this afternoon
- watch the next video of the serie of liveoverflow

Extra material:
- http://crypto.stanford.edu/~dabo/cs255/syllabus.html
- https://crypto.stanford.edu/cs155/syllabus.html
- [VIM shortcuts](https://vim.rtorr.com/)

</br>
Because my license of Vmware pro is about to end, I need to migrate to virtualBox, so today I had to watch [this video](https://www.youtube.com/watch?v=D2wjR3pCwrU) to configure virtualBox with pfsense and windows.
Another important point is that I want to have a solid configuration, and know how to move around installing and reinstalling at will without problems. So, I am focusing on what I is the basics of having a malwarelab and it is to have an enviroment that you can mess up millions times and in few click start again. 

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7-21-2018 Saturaday
I just realized I wrote three differen guides on pfsense:
- [This is the most schematic](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_pfsense_win10_linux.md)
- [This is with a lot of pictures](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_virtual_lab.md)
- [This contains a the solution for an error-network on kali](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/blob/master/Configure_virtual_lab/conf_fpsense.md)


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7-23-2018 After the accident
Unfortunately I had a minor accident and I could standup from the bed, but today I am back. 

- [x] [Smashing the Stack for Fun and Profit - setuid, ssh and exploit-exercises.com - bin 0x0B](https://www.youtube.com/watch?v=Y-4WHf0of6Y&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=12)
</br> 
I am currently exploring new technologies and opensource projects:
I am very excited about XIA, because it was something I was thinking about the importance of developing a new network protocol to replace TCP/IP. And then at 3AM in a total random search on google I found this:

```
Finding the successor of TCP/IP is the ultimate goal of our project. To do so, we have developed a new protocol stack, XIA. To reach this destination, we are both refining our codebase and working to meet unfulfilled demands of real-world networks. For example, our current short-term goal is to develop a DDoS protection system.
```

I am really want to try to cooperate or to play with XIA and see what is it, what can be done, and what I can help with.
### XIA-Linux
- https://github.com/mengxiang0811/gatekeeper  
- http://cs-people.bu.edu/qiaobinf/
- [Randomized Heavy Hitter Hierarchy Management](https://github.com/shalmonir/RHHH_Project)
- [Implementing blackholing in Gatekeeper](https://groups.google.com/forum/#!topic/linux-xia/5Y77yJ9DRk0)
- [Finding frequent items in data streams Presenter: Qiaobin Fu](https://drive.google.com/file/d/0B5ratrMov51eQ0JURVVLRlN6MWM/view)
- [XIA for Linux](https://github.com/AltraMayor/XIA-for-Linux)

Because I was already there I checked other opensource projects and I was super excited to find this projects too, very close to my interests as well. 
</br>
### The Honeynet Project
- [DRAKVUF: Support for Dynamic Malware Analysis on ARM](https://summerofcode.withgoogle.com/projects/#6677811633324032)
- [drakvuf-dynamic-malware-analysis](https://www.xenproject.org/directory/directory/products/237-drakvuf-dynamic-malware-analysis.html)
- [Sergej Proskurin, Tamás K. Lengyel – Stealthy, Hypervisor-based Malware Analysis](https://www.youtube.com/watch?v=86EvJK2Ef_U)
- [CONFidence 2017: Escaping the (sand)box (Robert Swiecki)](https://www.youtube.com/watch?v=gJpaxisyQfY)

Other interesting projects found there to follow up.
</br>
### Other Opensource projects
- [RTEMS is a real-time operating system kernel used around the world and in space.](https://summerofcode.withgoogle.com/organizations/5315176019001344/)
- [Open Source Robotics Foundation, Inc.](https://summerofcode.withgoogle.com/organizations/5366449791565824/)

#### The Captain's treasure chest "Arrr!"
- [The Strange Disappearance of D.B. Cooper](https://www.youtube.com/watch?v=oHSehKtDyoI)
- [Yet another universal Android root!](https://www.blackhat.com/docs/us-15/materials/us-15-Xu-Ah-Universal-Android-Rooting-Is-Back-wp.pdf)
- [Writing, Running, and Fixing Code in C](https://www.coursera.org/learn/writing-running-fixing-code/home/welcome)
- [Embedded-C-Coding-Standard](https://barrgroup.com/Embedded-Systems/Books/Embedded-C-Coding-Standard)


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/24/2018 - Tuesday chill.

- [x] [Own your Android! Yet Another Universal Root](https://www.blackhat.com/docs/us-15/materials/us-15-Xu-Ah-Universal-Android-Rooting-Is-Back-wp.pdf)
- [ ] [Read the next POCORGTFO](https://www.alchemistowl.org/pocorgtfo/pocorgtfo01.pdf)
- [ ] [The Basics and Pitfalls of Pointers in C](https://hackaday.com/2018/04/04/the-basics-and-pitfalls-of-pointers-in-c/) 
- [ ] [When 4 + 1 Equals 8: An Advanced Take On Pointers In C](https://hackaday.com/2018/04/19/when-4-1-equals-8-an-advanced-take-on-pointers-in-c/)
- [ ] Working on [protostar challenge](https://github.com/H3xHunter/PedanticMalwareAnalysisJournal/edit/master/reverse_eng.md)

#### The Captain's treasure chest "Arrr!"
- [How to Protect Your Privacy on The Web](https://www.fortinet.com/blog/threat-research/i-still-know-what-you-did-last-summer-how-to-protect-your-privacy-on-the-web.html)
- [Current issue : #49 | Release date : 1996-11-08 | Editor : daemon9](http://phrack.org/issues/49/14.html) 
- HighOn.Coffee 
- rot.fi

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 7/25/2018 - Carbon Black Training - CB Response Advanced Analyst
Today I will be busy almost all day long due to an online training.
- [CB Response Advanced Analyst Syllabus](https://learning.cbtechnicalacademy.com/pluginfile.php/2858/mod_resource/content/1/Cb%20Response%20Advanced%20Analyst%20Syllabus.pdf)



### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 08/11/2018
Few new links, [Complete Ethical Hacking Course](https://www.youtube.com/watch?v=tHd8k54kVs8&list=PLBf0hzazHTGOEuhPQSnq-Ej8jRyXxfYvl) on youtube and [Metasploit For Beginners](https://www.youtube.com/watch?v=6SNHuWaLuhU) and [How to Create Your First Exploi](https://www.youtube.com/watch?v=U2mpUQTWRhI)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 11/11/2018
There is [this](https://rinseandrepeatanalysis.blogspot.com/2018/10/picking-apart-poweliks-filelessish.html) awesome guide about Poweliks is an evasive click-fraud trojan that uses several interesting evasion techniques. It contains both multiple stages and programming languages, and heavily influenced other evasive malware families, such as kovter


### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 16/11/2018
Amazing video [Malware Analysis VM Setup Tutorial](https://www.youtube.com/watch?v=gFxImi5t37c) and amazing channel [OALabs](https://www.youtube.com/channel/UC--DwaiMV-jtO-6EvmKOnqg). 
- https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/
- https://gist.github.com/OALabs/cad8d9489245f3f96d9669f56d2877f3
- [Malware Lab Setup - Network Configuration](https://www.youtube.com/watch?v=DjKr-MYIqxo)
- [SANS DFIR Webcast - Memory Forensics for Incident Response](https://www.youtube.com/watch?v=3xAEsDT-4NA)

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 20/11/2018 Winter is coming
To see the memory layout of a process in linux:
```
ps -aux | grep <name of program> 
cat /proc/<pid>/maps
```

### <img src="http://icons.iconarchive.com/icons/crountch/one-piece-jolly-roger/256/Luffys-flag-icon.png" width="50" height="45"> 21/11/2018

- [Viewing C object code using Objdump](https://ddmedinski.wordpress.com/2015/03/04/compiled-c-code/)

<br><br>
# The Captain's treasure chest "Arrr!"
<img src="https://imagessl6.casadellibro.com/a/l/t0/16/9788467735116.jpg" width="500" height="300" align="right">

## Tools:

#### Disassembler
- [ ] [IDA Pro](https://www.hex-rays.com/products/ida/index.shtml)
- [ ] [Radare2](https://rada.re/)
- [ ] [Hopper](https://www.hopperapp.com/)

#### Debugger
- [ ] [x64dbg](https://x64dbg.com/#start)
- [ ] [Gdb](https://www.youtube.com/watch?v=PorfLSr3DDI)
- [ ] [Immunity debugger](https://www.youtube.com/watch?v=YgezGxzwD8A)
- [ ] [WinDbg](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg--kernel-mode-)


#### Scanners
- [x] Wireshark
- [ ] [Burb](https://portswigger.net/burp)
- [ ] [OpenVas](http://www.openvas.org/)
- [ ] [Nessus](https://www.tenable.com/products/nessus/nessus-professional)

#### Frameworks
- [ ] [Cuckoo](https://cuckoosandbox.org/)
- [ ] [metasploit](https://www.metasploit.com/)
- [ ] [MSFvenom](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)
- [ ] [YARA](https://virustotal.github.io/yara/)

#### VMs:
- [ ] [remnux](https://remnux.org/)
- [ ] [FlareVm](https://www.fireeye.com/blog/threat-research/2017/07/flare-vm-the-windows-malware.html)


## Malware analysis/Reverse engineering courses:
- [x] [cybrary malware-analysis](https://www.cybrary.it/course/malware-analysis/)
- <strike>[Offensive Computer Security](https://www.cs.fsu.edu/~redwood/OffensiveComputerSecurity/lectures.html)</strike>
- <strike>[IntroX86 (OpenSecurityTraining)](http://opensecuritytraining.info/IntroX86.html)</strike>
- <strike>[Malware Dynamic Analysis (OpenSecurityTraining)](http://opensecuritytraining.info/MalwareDynamicAnalysis.html)</strike>
- <strike>[Introduction to Reverse Engineering Software (OpenSecurityTraining)](http://opensecuritytraining.info/MalwareDynamicAnalysis.html)</strike>
- <strike>[Reverse Engineering Malware (OpenSecurityTraining)](http://opensecuritytraining.info/IntroductionToReverseEngineering.html)</strike>
- <strike>[Rootkits (OpenSecurityTraining)](http://opensecuritytraining.info/Rootkits.html)</strike>
 
- [ ] [BLOG malware-analysis-tutorials-reverse](https://fumalwareanalysis.blogspot.com/p/malware-analysis-tutorials-reverse.html)
- [ ] [LiveOverflow Binary Hacking](https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)

#### From Napier university few courses of the professor [Bill Buchanan](https://www.napier.ac.uk/people/bill-buchanan)
 - [ ] [Security,Metasploit,Crypto ... ](http://asecuritysite.com/subjects/)
- [ ] [Intro to Sec. and Net. Forensics](https://www.youtube.com/watch?v=4iWxTlTiku8&list=PL345237ABC8FA67FE)
 - [ ] [CEH](https://www.youtube.com/watch?v=pEmDUr3PlVA&list=PLB6DFC45A0FBA856E)
- [ ] [Network Forensic](https://www.youtube.com/watch?v=z3kf1DyoEB8&list=PLqhpVxkBo1dMCcfBElL8nHF4o6PLEawd4)
- [ ] [Introduction to Cryptography](https://www.youtube.com/watch?v=_9YuARcSTVY&list=PLqhpVxkBo1dPiKHym2CxOKEnqC0350JH2)
- [ ] [Vsrious LAB tutorial](https://www.youtube.com/user/billatnapier/search?query=lab)
 #### Pluralsight courses
 - [ ] [Code Auditing by Dr. Jared DeMott](https://app.pluralsight.com/library/courses/code-auditing-security-hackers-developers)
- [ ] [Fuzzing Dr. Jared DeMott](https://app.pluralsight.com/library/courses/fuzzing-security-hackers-developers)
- [ ] [Reverse Engineering Dr. Jared DeMott](https://app.pluralsight.com/library/courses/reverse-engineering-security-hackers-developers)
- [ ] [Exploit Development Dr. Jared DeMott](https://app.pluralsight.com/library/courses/exploit-development-security-hackers-developers)
- [ ] [Combating Exploit Kits Dr. Jared DeMott](https://app.pluralsight.com/library/courses/malware-advanced-analysis-combating-exploit-kits)
- [ ] [Analyzing Malware for .NET and Java Binaries by Josh Stroschein](https://app.pluralsight.com/library/courses/dotnet-java-binaries-analyzing-malware/table-of-contents)
- [ ] [Ethical Hacking: Malware Threats by Dale Meredith](https://app.pluralsight.com/library/courses/ethical-hacking-malware-threats/table-of-contents)
- [x] [Getting Started Analyzing Malware Infections by Cristian Pascariu](https://app.pluralsight.com/library/courses/analyzing-malware-infections-getting-started/table-of-contents)

#### Webpage:
- [VUsec](https://www.vusec.net/)
- [Defcon archive](https://www.defcon.org/html/links/dc-archives.html)
- [The International Obfuscated C Code Contest](https://www.ioccc.org/)

#### Repositories:
- [https://github.com/xpn](https://github.com/xpn)
- [https://github.com/RPISEC/Malware](https://github.com/RPISEC/Malware)
- [Awesome Malware Analysis](https://github.com/rshipp/awesome-malware-analysis)

#### Blogs:
- [xpnsec](https://blog.xpnsec.com/)
- [zeltser's reverse-engineering-webcasts](https://zeltser.com/reverse-engineering-webcasts/)

#### Youtube channels:
- [The big list](https://www.youtube.com/channel/UC4K85H338QqfNBAXSlrz0uA/)

#### Dump:
- [This site contains a number of material related to security, digital forensics, networking, and many other things.](https://asecuritysite.com/)
- [SANS Malware Course](https://www.sans.org/course/reverse-engineering-malware-malware-analysis-tools-techniques)

#### Papers:
- [ ] [On the Effectiveness of Source Code Transformations for
Binary Obfuscation](https://pdfs.semanticscholar.org/60df/bc3a2502df9f50ad8f87bd35a476a2146b1a.pdf)
- [ ] [A Binary Rewriting Defense against Stack based Buffer Overflow Attacks](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.99.8950&rep=rep1&type=pdf)
- [ ] [Binary Obfuscation Using Signals](https://www2.cs.arizona.edu/solar/papers/obf-signal.pdf)
- [ ] [On the Effectiveness of Source Code Transformations for
Binary Obfuscation](https://pdfs.semanticscholar.org/60df/bc3a2502df9f50ad8f87bd35a476a2146b1a.pdf)
- [ ] [A Binary Rewriting Defense against Stack based Buffer Overflow Attacks](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.99.8950&rep=rep1&type=pdf)
- [ ] [Binary Obfuscation Using Signals](https://www2.cs.arizona.edu/solar/papers/obf-signal.pdf)
- [ ] [Unleashing MAYHEM on Binary Code](https://users.ece.cmu.edu/~dbrumley/pdf/Cha%20et%20al._2012_Unleashing%20Mayhem%20on%20Binary%20Code.pdf)
- [ ] [Dynamic Taint Analysis and Forward Symbolic Execution](https://users.ece.cmu.edu/~aavgerin/papers/Oakland10.pdf)
- [ ] [Adversarial Malware Binaries: Evading Deep]()
- [ ] Learning for Malware Detection in Executables](https://arxiv.org/pdf/1803.04173.pdf)
- [ ] [Yet another universal android root!](https://www.blackhat.com/docs/us-15/materials/us-15-Xu-Ah-Universal-Android-Rooting-Is-Back-wp.pdf)

#### Articles:
- [why-you-need-you-a-malware-analysis-lab-and-how-to-build-it](https://medium.com/@pramos/why-you-need-you-a-malware-analysis-lab-and-how-to-build-it-10048eaa8e9)
- [the-road-to-reverse-engineering-malware](https://medium.com/secjuice/the-road-to-reverse-engineering-malware-7c0bc1bda9d2)
- [How Do I Become A Malware Analyst?](https://www.concise-courses.com/malware-analyst/)
- [Fake DNS Responses for Malware Analysis](https://zeltser.com/fake-dns-tools-for-malware-analysis/)
- [Malicious PowerShell Detection via Machine Learning](https://www.fireeye.com/blog/threat-research/2018/07/malicious-powershell-detection-via-machine-learning.html)
- [ssdeep is a program for computing context triggered piecewise hashes](https://ssdeep-project.github.io/ssdeep/index.html)

#### Guides:
- [Using the IDA debugger to unpack an "hostile" PE executable](https://www.hex-rays.com/products/ida/support/tutorials/unpack_pe/manual.shtml)

<img src="https://hackadaycom.files.wordpress.com/2017/08/poc07reading-themed.png" width="950" height="350" align="center"> 



