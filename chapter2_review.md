Name: Keerthija Yalamanchili
Course: 5143 Operating Systems
Date: 19 feb 2016 

1.What are three objectives of an OS design?
Convenience:The main purpose of an operating system is to provide a convenient interface for users of a computer. The operating system makes use of a computer's hardware and provides services to computer users. The operating system provides some of its services, such as the computer mouse and keyboard, directly to computer users. It provides other services through application programs. 
Efficiency:A computer's operating system acts to provide interfaces for computer users to the computer hardware. It should be able to manage the hardware so that the hardware does its work in an efficient manner and uses resources in the best way.
Maintainability:Another objective for the design of an operating system is that it should be easy to maintain and upgrade. It should be easy to upgrade an operating system when new computer hardware comes to the market. And it should also be possible to expand the system to include more services to meet user needs. 

2.What is the kernel of an OS?
A kernel is the central part of an operating system. It manages the tasks of the computer and the hardware, most notably memory and CPU time.

3.What is multiprogramming?
Multiprogramming is one of the more basic types of parallel processing that can be employed in many different environments. Essentially, it makes it possible for several programs to be active at the same time, while still running through a single processor. Its functionality in this environment involves a continual process of sequentially accomplishing tasks associated with the function of one program, then moving on to run a task associated with the next program.

4.What is a process?
Process can be defined as running of two or more programs or sequences of instructions simultaneously by a computer with more than one central processor.

5.How is the execution context of a process used by the OS?
Also known as the process state, the execution context is the internal data the Operating system uses to control or supervise a process.

6.List and briefly explain five storage management responsibilities of a typical OS.
Storage management responsibilities of OS are as follows.
Process isolation: This is the prevention of data and instruction from interfering with each other process isolation helps this happen.
Automatic allocation and management: This is the process whereby allocation should be transported to the programmer.
Support of modular programming: Supports the program to be able to define programs modules and to create, destroy and alter the size of modules dynamically.
Protection and access control: This is the process of sharing memory this is desirable when sharing is needed by a particular application it also threatens the integrity of programs.
Long term storage: Is a process whereby memory is stored for a long period of time even when the computer is switch off it is stored in the RAM.

7.Explain the distinction between a real address and a virtual address.
Real addresses refer to hardware addresses of physical memory.
Virtual addresses refer to the address that is viewed by the process.
Virtual address might be same as real address but they might differ only when the virtual address mapped into the real address.
virtual space is limited by size of virtual addresses but this is not the same case with real address.virtual space and physical memory space are independent.

8.Describe the round-robin scheduling technique.
Round robbin scheduling is one of the oldest and most widely used algorithm. In this technique, processes are dspatched in a FIFO manner and are given a limited amount of time.If a process does not complete before its CPU-time expires, the CPU is preempted and given to the next process waiting in a queue. The preempted process is then placed at the back of the ready list.

9.Explain the difference between a monolithic kernel and a microkernel.
Monolithic kernel is much older than Microkernel.
Monolithic kernels are faster than microkernels. The first microkernel Mach was 50% slower than Monolithic kernel.
Monolithic kernels generally are bulky whereas microkernels are smaller in size which easily fits into the processors cache.
In Monolithic kernels, the device drivers reside in the kernel space whereas in the Microkernel the device drivers reside in the user space.
Monolithic kernels use signals and sockets to ensure IPC whereas microkernel approach uses message queues.

10.What is multithreading?
Multithreading is the ability of a program or an operating system process to manage its use by more than one user at a time and to even manage multiple requests by the same user without having to have multiple copies of the programming running in the computer.

11.List the key design issues for an SMP operating system.
SMP operating system involves symmetric multiprocessor system hardware and software archtecture where two or more identical processors connect to a single shared memory which have full access to all I/O devices.
In symmetric (or "tightly coupled") multiprocessing, the processors share memory and the I/O bus or data path. A single copy of the operating system is in charge of all the processors.


