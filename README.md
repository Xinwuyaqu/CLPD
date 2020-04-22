HOSTNAME=COMPUTE-1-1
SHELL=/bin/bash
TERM=xterm
HISTSIZE=1000
QTDIR=/usr/lib64/qt-3.3
USER=USER
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:
SUDO_USER=USER
SUDO_UID=0
USERNAME=USER
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAIL=/var/spool/mail/USER
PWD=/home/ozx
LANG=en_US.UTF-8
SHLVL=1
SUDO_COMMAND=/bin/bash ./collect_environment.sh
HOME=/USER
LOGNAME=USER
SUDO_GID=0
DISPLAY=localhost:10.0
_=/bin/env
+ lsb_release -a
LSB Version:	:core-4.1-amd64:core-4.1-noarch:cxx-4.1-amd64:cxx-4.1-noarch:desktop-4.1-amd64:desktop-4.1-noarch:languages-4.1-amd64:languages-4.1-noarch:printing-4.1-amd64:printing-4.1-noarch
Distributor ID:	CentOS
Description:	CentOS Linux release 7.4.1708 (Core) 
Release:	7.4.1708
Codename:	Core
+ uname -a
Linux COMPUTE-1-1 3.10.0-693.21.1.el7.x86_64 #1 SMP Wed Mar 7 19:03:37 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
+ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                20
On-line CPU(s) list:   0-19
Thread(s) per core:    1
Core(s) per socket:    10
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 63
Model name:            Intel(R) Xeon(R) CPU E5-2660 v3 @ 2.60GHz
Stepping:              2
CPU MHz:               2300.000
CPU max MHz:           2601.0000
CPU min MHz:           1200.0000
BogoMIPS:              5199.93
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              25600K
NUMA node0 CPU(s):     0-9
NUMA node1 CPU(s):     10-19
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm epb invpcid_single tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm xsaveopt cqm_llc cqm_occup_llc dtherm ida arat pln pts
+ cat /proc/meminfo
MemTotal:       65692152 kB
MemFree:        23887312 kB
MemAvailable:   57104908 kB
Buffers:            2144 kB
Cached:         32577008 kB
SwapCached:            0 kB
Active:         33122792 kB
Inactive:        1688648 kB
Active(anon):    4454228 kB
Inactive(anon):  1159704 kB
Active(file):   28668564 kB
Inactive(file):   528944 kB
Unevictable:      106744 kB
Mlocked:          106744 kB
SwapTotal:      32964604 kB
SwapFree:       32964604 kB
Dirty:              2612 kB
Writeback:             0 kB
AnonPages:       2338572 kB
Mapped:           232532 kB
Shmem:           3373276 kB
Slab:            5875864 kB
SReclaimable:    4517172 kB
SUnreclaim:      1358692 kB
KernelStack:       14432 kB
PageTables:        28580 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    65810680 kB
Committed_AS:    9177508 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      406704 kB
VmallocChunk:   34325397500 kB
HardwareCorrupted:     0 kB
AnonHugePages:    892928 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:      208060 kB
DirectMap2M:     7016448 kB
DirectMap1G:    61865984 kB
+ inxi -F -c0
./collect_environment.sh: line 14: inxi: command not found
+ lsblk -a
NAME            MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda               8:0    0 931.5G  0 disk 
?..sda1            8:1    0     1G  0 part /boot
?..sda2            8:2    0 930.5G  0 part 
  ?..centos-root 253:0    0    50G  0 lvm  /
  ?..centos-swap 253:1    0  31.4G  0 lvm  [SWAP]
  ?..centos-home 253:2    0 849.1G  0 lvm  /home
+ lsscsi -s
[4:0:0:0]    disk    ATA      TOSHIBA MG03ACA1 FL2A  /dev/sda   1.00TB
+ module list
./collect_environment.sh: line 17: module: command not found
+ nvidia-smi
./collect_environment.sh: line 18: nvidia-smi: command not found
+ lshw -short -quiet -sanitize
+ cat
./collect_environment.sh: line 19: lshw: command not found
+ lspci
00:00.0 Host bridge: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMI2 (rev 02)
00:01.0 PCI bridge: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCI Express Root Port 1 (rev 02)
00:02.0 PCI bridge: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCI Express Root Port 2 (rev 02)
00:02.2 PCI bridge: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCI Express Root Port 2 (rev 02)
00:03.0 PCI bridge: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCI Express Root Port 3 (rev 02)
00:04.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 0 (rev 02)
00:04.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 1 (rev 02)
00:04.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 2 (rev 02)
00:04.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 3 (rev 02)
00:04.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 4 (rev 02)
00:04.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 5 (rev 02)
00:04.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 6 (rev 02)
00:04.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 7 (rev 02)
00:05.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Address Map, VTd_Misc, System Management (rev 02)
00:05.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Hot Plug (rev 02)
00:05.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 RAS, Control Status and Global Errors (rev 02)
00:05.4 PIC: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 I/O APIC (rev 02)
00:11.0 Unassigned class [ff00]: Intel Corporation C610/X99 series chipset SPSR (rev 05)
00:11.4 SATA controller: Intel Corporation C610/X99 series chipset sSATA Controller [AHCI mode] (rev 05)
00:14.0 USB controller: Intel Corporation C610/X99 series chipset USB xHCI Host Controller (rev 05)
00:16.0 Communication controller: Intel Corporation C610/X99 series chipset MEI Controller #1 (rev 05)
00:16.1 Communication controller: Intel Corporation C610/X99 series chipset MEI Controller #2 (rev 05)
00:1a.0 USB controller: Intel Corporation C610/X99 series chipset USB Enhanced Host Controller #2 (rev 05)
00:1c.0 PCI bridge: Intel Corporation C610/X99 series chipset PCI Express Root Port #1 (rev d5)
00:1c.2 PCI bridge: Intel Corporation C610/X99 series chipset PCI Express Root Port #3 (rev d5)
00:1d.0 USB controller: Intel Corporation C610/X99 series chipset USB Enhanced Host Controller #1 (rev 05)
00:1f.0 ISA bridge: Intel Corporation C610/X99 series chipset LPC Controller (rev 05)
00:1f.2 SATA controller: Intel Corporation C610/X99 series chipset 6-Port SATA Controller [AHCI mode] (rev 05)
00:1f.3 SMBus: Intel Corporation C610/X99 series chipset SMBus Controller (rev 05)
02:00.0 Network controller: Mellanox Technologies MT27500 Family [ConnectX-3]
03:00.0 Ethernet controller: Intel Corporation I350 Gigabit Network Connection (rev 01)
03:00.1 Ethernet controller: Intel Corporation I350 Gigabit Network Connection (rev 01)
06:00.0 PCI bridge: ASPEED Technology, Inc. AST1150 PCI-to-PCI Bridge (rev 03)
07:00.0 VGA compatible controller: ASPEED Technology, Inc. ASPEED Graphics Family (rev 30)
7f:08.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 0 (rev 02)
7f:08.2 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 0 (rev 02)
7f:08.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 0 (rev 02)
7f:09.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 1 (rev 02)
7f:09.2 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 1 (rev 02)
7f:09.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 1 (rev 02)
7f:0b.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring (rev 02)
7f:0b.1 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring (rev 02)
7f:0b.2 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring (rev 02)
7f:0c.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0c.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0c.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0c.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0c.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0c.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0c.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0c.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0d.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0d.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
7f:0f.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
7f:0f.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
7f:0f.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
7f:0f.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
7f:0f.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers (rev 02)
7f:0f.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers (rev 02)
7f:0f.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers (rev 02)
7f:10.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCIe Ring Interface (rev 02)
7f:10.1 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCIe Ring Interface (rev 02)
7f:10.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers (rev 02)
7f:10.6 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers (rev 02)
7f:10.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers (rev 02)
7f:12.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 0 (rev 02)
7f:12.1 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 0 (rev 02)
7f:12.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 1 (rev 02)
7f:12.5 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 1 (rev 02)
7f:13.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Target Address, Thermal & RAS Registers (rev 02)
7f:13.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Target Address, Thermal & RAS Registers (rev 02)
7f:13.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder (rev 02)
7f:13.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder (rev 02)
7f:13.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Channel 0/1 Broadcast (rev 02)
7f:13.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Global Broadcast (rev 02)
7f:14.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 0 Thermal Control (rev 02)
7f:14.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 1 Thermal Control (rev 02)
7f:14.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 0 ERROR Registers (rev 02)
7f:14.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 1 ERROR Registers (rev 02)
7f:14.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
7f:14.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
7f:14.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
7f:14.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
7f:16.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Target Address, Thermal & RAS Registers (rev 02)
7f:16.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Target Address, Thermal & RAS Registers (rev 02)
7f:16.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel Target Address Decoder (rev 02)
7f:16.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel Target Address Decoder (rev 02)
7f:16.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Channel 2/3 Broadcast (rev 02)
7f:16.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Global Broadcast (rev 02)
7f:17.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 0 Thermal Control (rev 02)
7f:17.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 1 Thermal Control (rev 02)
7f:17.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 0 ERROR Registers (rev 02)
7f:17.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 1 ERROR Registers (rev 02)
7f:17.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
7f:17.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
7f:17.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
7f:17.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
7f:1e.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
7f:1e.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
7f:1e.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
7f:1e.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
7f:1e.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
7f:1f.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 VCU (rev 02)
7f:1f.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 VCU (rev 02)
80:04.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 0 (rev 02)
80:04.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 1 (rev 02)
80:04.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 2 (rev 02)
80:04.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 3 (rev 02)
80:04.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 4 (rev 02)
80:04.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 5 (rev 02)
80:04.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 6 (rev 02)
80:04.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMA Channel 7 (rev 02)
80:05.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Address Map, VTd_Misc, System Management (rev 02)
80:05.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Hot Plug (rev 02)
80:05.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 RAS, Control Status and Global Errors (rev 02)
80:05.4 PIC: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 I/O APIC (rev 02)
ff:08.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 0 (rev 02)
ff:08.2 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 0 (rev 02)
ff:08.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 0 (rev 02)
ff:09.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 1 (rev 02)
ff:09.2 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 1 (rev 02)
ff:09.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 QPI Link 1 (rev 02)
ff:0b.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring (rev 02)
ff:0b.1 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring (rev 02)
ff:0b.2 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring (rev 02)
ff:0c.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0c.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0c.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0c.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0c.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0c.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0c.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0c.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0d.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0d.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers (rev 02)
ff:0f.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
ff:0f.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
ff:0f.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
ff:0f.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent (rev 02)
ff:0f.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers (rev 02)
ff:0f.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers (rev 02)
ff:0f.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers (rev 02)
ff:10.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCIe Ring Interface (rev 02)
ff:10.1 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCIe Ring Interface (rev 02)
ff:10.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers (rev 02)
ff:10.6 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers (rev 02)
ff:10.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers (rev 02)
ff:12.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 0 (rev 02)
ff:12.1 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 0 (rev 02)
ff:12.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 1 (rev 02)
ff:12.5 Performance counters: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 1 (rev 02)
ff:13.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Target Address, Thermal & RAS Registers (rev 02)
ff:13.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Target Address, Thermal & RAS Registers (rev 02)
ff:13.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder (rev 02)
ff:13.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder (rev 02)
ff:13.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Channel 0/1 Broadcast (rev 02)
ff:13.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Global Broadcast (rev 02)
ff:14.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 0 Thermal Control (rev 02)
ff:14.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 1 Thermal Control (rev 02)
ff:14.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 0 ERROR Registers (rev 02)
ff:14.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 1 ERROR Registers (rev 02)
ff:14.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
ff:14.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
ff:14.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
ff:14.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1 (rev 02)
ff:16.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Target Address, Thermal & RAS Registers (rev 02)
ff:16.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Target Address, Thermal & RAS Registers (rev 02)
ff:16.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel Target Address Decoder (rev 02)
ff:16.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel Target Address Decoder (rev 02)
ff:16.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Channel 2/3 Broadcast (rev 02)
ff:16.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Global Broadcast (rev 02)
ff:17.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 0 Thermal Control (rev 02)
ff:17.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 1 Thermal Control (rev 02)
ff:17.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 0 ERROR Registers (rev 02)
ff:17.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 1 ERROR Registers (rev 02)
ff:17.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
ff:17.5 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
ff:17.6 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
ff:17.7 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3 (rev 02)
ff:1e.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
ff:1e.1 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
ff:1e.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
ff:1e.3 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
ff:1e.4 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit (rev 02)
ff:1f.0 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 VCU (rev 02)
ff:1f.2 System peripheral: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 VCU (rev 02)
