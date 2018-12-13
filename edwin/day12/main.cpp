#include "bits/stdc++.h"

#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day12/input.txt"
//#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day12/input-test.txt"

void evolve();

std::string state;
std::vector<std::pair<std::string, bool>> rules;

static const int PADDING = 5;
int offset = PADDING;

//#define MAX_GEN 20 // part 1
#define MAX_GEN 50000000000 // part 2: yeah, no that's not gonna happen

int main() {

    // load input
    std::ifstream input(INPUT);
    std::string junk, pattern;
    char result;

    input >> junk >> junk >> state;
    state = std::string(offset, '.') + state + std::string(offset, '.');
    while (input >> pattern >> junk >> result) {
        rules.push_back({pattern, result == '#'});
    }
    input.close();

    int lastSum, lastDiff = 0;
    int repeatCount = 0;

    // part 1
    std::cout << "  0: " << state << std::endl;
    for (long i = 0; i < MAX_GEN; ++i) {
        evolve();
//        std::cout << (i < 9 ? " " : "") << i + 1 << " : " << state << std::endl;

        // ensure enough padding
        if (state.find('#') < PADDING) {
            state.insert(0, std::string(PADDING, '.'));
            offset += PADDING;
        }
        if (state.rfind('#') > state.size() - PADDING) {
            state += std::string(PADDING, '.');
        }

        int sum = 0;
        for (int j = 0; j < state.size(); ++j) {
            if (state[j] == '#') {
                sum += (j - offset);
            }
        }

        // part 2
        int diff = sum - lastSum;
        lastSum = sum;
        std::cout << i + 1 << " " << " sum: " << sum << " diff " << diff << std::endl;
        if (lastDiff == diff) {
            repeatCount++;
        } else {
            lastDiff = diff;
        }

        if (repeatCount > 5) {
            std::cout << "Stable growth after gen " << i - 5 << std::endl;
            std::cout << (50000000000 - i - 1) * diff + lastSum << std::endl;
            break;
        }
    }

    return 0;
}

void evolve() {
    std::string nextState(state.size(), '.');

    for (int i = 2; i < state.size(); ++i) {
        std::string env = state.substr(i - 2, PADDING);
        for (auto rule: rules) {
            if (rule.first == env) {
                nextState[i] = rule.second ? '#' : '.';
            }
        }
    }

    state.swap(nextState);
}
