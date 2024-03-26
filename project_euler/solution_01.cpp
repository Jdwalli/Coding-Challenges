#include <iostream>


int is_multiple_of_3_or_5(int number){
    if (number % 3 == 0 || number % 5 == 0) {
            return number;
        }
    return 0;
}


int main(){
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        sum += is_multiple_of_3_or_5(i);
    }
    std::cout << sum << "\n";
}

