#pragma once
#include <regex>
#include <string>

class Claim {

    public:
        Claim(std::string line);
        int id;
        int x,y;
        int width, height;

    private:
        static std::regex re;
};



