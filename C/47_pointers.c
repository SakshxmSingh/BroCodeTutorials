#include<stdio.h>

void printAge(int *pAge)
{
   printf("You are %d years old\n", *pAge); //dereference
}

int main(){

    // pointer = a "variable-like" reference that holds a memory address to another variable, array, etc.
    //           some tasks are performed more easily with pointers
    //           * = indirection operator (value at address)

    int age = 18;
    int *pAge = &age;           

    printf("address of age: %p\n", &age);           //%p - format specifier to show add in hexadecimal, & is 'address-of' operator
    printf("value of pAge: %p\n", pAge);

    printf("size of age: %lu bytes\n", sizeof(age));
    printf("size of pAge: %lu bytes\n", sizeof(pAge));

    printf("value of age: %d\n", age);
    printf("value at stored address: %d\n", *pAge); //dereferencing

    printAge(&age);


    return 0;
}