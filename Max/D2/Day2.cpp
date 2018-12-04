#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>  
#include <string>

#define FILE_READ "/Users/Gebruiker/Desktop/ADVC_D2.txt"
#include "Day2.h"



Day2::Day2()
{
}

void Day2::calculate1() {
	std::ifstream in_stream;
	std::string line;
	//std::vector<char> letters;

	int curDup = 0;

	int doubles = 0;
	int triples = 0;

	int loops = 0;
	std::vector<int> result = {0, 0};

	//open File
	in_stream.open(FILE_READ);

	while (!in_stream.eof()) {
		loops++;
		getline(in_stream, line);
		std::vector<char> letters(line.begin(), line.end());

		//Pak 1 letter
		///////////////////////////////////////////////////////
		std::vector<char>::iterator iterator_1 = letters.begin();
		while (iterator_1 != letters.end()) {
			char toTest = (*iterator_1);

			curDup = 0;

			//Loop over woord
			std::vector<char>::iterator iterator_2 = letters.begin();
			while (iterator_2 != letters.end()) {
				if (toTest == (*iterator_2)) {
					curDup++;
				}
				iterator_2++;
			}

			if (curDup == 2) {
				if (doubles < 1) {
					result[0] += 1;
					doubles = 1;
				}			
			}
			else if (curDup >= 3) {
				if (triples < 1) {
					result[1] += 1;
					triples = 1;
				}				
			}
			iterator_1++;
		}
		triples = 0;
		doubles = 0;
		///////////////////////////////////////////////////////
	}
	std::cout << "double: " << result[0] << " Triple: " << result[1] << std::endl;
	in_stream.close();
}

void Day2::calculate2() {
	std::ifstream in_stream1;
	std::ifstream in_stream2;
	int same = 0;
	std::string line1;
	std::string line2;
	std::vector<int> list;

	in_stream1.open(FILE_READ);
	while (!in_stream1.eof()) {
		getline(in_stream1, line1);
		std::vector<char> letters_1(line1.begin(), line1.end());

		in_stream2.open(FILE_READ);
		while (!in_stream2.eof()) {
			getline(in_stream2, line2);
			std::vector<char> letters_2(line2.begin(), line2.end());
			int i = 0;
			std::vector<char>::iterator iterator = letters_2.begin();
			while (iterator != letters_2.end()) {
				if ((*iterator) == letters_1[i]) {
					if (letters_1 == letters_2) {
						//nothing
					}
					else {
						same++;
					}					
				}
				i++;
				iterator++;
				
			}
			if(same >= 25){
				for (std::vector<char>::iterator it = letters_1.begin(); it != letters_1.end(); ++it) {
					std::cout << *it;
				}
				std::cout << " :" << same << std::endl;
			}
			same = 0;			
		}
		in_stream2.close();
	}
}

Day2::~Day2()
{
}
