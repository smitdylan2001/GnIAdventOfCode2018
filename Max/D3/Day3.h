#pragma once
#include <boost\algorithm\string.hpp>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>  
#include <string>
#include <algorithm>
#include <iomanip>  

class Day3
{
public:
	void calculate1();
	Day3();
	~Day3();

	//Square inches die overlappen
	int overlap = 0;

	//test grote van vlak
	int test = 0;

	//Posities voor vlak loop 1
	int a, b, c, d = 0;
	//Posities voor vlak loop 2
	int i, x, y, z = 0;
	//Om de Posities te resetten het volgende vlak
	int aBase, cBase, iBase, yBase = 0;

	//File input, 2 omdat ik tegelijk 2 files open trek.
	std::ifstream in_stream_1, in_stream_2;

	//Voor de getline uit de bestanden.
	std::string line_1, line_2;

	//Om alle belangerijke strings in te bewaren zonder clutter
	std::vector<std::string> result_1, result_2;

	//Om de std::stoi maar 1 keer uit te voeren per loop.
	int intHold_1, intHold_2;


	//Vector met alle regels uit het bestand om één voor één weg te halen.
	std::vector<std::string> nonOverlap;

	//Hier bewaar ik alle posities van de vlakken in
	std::vector<std::vector<int>> overlaps;

	//bewaart de huidige coordinaat om op te zoeken en te testen of hij overlapt
	std::vector<int> tempIntVect;
};

