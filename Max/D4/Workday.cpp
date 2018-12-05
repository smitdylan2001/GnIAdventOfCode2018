#include "Workday.h"



Workday::Workday(std::string m, std::string d, std::string h, std::string mi, std::string ev)
{
	this->maand = m;
	this->dag = d;
	this->uur = h;
	this->minuut = mi;
	this->gebeurtenis = ev;
}

//werkdagEvent <- iterator[value]
//DATUM
//[1] == Jaar	[2] == Maand	[3] == Dag
//TIJD
//[4] == uur	[5] == minuten
//BETEKENIS
//[7] == wakes || falls || Guard	[8] == GuardNummer

int Workday::sleepyBoys() {
	std::vector<int> sleepMinutes;
	std::vector<int> awakeMinutes;

	std::vector<std::vector<std::string>>::iterator iterator = werkDagEvent.begin();
	while (iterator != werkDagEvent.end()) {
		if ((*iterator)[7] == "falls") {
			sleepMinutes.push_back(std::stoi((*iterator)[5]));
		}
		if ((*iterator)[7] == "wakes") {
			awakeMinutes.push_back(std::stoi((*iterator)[5]));
		}
		iterator++;
	}
	std::sort(sleepMinutes.begin(), sleepMinutes.end());
	std::sort(awakeMinutes.begin(), awakeMinutes.end());

	int sleepsMins = sleepMinutes.size();
	int curSleep = 0;
	int minsASleep = 0;
	for (int i = 0; i < 60; i++) {
		if (!sleepMinutes.empty()) {
			if (i >= sleepMinutes[curSleep] && i < awakeMinutes[curSleep]) {
				sleeps.push_back("#");
				std::cout << "#";
				minsASleep++;
			}
			else {
				if (awakeMinutes[curSleep] < i && sleepsMins > curSleep) {
					curSleep++;
				}
				sleeps.push_back(".");
				std::cout << ".";
			}
		}
		else {
			sleeps.push_back(".");
			std::cout << ".";
		}
	}
	std::cout << minsASleep << std::endl;
	return minsASleep;
}



Workday::~Workday()
{
}
