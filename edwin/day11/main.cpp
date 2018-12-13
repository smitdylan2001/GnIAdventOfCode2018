#include <iostream>
#include <assert.h>
#include <tuple>

int GRID_SERIAL = 7989;

int grid[300][300];

void fillGrid(int gridSerial);
int powerlevel(int x, int y, int gridSerial);
std::tuple<int, int, int> bestGrid(int size);

int main() {
    // tests
    assert(powerlevel(3, 5, 8) == 4);
    assert(powerlevel(122, 79, 57) == -5);
    assert(powerlevel(217, 196, 39) == 0);
    assert(powerlevel(101, 153, 71) == 4);

    // fill grid
    fillGrid(GRID_SERIAL);

    // part 1
    auto best = bestGrid(3);
    std::cout << "Best 3x3 grid: " << std::get<2>(best) << "@" << std::get<0>(best) << "," << std::get<1>(best) << std::endl;

    // tests

    // part 2
    fillGrid(18);
    best = bestGrid(16);
    assert(std::get<0>(best) == 90);
    assert(std::get<1>(best) == 269);
    assert(std::get<2>(best) == 113);

    fillGrid(42);
    best = bestGrid(12);
    assert(std::get<0>(best) == 232);
    assert(std::get<1>(best) == 251);
    assert(std::get<2>(best) == 119);

    // part 2
    fillGrid(GRID_SERIAL);

    int bestX = 0;
    int bestY = 0;
    int bestSize = 0;
    int bestPower = INT32_MIN;

    for (int size = 1; size <= 300; ++size) {
        best = bestGrid(size);
        int power = std::get<2>(best);
        if (power > bestPower) {
            bestSize = size;
            bestPower = power;
            bestX = std::get<0>(best);
            bestY = std::get<1>(best);
            std::cout << "Best so far: " << bestPower << "@" << bestX << "," << bestY << "," << bestSize << std::endl;
        }
    }

    return 0;
}

int powerlevel(int x, int y, int gridSerial) {
    int rackId = x + 10;
    int level = rackId * y;
    level += gridSerial;
    level *= rackId;
    level /= 100;
    level %= 10;

    return level - 5;
}

void fillGrid(int gridSerial) {
    for (int i = 0; i < 300; ++i) {
        for (int j = 0; j < 300; ++j) {
            grid[i][j] = powerlevel(i + 1, j + 1, gridSerial);
        }
    }
}

std::tuple<int, int, int> bestGrid(int size) {
    int maxSum = INT32_MIN;
    int maxY = 0;
    int maxX = 0;

    for (int x = 0; x < 300 - size + 1; ++x) {
        for (int y = 0; y < 300 - size + 1; ++y) {
            int sum = 0;
            for (int i = 0; i < size; ++i) {
                for (int j = 0; j < size; ++j) {
                    sum += grid[x + i][y + j];
                }
            }
            if (sum > maxSum) {
                maxX = x + 1;
                maxY = y + 1;
                maxSum = sum;
            }
        }
    }
    return {maxX, maxY, maxSum};
}