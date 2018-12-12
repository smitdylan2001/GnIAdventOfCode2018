#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <set>
#include <regex>
#include <chrono>
#include <iomanip>

#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day6/input.txt"

int manhattanDistance(std::pair<int, int> a, std::pair<int, int> b) {
    return std::abs(a.first - b.first) + std::abs(a.second - b.second);

}
/*
//
//    int width = std::max_element(coords.begin(), coords.end(), [](auto a, auto b) { return a.first < b.first; })->first;
//    int height = std::max_element(coords.begin(), coords.end(),
//                                  [](auto a, auto b) { return a.second < b.second; })->first;
//
//
//    std::map<int, int> cnt;
//    for(int i = 0; i < width; i++) {
//        for(int j = 0; j < height; j++) {
//            int minDist = 1e9;
//            int idx;
//            bool eq = false;
//            for(int k = 0; k < coords.size(); k++) {
//                int curDist = abs(coords[k].first - i) + abs(coords[k].second -j);
//                if(curDist < minDist) {
//                    minDist = curDist;
//                    idx = k;
//                    eq = false;
//                } else if (curDist == minDist) {
//                    eq = true;
//                }
//            }
//            if(!eq) cnt[idx]++;
//        }
//    }
//
//
//    std::vector<std::pair<int,int>> ans;
//    for(auto cur : cnt) {
//        ans.push_back({cur.second, cur.first});
//    }
//    sort(ans.begin(), ans.end());
//    for(auto cur : ans) std::cout << cur.first << " " << cur.second << std::endl;
//
//    // for each square, determine
////    int grid[width][height];
////    for (int i = 0; i < width; ++i) {
////        for (int j = 0; j < height; ++j) {
////
////        }
////    }
//
//
//    return 0;
//}



#include <bits/stdc++.h>

using namespace std;

std::regex re = std::regex("(\\d+), (\\d+)");
std::vector<std::pair<int, int>> coords;

//
//

int main() {
    vector<pair<int, int>> coords;

    std::ifstream input(INPUT);

//    int x, y;
//    char junk;
//    while (input >> x) {
//        input >> junk >> y;
//        coords.push_back({x, y});
//    }

    std::string line;
    while (std::getline(input, line)) {
        std::smatch match;
        std::regex_match(line, match, re);
        coords.push_back({std::stoi(match[1]), std::stoi(match[2])});
    }

    input.close();

    std::cout << "total number of coords: " << coords.size() << std::endl;

    map<int, int> cnt;

// For Part 2, uncomment all comments
// int ans = 0;
    for (int i = -200; i < 200; i++) {
        for (int j = -200; j < 200; j++) {
            int minDist = 1e9;
            int idx;
            bool eq = false;
            for (int k = 0; k < coords.size(); k++) {
                int curDist = abs(coords[k].first - i) + abs(coords[k].second - j);
                if (curDist < minDist) {
                    minDist = curDist;
                    idx = k;
                    eq = false;
                } else if (curDist == minDist) {
                    eq = true;
                }
            }
            if (!eq) cnt[idx]++;

            // For Part 2, delete the rest of the inner loop
            // int totDist = 0;
            // for(int k = 0; k < vals.size(); k++) {
            // 	int curDist = abs(vals[k].first - i) + abs(vals[k].second -j);
            // 	totDist += curDist;
            // }
            // if(totDist < 10000) ans++;
        }
    }

// cout << ans << endl;
// For Part 2 delete everything below
    vector<pair<int, int>> ans;
    for (auto cur : cnt) {
        ans.push_back({cur.second, cur.first});
    }
    sort(ans.begin(), ans.end());
    for (auto cur : ans) cout << cur.first << " " << cur.second << endl;

    return 0;
}

{
    */
#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

int main(){

    std::ifstream input(INPUT);

    vector<pii> vals;
    int x, y;
    char junk;
    while (input >> x) {
        input >> junk >> y;
        vals.push_back({x, y});
    }

    map<int, int> cnt;

// For Part 2, uncomment all comments
 int ans = 0;
    for(int i = -1000; i < 1000; i++) {
        for(int j = -1000; j < 1000; j++) {
            int minDist = 1e9;
            int idx;
            bool eq = false;
            for(int k = 0; k < vals.size(); k++) {
                int curDist = abs(vals[k].first - i) + abs(vals[k].second -j);
                if(curDist < minDist) {
                    minDist = curDist;
                    idx = k;
                    eq = false;
                } else if (curDist == minDist) {
                    eq = true;
                }
            }
            if(!eq) cnt[idx]++;

//             For Part 2, delete the rest of the inner loop
             int totDist = 0;
             for(int k = 0; k < vals.size(); k++) {
             	int curDist = abs(vals[k].first - i) + abs(vals[k].second -j);
             	totDist += curDist;
             }
             if(totDist < 10000) ans++;
        }
    }

 cout << ans << endl;

    return 0;
}
