using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Puzzle5
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = System.IO.File.ReadAllLines(@"input_puzzle_5.txt");
            int lowest = -1;

            for (int i = 0; i < 26; i++)
            {
		//Using a stack is way faster if you immediately check after pushing input
                List<int> polymer = new List<int>();
                //Make the list + leave out specific letters
                for (int j = 0; j < input[0].Length; j++)
                {
                    if (input[0][j] == 65 + i || input[0][j] == 97 + i)
                        continue;
                    polymer.Add(input[0][j]);
                }

                int leftPos = 0;
                int rightPos = 1;

                while (rightPos < polymer.Count())
                {
                    //32 is the difference in the ASCII table between lowercase and uppercase letters
                    if (polymer[leftPos] - polymer[rightPos] == 32 || polymer[leftPos] - polymer[rightPos] == -32)
                    {
                        //Delete right first otherwise the positions dont match
                        polymer.RemoveAt(rightPos);
                        polymer.RemoveAt(leftPos);

                        if (leftPos > 0)
                            leftPos--;
                    }
                    else
                        leftPos++;

                    rightPos = leftPos + 1;
                }
                Console.WriteLine("{0} : " + polymer.Count(), (char)(65 + i));
                if (polymer.Count() < lowest || lowest == -1)
                    lowest = polymer.Count();
            }

            Console.WriteLine("Lowest : " + lowest);
            Console.ReadKey();
        }
    }
}
