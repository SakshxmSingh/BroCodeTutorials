#include <stdio.h>

int main(){

    char ops;
    double num1;
    double num2;
    double result;

    printf("Enter operation: ");
    scanf("%c",&ops);

    printf("Enter no.1: ");
    scanf("%lf",&num1);

    printf("Enter no.2: ");
    scanf("%lf",&num2);

    switch(ops){
        case '+':
            result = num1 + num2;
            printf("%lf", result);
            break;
        case '*':
            result = num1 * num2;
            printf("%lf", result);
            break;
        case '-':
            result = num1 - num2;
            printf("%lf", result);
            break;
        case '/':
            result = num1 / num2;
            printf("%lf", result);
            break;
        default:
            printf("Enter valid operation.\n");
    }

    return 0;
}