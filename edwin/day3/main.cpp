#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

#include "Fabric.h"
#include "Claim.h"

#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day3/input.txt"

Fabric fabric;
std::vector<Claim> claims;

int main() {
    // load input
    std::ifstream input(INPUT);
    std::string word;
    while (std::getline(input, word)) claims.push_back(Claim(word));
    input.close();

    std::cout << "Total claims: " << claims.size() << std::endl;

    // part 1
    fabric.wipe();
    std::for_each(claims.begin(), claims.end(), [&](Claim claim) { fabric.applyClaim(claim); });
    std::cout << "Contested squares: " << fabric.countContestedSquares() << std::endl;

    // part 2
    fabric.wipe();
    std::for_each(claims.begin(), claims.end(), [&](Claim claim) { fabric.applyOverlap(claim); });
    std::cout << "Non-overlapping claim: " << fabric.findNonOverlappingClaim() << std::endl;

    return 0;
}