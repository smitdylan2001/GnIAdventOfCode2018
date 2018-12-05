#pragma once
#include <vector>
#include <boost\algorithm\string.hpp>
#include <iostream>
#include <fstream>
#include <stdlib.h>  
#include <string>
#include <algorithm>
#include <iomanip>  
class Day5
{
public:	
	Day5();
	void calculate();
	void deleteStuff();
	void deleteByLetter();
	~Day5();
	void setInput();
	std::string inputLine;
	std::string file_contents;
	std::vector<char> data;
	std::vector<char> U_Alphabet;
	std::vector<char> L_Alphabet;
};

