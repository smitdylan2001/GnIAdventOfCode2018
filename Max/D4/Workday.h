#pragma once
#include <vector>
#include <boost\algorithm\string.hpp>
#include <iostream>
#include <fstream>
#include <stdlib.h>  
#include <string>
#include <algorithm>
#include <iomanip>  

class Workday
{
public:
	Workday(std::string m, std::string d, std::string mi, std::string u, std::string ev);
	int sleepyBoys();
	std::string maand;
	std::string dag;
	std::string minuut;
	std::string uur;
	std::string gebeurtenis;

	std::vector<std::vector<std::string>> werkDagEvent;
	std::vector<std::string> sleeps;

	~Workday();
};

