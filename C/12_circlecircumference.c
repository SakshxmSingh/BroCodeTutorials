#include <stdio.h>

int main(){

    float radius;
    printf("Enter radius: \n");
    scanf("%f", &radius);

    float circ = 2*3.14*radius;

    printf("Circumference is %.2f units\n", circ);
    return 0;
}