using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Puzzle4
{
    public class Program
    {
        public static string[] sortedInput;
        public static int startSleep;
        public static int endSleep;
        static void Main(string[] args)
        {
            sortedInput = System.IO.File.ReadAllLines(@"input_puzzle_4.txt");
            List<Guard> guardList = new List<Guard>();
            List<int> idList = new List<int>();
            int currentGuard = -1;

            int bestGuard = 0;
            int bestTime = 0;

            int mostSleep = 0;
            int bestCombi = 0;

            //First sort the input
            Array.Sort(sortedInput);

            //Walk through the sorted input
            for(int i = 0; i < sortedInput.Length; i++)
            {
                //Determine the guard (possibly add him)
                if(sortedInput[i][19] == 'G')
                {
                    string[] temp = sortedInput[i].Split('#');
                    currentGuard = int.Parse(temp[1].Split(' ')[0]);

                    if(!idList.Contains(currentGuard))
                    {
                        idList.Add(currentGuard);
                        guardList.Add(new Guard(currentGuard));
                    }
                }

                //Set startTime
                if(sortedInput[i][19] == 'f')
                    startSleep = int.Parse(sortedInput[i].Substring(15,2));

                //Set endTime and note the time he slept
                if (sortedInput[i][19] == 'w')
                {
                    endSleep = int.Parse(sortedInput[i].Substring(15, 2));

                    for(int j = 0; j < guardList.Count(); j++)
                    {
                        if (guardList[j].id == currentGuard)
                            guardList[j].addTime();
                        else
                            continue;
                    }
                }
            }

            //Output calculations
            for (int i = 0; i < guardList.Count(); i++)
            {
                if(guardList[i].total > bestTime)
                {
                    bestTime = guardList[i].total;
                    bestGuard = i;
                }
                for (int j = 0; j < guardList[i].scheme.Count(); j++)
                {
                    if (guardList[i].scheme[j] > mostSleep)
                    {
                        mostSleep = guardList[i].scheme[j];
                        bestCombi = j * guardList[i].id;
                    }
                }
            }
            Console.WriteLine(guardList[bestGuard].bestTime() * guardList[bestGuard].id);
            Console.WriteLine(bestCombi);
            Console.ReadKey();
        }
    }

    public class Guard : Program
    {
        public int id;
        public int[] scheme;
        public int total;

        public Guard(int id)
        {
            this.id = id;
            scheme = new int[60];
            total = 0;
        }

        public void addTime()
        {
            for(int i = 0; i < endSleep - startSleep; i++)
            {
                scheme[startSleep + i]++;
                total++;
            }
        }

        //Return best possible minute to go
        public int bestTime()
        {
            int amount = 0;
            int bestMinute = 0;
            for (int i = 0; i < scheme.Length; i++)
            {
                if(scheme[i] > amount)
                {
                    amount = scheme[i];
                    bestMinute = i;
                }
            }
            return bestMinute;
        }
    }
}
