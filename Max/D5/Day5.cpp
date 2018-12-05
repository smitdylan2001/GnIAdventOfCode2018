#include "Day5.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>  
#include <string>
#define FILE_READ "/Users/Gebruiker/Desktop/ADVC_D5.txt"
Day5::Day5()
{
}

void Day5::calculate() {

	//OP 1
	//int len = 0;
	//setInput();
	//std::cout << data.size() << std::endl;
	//deleteStuff();
	//std::cout << data.size() <<  std::endl;	

	static const char* sAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	static const char* Alphabet = "abcdefghijklmnopqrstuvwxyz";

	std::vector<char> mAlphabet(sAlphabet, sAlphabet + 26);
	U_Alphabet = mAlphabet;

	std::vector<char> rAlphabet(Alphabet, Alphabet + 26);
	L_Alphabet = rAlphabet;



	deleteByLetter();
}

void Day5::setInput() {
	data.clear();
	typedef std::istream_iterator<char> istream_iterator;
	std::ifstream file(FILE_READ);

	file >> std::noskipws;
	std::copy(istream_iterator(file), istream_iterator(),
		std::back_inserter(data));
}

void Day5::deleteStuff() {
	std::vector<char>::iterator iterator = data.begin();
	while ((iterator) != data.end()) {
		char a;
		char b;
		if ((iterator +1) != data.end()) {
			a = (*iterator);
			iterator++;
			b = (*iterator);
			iterator--;
		}
		if (a != b) {
			if (a == toupper(b) || a == tolower(b)) {
				data.erase(iterator);
				data.erase(iterator);
				iterator = data.begin();
			}
			else {
				iterator++;
			}
		}
		else {
			iterator++;
		}		
	}
}

void Day5::deleteByLetter() {
	std::cout << U_Alphabet.size();
	for (int i = 0; i < U_Alphabet.size() -1; i++) {
		std::cout << "round" << std::endl;
		setInput();

		std::vector<char>::iterator iterator = data.begin();
		while ((iterator) != data.end()) {
			char A = U_Alphabet[i];
			char a = L_Alphabet[i];

			if ((*iterator) == A || (*iterator) == a) {
				data.erase(iterator);
				data.begin();
			}
			else {
				iterator++;
			}
			
		}

		deleteStuff();
		std::cout << data.size() <<" deleted" << L_Alphabet[i] << U_Alphabet[i] <<  std::endl;
	}
}

Day5::~Day5()
{
}
