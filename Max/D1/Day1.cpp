#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>  
#include <string>
#include "Day1.h"

#define FILE_READ "/Users/Gebruiker/Desktop/ADVC_D1.txt"

//Constructor
Day1::Day1()
{
}

void Day1::calculate() {

	std::vector<int> list;
	std::vector<int> list2;
	std::ifstream in_stream;
	int count = 0;
	int temp;
	int loops = 0;
	std::string line;

	//Open het bestand
	

	if (!in_stream) {
		std::cout << "Error with input-file" << std::endl;
	}
	std::cout << "Buzzy: ";
	while (true) {
		in_stream.open(FILE_READ);
		while (!in_stream.eof()) {
			getline(in_stream, line);
			count += std::stoi(line);

			std::vector<int>::iterator iterator = list.begin();
			while (iterator != list.end()) {
				if ((*iterator) == count) {
					std::cout << "DONE" << std::endl;
					std::cout << (*iterator) << std::endl;
					std::cin.get();
				}
				else {
					iterator++;
				}
			}
			list.push_back(count);
		}
		std::cout << ".";
		in_stream.close();
	}
}

//Destructor
Day1::~Day1()
{
}
