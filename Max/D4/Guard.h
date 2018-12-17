#pragma once
#include <vector>
#include <stdlib.h>  
#include <string>
#include "Workday.h"

class Guard
{
public:
	Guard(std::string nummer);
	
	void addWorkday(std::string m, std::string d, std::string h, std::string u, std::string ev);
	int printDays();
	std::vector<Workday> workdays;
	std::string nummer;

	~Guard();
};

