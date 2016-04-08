Name : Keerthija Yalamanchili
Date : 8th April, 2016
M Id : M20227829

Question 1
Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

Threads1.py contains the threads that run without using the same memory in their execution and it also contains the copies of the local variables.
In threads2.py, the threads uses global variables in their execution and so the threads will try to access together during their execution.

Question 2
After running Thread3.py does it fix the problems that occurred in Threads2.py? What's the down-side?

Thread3.py fix the problems that have occurred in Threads2.py. The Threads3.py uses lock() method in the code. With the help of lock() method, whenever one thread access the global variable, the other thread uses this lock() method and lock the access to the first thread until the process is done and the variable is unlocked by the thread.

Question 3
Comment out the join statements at the bottom of the program and describe what happens.

Generally, when there is join function in the program, the main function will execute only after all the threads complete the execution. But here, as there is no join function in the program, the main function has executed without the completion of the threads execution and so printing as "Goodbye from the main program".

Question 4
What happens if you try to Ctrl-C out of the program before it terminates?

If we do so, the program does not stop running, rather it continues with its execution.

Question 5
Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.
Here, each and every thread tries to assign the value to the global variable. Whenever, a particular thread is requesting an access to the global variable, if some other thread try to access the same global variable, then there will be change in the contents resulting in false output. 

Question 6
Does un-commenting the lock operations clear up the problem in question 5?

Yes, it clear up the problem that has occurred in question 5. This is because, when there is lock function in the code, one particular thread cannot access the variables independently. When there is no lock function, the threads can access the variable at any point of time.
