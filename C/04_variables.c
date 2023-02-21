#include <stdio.h>

int main(){
    
    int x;
    x = 123;
    int y = 321;

    int age = 12;               // int
    float gpa = 8.3;            // float
    char grade = 'B';           // single character
    char name[] = "Saksham";    // array of characters

    printf("Your name is %s \n", name);                         // %s placehoder for string
    printf("You are %d years old.\n",age);                      // %d for decimal
    printf("Your average grade is %c and gpa is %f \n",grade,gpa); // %c for char, %f for float

    return 0;
}