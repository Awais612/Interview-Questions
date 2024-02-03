# What is the Difference between Dangling Pointers and Memory Leakage

Basically, dangling pointer and memory leak are different terms. If a pointer is pointing to memory that is not owned by your program (except the null pointer ) or an invalid memory, the pointer is called a dangling pointer. Generally, daggling pointers arise when the referencing object is deleted or deallocated, without changing the value of the pointers.

![alt text](https://aticleworld.com/wp-content/uploads/2017/10/Dangling-Pointer.png)

In opposite to the dangling pointer, a memory leak occurs when you forget to deallocate the allocated memory. In the C language compiler does not deallocate the memory automatically it is freed by the programmer explicitly. In another word, you can say that a memory leak is a type of resource leak.