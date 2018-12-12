#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <set>
#include <regex>
#include <chrono>
#include <iomanip>

#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day10/input.txt"
//#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day10/input-test.txt"

std::vector<std::pair<int, int>> points;
std::vector<std::pair<int, int>> speeds;

std::regex re = std::regex("position=<\\s*(-?\\d*),\\s*(-?\\d*)> velocity=<\\s*(-?\\d*),\\s*(-?\\d*)>");

struct bbox {
    long minX, maxX, minY, maxY;
};

bbox findBoundingBox() {
    bbox b = {INT64_MAX, -INT64_MAX, INT64_MAX, -INT64_MAX};
    std::for_each(points.begin(), points.end(), [&](auto e) {
        if (e.first > b.maxX) b.maxX = e.first;
        if (e.first < b.minX) b.minX = e.first;
        if (e.second > b.maxY) b.maxY = e.second;
        if (e.second < b.minY) b.minY = e.second;
    });

//    auto minMaxX = std::minmax_element(points.begin(), points.end(), [](auto a, auto b) { return a.first < b.first; });
//    b.minX = points[minMaxX.first - points.begin()].first;
//    b.maxX = points[minMaxX.second - points.begin()].first;

//    auto minMaxY = std::minmax_element(points.begin(), points.end(), [](auto a, auto b) { return a.second < b.second; });
//    b.minY = points[minMaxY.first - points.begin()].first;
//    b.maxY = points[minMaxY.second - points.begin()].first;

    return b;
}

long boundingBoxSize() {
    bbox b = findBoundingBox();
    return std::abs(b.maxX - b.minX) * std::abs(b.maxY - b.minY);
}

void printAt(int x, int y, char c) {
    printf("\033[%d;%dH%c\n", x, y, c);
}

int main() {
    // load input
    std::ifstream input(INPUT);
    std::string line;

    std::smatch match;
    while (std::getline(input, line)) {
        std::regex_match(line, match, re);
        auto s1 = match[1];
        auto s2 = match[2];
        auto s3 = match[3];
        auto s4 = match[4];
        points.push_back({std::stoi(s1), std::stoi(match[2])});
        speeds.push_back({std::stoi(match[3]), std::stoi(match[4])});
    }
    input.close();
    std::cout << "total points: " << points.size() << std::endl;

    long bboxSize;
    long lastSize = 0;
    long seconds = 0;

    do {
        lastSize = boundingBoxSize();

        // move all points one second
        for (int i = 0; i < points.size(); ++i) {
            points[i].first += speeds[i].first;
            points[i].second += speeds[i].second;
        }

        // calculate bounding box size
        bboxSize = boundingBoxSize();
        seconds++;

        std::cout << "Seconds: " << seconds << " " << "size:" << bboxSize << std::endl;

    } while (bboxSize < lastSize);

    seconds--;
    // do one step back
    for (int i = 0; i < points.size(); ++i) {
        points[i].first -= speeds[i].first;
        points[i].second -= speeds[i].second;
    }

    bboxSize = boundingBoxSize();
    bbox b = findBoundingBox();


    printf("\033[2J"); // clear
    for (auto point: points) {
        printAt(point.second - b.minY, point.first - b.minX, 'X');
    }
    std::cout << std::endl << "Seconds: " << seconds << " " << "size:" << bboxSize << std::endl;

    return 0;
}