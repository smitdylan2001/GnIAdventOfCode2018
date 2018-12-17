using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Puzzle2
{
    class Program
    {
        static void Main(string[] args)
        {
            int doubles = 0;
            int triples = 0;
            int total = 0;
            List<string> boxID = new List<string>();

            string[] input = System.IO.File.ReadAllLines(@"input_puzzle_2.txt");

            for(int i = 0; i < input.Length; i++)
            {
                int temp_doubles = 0;
                int temp_triples = 0;
                Dictionary<char, int> frequency = new Dictionary<char, int>();
                string currentString = input[i];

                //Determine the frequency of all characters
                for(int j = 0; j < currentString.Length; j++)
                {
                    char key = currentString[j];
                    int value;

                    if (!frequency.TryGetValue(key, out value))
                        frequency.Add(key, 1);
                    else
                        frequency[key]++;
                }

                //See if you have doubles or triples
                for(int j = 0; j < frequency.Count(); j++)
                {
                    char key = currentString[j];
                    if (frequency[key] == 2)
                        temp_doubles++;
                    if (frequency[key] == 3)
                        temp_triples++;
                }

                //Add to the total doubles or triples
                if (temp_doubles > 0)
                    doubles++;
                if (temp_triples > 0)
                    triples++;
                if (temp_doubles > 0 || temp_triples > 0)
                    boxID.Add(currentString);
            }

            //Check the difference between all ID's
            //Slow solution of n^2 but it does have an early stop
            bool done = false;
            for(int x = 0; x < boxID.Count(); x++)
            {
                for(int y = x + 1; y < boxID.Count(); y++)
                {
                    int difference = 0;
                    for(int i = 0; i < boxID[x].Length; i++ )
                    {
                        if (boxID[x][i] == boxID[y][i])
                            continue;
                        else
                            difference++;
                    }
                    if(difference == 1)
                    {
                        for (int i = 0; i < boxID[x].Length; i++)
                        {
                            if (boxID[x][i] == boxID[y][i])
                                Console.Write(boxID[x][i]);
                            else
                                continue;
                        }
                        Console.WriteLine();
                        done = true;
                        break;
                    }
                }
                if (done)
                    break;
            }
            total = doubles * triples;
            Console.WriteLine(total);
            Console.ReadKey();
        }
    }
}
