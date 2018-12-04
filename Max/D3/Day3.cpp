#include "Day3.h"



//Disclaimer, ik ben los gegaan met de while loops.
//Be warned ik weet dat dit verre van netjes is :D



#define FILE_READ "/Users/Gebruiker/Desktop/ADVC_D3.txt"

Day3::Day3()
{
}

void Day3::calculate1() {

	//Vul nonOverlap
	in_stream_1.open(FILE_READ);
	while (!in_stream_1.eof()) {
		getline(in_stream_1, line_1);
		nonOverlap.push_back(line_1);
	}
	in_stream_1.close();


	std::cout << "Can take a while | RUN IN RELEASE x64" << std::endl;
	std::cout << "Working: ";

	//Open bestand 1
	in_stream_1.open(FILE_READ);
	while (!in_stream_1.eof()) {
		getline(in_stream_1, line_1);

		//split string line_1
		//[3] and [4] are positions
		//[6] and [7] are size
		//Ontclutteren
		boost::algorithm::split(result_1, line_1, boost::is_any_of(", @:x"));

		//breedte
		intHold_1 = std::stoi(result_1[3]);
		aBase = intHold_1;
		a = intHold_1;
		b = intHold_1;
		b += std::stoi(result_1[6]);
		
		//Lengte
		intHold_1 = std::stoi(result_1[4]);
		cBase = intHold_1;
		c = intHold_1;
		d = intHold_1;
		d += std::stoi(result_1[7]);
		

		//Open file again to compare (Lokaal opslaan is goedkoper dan deze oplossing)
		in_stream_2.open(FILE_READ);
		while (!in_stream_2.eof()) {
			getline(in_stream_2, line_2);

			//split string line_1
			//[3] and [4] are positions
			//[6] and [7] are size
			boost::algorithm::split(result_2, line_2, boost::is_any_of(", @:x"));

			//breedte
			intHold_1 = std::stoi(result_2[3]);
			iBase = intHold_1;
			i = intHold_1;
			x = intHold_1;
			
			//Lengte
			intHold_1 = std::stoi(result_2[4]);
			yBase = intHold_1;
			y = intHold_1;
			z = intHold_1;

			intHold_1 = std::stoi(result_2[6]);
			intHold_2 = std::stoi(result_2[7]);
		
			x += intHold_1;
			z += intHold_2;


			//Test niet jezelf
			if (line_1 != line_2) {
				test = (intHold_1 * intHold_2);
				//Breedte File 2
				while(i < x) { //hey een loop

					//Lengte File 2
					while (y < z) { //Okey, nog een loop

						//Breedte File 1
						while (a < b) { //Nu is het wel veel

							//Lengte File 1
							while(c < d) { //Oh pleas stop de loops
								if (a == i && c == y) {
									//Als er een overlap is, haal 1 weg van test zodat de string wordt verwijderd uit de nonOverlap vector<string>
									test += - 1;
									tempIntVect = { a,y };

									//Dit is duur, Loopt bij wijze van spreken 1.000.000 vlakken af, honderde keren per vlak. (ouch)
									if (std::find(overlaps.begin(), overlaps.end(), tempIntVect) != overlaps.end() == false) {
										overlap++;
										overlaps.push_back(tempIntVect);
									}								
								}
								c++;
							}
							c = cBase;
							a++;
						}
						a = aBase;
						y++;
					}
					y = yBase;
					i++;
				}
				i = iBase;
				
				//Verwijder string uit nonOverlap als test kleiner is dan de x en y grote van het vlak.
				if (test != (intHold_1 * intHold_2)) {
					std::vector<std::string>::iterator result = find(nonOverlap.begin(), nonOverlap.end(), line_1);
					if (result != nonOverlap.end()) {
						nonOverlap.erase(result);
						std::cout << "|";
					}				
				}
				test = 0;
			}
		}
		in_stream_2.close();
	}
	std::cout << std::endl;
	std::cout << "Overlapping square inches: " << overlap << std::endl;

	std::vector<std::string>::iterator iterator = nonOverlap.begin();
	while (iterator != nonOverlap.end()) {
		std::cout << (*iterator) << " Does not overlap| Knip maar lekker raak!" << std::endl;
		iterator++;
	}
}

Day3::~Day3()
{
}
