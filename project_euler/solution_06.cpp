#include <iostream>
#include <cmath>

int calculate_sum_of_squares(int MAX){
    int sum = 0;

    for (int i = 0; i < MAX + 1; i++) {
        sum += pow(i, 2);
    }

    return sum;
}

int calculate_square_of_sum(int MAX){
    int sum = 0;

    for (int i = 0; i < MAX + 1; i++) {
        sum += i;
    }

    return pow(sum, 2);
}

int main(){
    std::cout << calculate_square_of_sum(100) - calculate_sum_of_squares(100) << "\n";
}

