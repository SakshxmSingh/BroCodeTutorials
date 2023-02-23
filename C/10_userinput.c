#include <stdio.h>
#include <string.h>

int main(){

    char name[25];                              // 25 here specifies no of bytes for the char list
    int age;

    printf("What is your name?\n");
    //scanf("%s", &name);                          this only reads uptill a blank space, so to prevent this, use fgets()
    fgets(name, 25, stdin);                     // (char variable, size of char variable, file/ops), returns a new line character, for blank spaces
    name[strlen(name)-1] = '\0';                // to remove the new line escape sequence

    printf("How old are you?\n");
    scanf("%d", &age);                          // & returns the memory address of the variable
    
    printf("Hello %s\n", name);
    printf("You are %d years old\n", age);

    return 0;
}