# introduction 
Notes about reverse engineering

## introduction to gdb 7-16-2018
- [x] [Reversing and Cracking first simple Program](https://www.youtube.com/watch?v=VroEiMOJPm8&t=2s)
  - Download [this repository](https://github.com/LiveOverflow/liveoverflow_youtube/tree/master/0x05_simple_crackme_intro_assembler) or use     git clone https://github.com/LiveOverflow/liveoverflow_youtube.git
  - Change the gdb disassembly-flavor intel
  - Disassembly main
    - check all the [jumps](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow) and try to rebuild the flow of the program understanding which part of the program does what and why it jumps
      - JNE Jump if Not Equal
      - JG  Jump if Greater
      - JGE Jump if Greater or Equal
      - JAE Jump if Above or Equal
      - JL  Jump if Lesser
      - JLE Jump if Less or Equal
      - JBE Jump if Below or Equal 
      - JZ  Jump if Zero
      - JNZ Jump if Not Zero
    
      