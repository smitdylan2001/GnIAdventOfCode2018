#include <iostream>
#include "Claim.h"

std::regex Claim::re = std::regex("#(\\d*) @ (\\d*),(\\d*): (\\d*)x(\\d*)");

Claim::Claim(std::string line) {
    std::smatch match;
    if (std::regex_match(line, match, Claim::re) && match.size()==6) {
//        std::cout << match[0] << std::endl;
        this->id = std::stoi(match[1]);
        this->x = std::stoi(match[2]);
        this->y = std::stoi(match[3]);
        this->width = std::stoi(match[4]);
        this->height = std::stoi(match[5]);

    } else {
        std::cout << "No match!" << line << std::endl;
    }

}


