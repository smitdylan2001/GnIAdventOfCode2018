#include <iostream>
#include <fstream>
#include <vector>

#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day8/input.txt"
//#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day8/input-test.txt"

int totalMetadataSum;

int readNode(std::ifstream& input) {
    std::vector<int> childNodeValues;
    int nodeValue = 0;

    int childNodeCount;
    int metadataCount;

    input >> childNodeCount;
    input >> metadataCount;

    std::cout << "Node has " << childNodeCount << " child, " << metadataCount << " metadata" << std::endl;
    for (int i = 0; i < childNodeCount; ++i) {
        childNodeValues.push_back(readNode(input));
    }

    int metadata;
    for (int j = 0; j < metadataCount; ++j) {
        input >> metadata;
        totalMetadataSum += metadata;
        if (childNodeCount == 0) {
            nodeValue += metadata;
        } else {
            if (metadata <= childNodeValues.size()) {
                nodeValue+= childNodeValues[metadata - 1];
            }
        }
    }

    return nodeValue;
}

int main() {
// part 1
    std::ifstream input(INPUT);
    int rootValue = readNode(input);
    std::cout << "Total metadata sum: " << totalMetadataSum << std::endl;
    std::cout << "Root node value: " << rootValue << std::endl;

    return 0;
}