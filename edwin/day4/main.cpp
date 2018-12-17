#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <set>
#include <regex>
#include <chrono>
#include <iomanip>

#define INPUT "/home/edwin/code/GnIAdventOfCode2018/edwin/day4/input.txt"

struct guard_record {
    long timestamp;
    int minute;
    std::string activity;
};

std::vector<guard_record> records;

std::regex re_guardId = std::regex(".* Guard #(\\d*) .*");
std::regex re_wakeup = std::regex(".* wakes up.*");
std::regex re_fallasleep = std::regex(".* falls asleep.*");

guard_record parse(std::string recordStr) {
    guard_record record;
    std::string timestr = recordStr.substr(1, 16);
    std::tm tm = {};
    std::stringstream ss(timestr);
    ss >> std::get_time(&tm, "%Y-%m-%d %H:%M");

    record.timestamp = std::mktime(&tm);
    record.minute = tm.tm_min;
    record.activity = recordStr.substr(18, recordStr.length());

    return record;
}

int main() {
    // load input
    std::ifstream input(INPUT);
    std::string txtRecord;

    while (std::getline(input, txtRecord)) {
        guard_record record = parse(txtRecord);
        records.push_back(record);
    }
    input.close();
    std::cout << "total records: " << records.size() << std::endl;

    // part 1
    std::sort(records.begin(), records.end(), [](guard_record a, guard_record b) { return a.timestamp < b.timestamp; });

    std::unordered_map<int, long> sleepDurationByGuard;
    std::unordered_map<int, std::array<int, 60>> sleepPerMinuteByGuard;

    int currentGuard = 0;
    long sleepStart = 0;
    long sleepEnd = 0;
    int minuteStart = 0;
    int minuteEnd = 0;

    std::smatch match;
    for (guard_record record: records) {
        if (std::regex_match(record.activity, match, re_guardId)) {
            currentGuard = std::stoi(match[1]);
            std::cout << " guard " << currentGuard << " starts watch" << std::endl;
        } else if (std::regex_match(record.activity, match, re_fallasleep)) {
            std::cout << " guard " << currentGuard << " falls aleep at minute " << record.minute << std::endl;
            sleepStart = record.timestamp;
            minuteStart = record.minute;
        } else if (std::regex_match(record.activity, match, re_wakeup)) {
            sleepEnd = record.timestamp;
            minuteEnd = record.minute;
            long duration = sleepEnd - sleepStart;
            std::cout << " guard " << currentGuard << " wakes up at minute " << record.minute << " after "
                      << duration / 60 << " min" << (minuteEnd < minuteStart) << std::endl;
            sleepDurationByGuard[currentGuard] += duration / 60;
            for (int i = minuteStart; i < minuteEnd; ++i) {
                sleepPerMinuteByGuard[currentGuard][i]++;
            }
        }
    }

    // find guard with largest total number of sleep minutes
    auto sleepiestGuard = std::max_element(sleepDurationByGuard.begin(),
                                           sleepDurationByGuard.end(),
                                           [](auto a, auto b) { return a.second < b.second; });

    // find minute where this guard is most often asleep
    int sleepiestGuardId = (*sleepiestGuard).first;
    auto minutesForGuard = sleepPerMinuteByGuard[sleepiestGuardId];
    auto medianMinute = std::distance(std::begin(minutesForGuard),
                                      std::max_element(std::begin(minutesForGuard),
                                                       std::end(minutesForGuard)));

    std::cout << "sleepiest guard: " << sleepiestGuardId << ", "
              << "total: " << (*sleepiestGuard).second << " minutes asleep, "
              << "median minute: " << medianMinute
              << std::endl;
    std::cout << "check for part 1: " << sleepiestGuardId * medianMinute << std::endl;

    // part 2
    int maxMinutes = 0;
    int maxMinute = 0;
    int maxGuard = 0;
    for (auto guardWithMinutes : sleepPerMinuteByGuard) {
        for (int j = 0; j < 60; ++j) {
            int guardId = guardWithMinutes.first;
            int guardMinutes = guardWithMinutes.second[j];
            if (guardMinutes > maxMinutes) {
                maxMinutes = guardMinutes;
                maxGuard = guardId;
                maxMinute = j;
            }
        }
    }

    std::cout << "guard" << maxGuard << " maxMinute: " << maxMinute << " " << maxGuard * maxMinute << std::endl;

    return 0;
}