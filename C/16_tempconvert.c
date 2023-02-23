#include <stdio.h>
#include <ctype.h>

int main(){
    char unit;
    double tempf;
    double tempc;

    printf("Enter unit of temp (C or F)\n");
    scanf("%c", &unit);

    unit = toupper(unit);
    if(unit == 'C'){
        printf("Enter temp in C: \n");
        scanf("%lf", &tempc);
        tempf = (9/5.0)*tempc + 32;

        printf("Temp in F is %.3lf\n",tempf);
    }
    else if(unit == 'F'){
        printf("Enter temp in F: \n");
        scanf("%lf", &tempf);
        tempc = (tempf - 32)*(5/9.0);

        printf("Temp in C is %.3lf\n",tempc);
    }
    else{
        printf("Enter valid unit.\n");
    }

    return 0;
}