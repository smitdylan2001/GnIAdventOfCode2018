using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Puzzle1
{
    class Program
    {
        static void Main(string[] args)
        {
            int total = 0;
            bool done = false;
            Dictionary<int, int> frequency = new Dictionary<int, int>();
            string[] input = System.IO.File.ReadAllLines(@"input_puzzle_1.txt");

            //To get the answer to question 1, get rid of this while loop
            while (!done)
            {
                for (int i = 0; i < input.Length; i++)
                {
                    string temp = input[i];
                    int number = int.Parse(temp.Substring(1, temp.Length - 1));

                    if (temp[0] == '+')
                        total += number;
                    else
                        total -= number;

                    //Not interested in the value but we just use it to see if we have a particulary key already
                    int value;
                    if (frequency.TryGetValue(total, out value))
                    {
                        done = true;
                        break;
                    }
                    frequency.Add(total, i);
                }
            }
            Console.WriteLine(total);
            Console.ReadKey();
        }
    }
}
