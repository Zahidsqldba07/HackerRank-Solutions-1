#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    double mealCost;
    int tipPercent, taxPercent;
    
    scanf("%lf", &mealCost);
    scanf("%d", &tipPercent);
    scanf("%d", &taxPercent);
    
    int totalCost = round(mealCost+(tipPercent+taxPercent)*mealCost/100);
    
    printf("The total meal cost is %d dollars.", totalCost);
    
    return 0;
}
