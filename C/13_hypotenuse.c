#include <stdio.h>
#include <math.h>

int main(){

    double l1;
    double l2;
    double h;

    printf("Enter l1: \n");
    scanf("%lf", &l1);
    printf("Enter l2: \n");
    scanf("%lf", &l2);

    h = sqrt((l1*l1) + (l2*l2));
    printf("The hypotenuse is %.3lf\n", h);

    return 0;
}