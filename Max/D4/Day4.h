#pragma once
#include "Guard.h"
#include <vector>
#include <boost\algorithm\string.hpp>
#include <iostream>
#include <fstream>
#include <stdlib.h>  
#include <string>
#include <algorithm>
#include <iomanip>  
class Day4
{
public:
	Day4();
	void calculate();
	void setInput();
	void defineGuards();
	void getWorkDays();
	void addWorkDayEvent();
	void printSleeps();

	std::vector<Guard> guards;
	std::vector<std::string> input;
	std::string inputLine;
	std::ifstream in_stream;
	~Day4();
};

