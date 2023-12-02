#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

int largestCalories(list<int> calorieList)
{
    if (calorieList.empty())
    {
        return 0;
    }

    int maxCalories = calorieList.front();
    for (int calories : calorieList)
    {
        if (calories > maxCalories)
        {
            maxCalories = calories;
        }
    }

    return maxCalories;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <filename>\n", argv[0]);
    }

    list<int> elfCalories;
    int calories = 0;
    int topThreeElvesCalories = 0;


    ifstream inputFile(argv[1]);
    string line;

    if (!inputFile.is_open())
    {
        printf("Failed to open the input file!\n");
    }

    while (getline(inputFile, line))
    {
        if (!line.empty())
        {
            int calorie = stoi(line.c_str());
            calories += calorie;
        }
        else
        {
            elfCalories.push_back(calories);
            calories = 0;
        }
    }

    int maxCalories = largestCalories(elfCalories);
    printf("Part One Solution: %d\n", maxCalories);


    for (int i = 0; i <= 2; i++)
    {
        topThreeElvesCalories += largestCalories(elfCalories);
        elfCalories.remove(largestCalories(elfCalories));
    }

    printf("Part Two Solution: %d\n", topThreeElvesCalories);

    inputFile.close();
    return 0;
}