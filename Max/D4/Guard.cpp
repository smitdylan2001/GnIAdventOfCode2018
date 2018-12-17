#include "Guard.h"
#include "Workday.h"



Guard::Guard(std::string num)
{
	this->nummer = num;
}

void Guard::addWorkday(std::string m, std::string d, std::string h, std::string u, std::string ev)
{
	Workday w = Workday(m, d, h, u, ev);
	workdays.push_back(w);
}

int Guard::printDays() {
	int sleep = 0;
	int workDs = 0;
	std::cout << "000000000011111111112222222222333333333344444444445555555555" << std::endl;
	std::cout << "012345678901234567890123456789012345678901234567890123456789"<< std::endl;
	std::vector<Workday>::iterator iterator = workdays.begin();
	while (iterator != workdays.end()) {
		sleep = sleep + (*iterator).sleepyBoys();
		workDs++;
		iterator++;
	}
	std::cout <<sleep<<" WorkDays "<<workDs<< std::endl;
	return sleep;
}

Guard::~Guard()
{
}
