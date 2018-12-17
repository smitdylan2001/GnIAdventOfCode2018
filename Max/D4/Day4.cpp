#include "Guard.h"
#include "Workday.h"
#include "Day4.h"

#define FILE_READ "/Users/Gebruiker/Desktop/ADVC_D4.txt"

//cutInputLine[value]
//DATUM
//[1] == Jaar	[2] == Maand	[3] == Dag
//TIJD
//[4] == uur	[5] == minuten
//BETEKENIS
//[7] == Wakes || falls || Guard	[8] == GuardNummer

Day4::Day4()
{
}

void Day4::calculate() {
	setInput();
	defineGuards();
	getWorkDays();
	addWorkDayEvent();
	printSleeps();

}

//Stopt de data in lokaal memory
void Day4::setInput() {
	in_stream.open(FILE_READ);
	while (!in_stream.eof()) {
		getline(in_stream, inputLine);
		input.push_back(inputLine);
	}
	in_stream.close();
}

//Vindt alle guards en maakt er een guard object voor aan.
void Day4::defineGuards() {
	std::vector<std::string>::iterator iterator = input.begin();
	while (iterator != input.end()) {
		std::string line = (*iterator);
		std::vector<std::string> cutInputLine;

		boost::algorithm::split(cutInputLine, line, boost::is_any_of("[], @x-:"));

		if (cutInputLine[7] == "Guard") {
			bool notFound = true;
			std::vector<Guard>::iterator iterator1 = guards.begin();
			while (iterator1 != guards.end()) {
				if ((*iterator1).nummer == cutInputLine[8]) {
					notFound = false;
				}
				iterator1++;
			}
			if (notFound) {
				std::string temp = cutInputLine[8];
				guards.push_back(Guard(temp));
			}
		}
		iterator++;
	}
}

//Maakt nieuwe werkdagen aan
void Day4::getWorkDays() {
	std::vector<std::string>::iterator iterator = input.begin();
	while (iterator != input.end()) {
		std::string line = (*iterator);
		std::vector<std::string> cutInputLine;

		boost::algorithm::split(cutInputLine, line, boost::is_any_of("[], @x-:"));

		//Als nieuwe guard komt
		if (cutInputLine[7] == "Guard") {
			std::vector<Guard>::iterator iterator1 = guards.begin();
			while (iterator1 != guards.end()) {
				if ((*iterator1).nummer == cutInputLine[8]) {
					(*iterator1).addWorkday(cutInputLine[2], 
											cutInputLine[3], 
											cutInputLine[4], 
											cutInputLine[5], 
											cutInputLine[7]);
				}
				iterator1++;
			}
		}
		iterator++;
	}
}

void Day4::addWorkDayEvent() {
	std::vector<std::string>::iterator iterator = input.begin();
	while (iterator != input.end()) {
		std::string line = (*iterator);
		std::vector<std::string> cutInputLine;

		boost::algorithm::split(cutInputLine, line, boost::is_any_of("[], @x-:"));
		if (cutInputLine[7] != "Guard") {//Deze zijn er al uit ge-vist
			std::vector<Guard>::iterator iterator1 = guards.begin();
			while (iterator1 != guards.end()) {
				std::vector<Workday>::iterator iterator2 = (*iterator1).workdays.begin();
				while (iterator2 != (*iterator1).workdays.end()) {

					if ((*iterator2).uur == "23") {//Werkdag begint voor 00 uur.

						if ((*iterator2).dag == "01") {//Werkdag begint op eerste van de maand.

							if (std::stoi((*iterator2).maand) == (std::stoi(cutInputLine[2]) - 1)) {

								if (std::stoi(cutInputLine[3]) <= 31 && std::stoi(cutInputLine[3]) >= 29) {
									(*iterator2).werkDagEvent.push_back(cutInputLine);
								}
							}
						}
						//als werkdag voor 00 begint maar het is niet de eerste van de maand.
						else if (std::stoi((*iterator2).dag) == (std::stoi(cutInputLine[3]) - 1) && (*iterator2).maand == cutInputLine[2]) {
							(*iterator2).werkDagEvent.push_back(cutInputLine);
						}
					}
					//Als werkdag na 00 begint
					else if ((*iterator2).maand == cutInputLine[2] && (*iterator2).dag == cutInputLine[3]) {
						(*iterator2).werkDagEvent.push_back(cutInputLine);					
					}
					iterator2++;
				}
				iterator1++;
			}
		}		
		iterator++;
	}
}

void Day4::printSleeps() {
	int sleep = 0;
	int x = 0;
	std::string name;

	std::vector<Guard>::iterator iterator = guards.begin();
	while (iterator != guards.end()) {
		std::cout << "Guard: " << (*iterator).nummer << std::endl;
		x = (*iterator).printDays();
		if (x > sleep) {
			sleep = x;
			name = (*iterator).nummer;
		}
		std::cout << std::endl;
		x = 0;
		iterator++;
	}
	std::cout<< name << " slept the most: " << sleep <<" Minutes"<< std::endl;
}

Day4::~Day4()
{
}
