#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <sstream>
#include <map>

using namespace std;

map<char, std::pair<std::string, int>> gameTable = {
    {'A', {"Rock", 1}},
    {'B', {"Paper", 2}},
    {'C', {"Scissors", 3}},
    {'X', {"Rock", 1}},
    {'Y', {"Paper", 2}},
    {'Z', {"Scissors", 3}}
};


int determinePartOneScore(char opponent, char me){
    int score = gameTable[me].second;

    if ( (opponent == 'A' && me == 'X') ||  (opponent == 'B' && me == 'Y') || (opponent == 'C' && me == 'Z') ) {
        score += 3;
    }

    if ((me == 'X' && opponent == 'C') || (me == 'Y' && opponent == 'A') || (me == 'Z' && opponent == 'B')) {
        score += 6;
    } 

    return score;
}

int determinePartTwoScore(char opponent, char me){

    if (me == 'X') {
        switch (opponent){
            case 'C':
                return 2;
            case 'A':
                return 3;
            case 'B':
                return 1;
        }
    }

    if (me == 'Y') {
        return gameTable[opponent].second + 3;
    }

    if (me == 'Z') {
        switch (opponent){
            case 'C':
                return 1 + 6;
            case 'A':
                return 2 + 6;
            case 'B':
                return 3 + 6;
        }
        
    }

    return 0;
}


int main(int argc, char *argv[])
{
    int partOneScore = 0;
    int partTwoScore = 0;


    if (argc != 2)
    {
        printf("Usage: %s <filename>\n", argv[0]);
        return -1;
    }

    ifstream inputFile(argv[1]);
    string line;

    if (!inputFile.is_open())
    {
        printf("Failed to open the input file!\n");
        return -1;
    }


    while (getline(inputFile, line))
    {
        if (!line.empty())
        {
            char opponent, me;
            istringstream iss(line);
            iss >> opponent >> me;
            partOneScore += determinePartOneScore(opponent, me);
            partTwoScore += determinePartTwoScore(opponent, me);
        }
    }

    cout << "Part One Solution: " << partOneScore << "\n";
    cout << "Part Two Solution: " << partTwoScore << "\n";

    inputFile.close();
    return 0;
}
