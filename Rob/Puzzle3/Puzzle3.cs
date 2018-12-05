using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Puzzle3
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = System.IO.File.ReadAllLines(@"input_puzzle_3.txt");
            int[,] fabric = new int[1000,1000];
            List<int> idList = new List<int>();

            int total = 0;

            for (int i = 0; i < input.Length; i++)
            {
                string[] currentClaim = input[i].Split(' ');

                //Add all id's to a list
                int id = int.Parse(currentClaim[0].Substring(1, currentClaim[0].Length - 1));
                idList.Add(id);

                //Determine the starting position and size of the claim
                string position = currentClaim[2].Substring(0, currentClaim[2].Length - 1);
                int startX = int.Parse(position.Split(',')[0]);
                int startY = int.Parse(position.Split(',')[1]);
                int sizeX = int.Parse(currentClaim[3].Split('x')[0]);
                int sizeY = int.Parse(currentClaim[3].Split('x')[1]);

                for(int y = startY; y < startY + sizeY; y++)
                {
                    for(int x = startX; x < startX + sizeX; x++)
                    {
                        //If not claimed, claim it with your ID
                        if (fabric[x, y] == 0)
                            fabric[x, y] = id;
                        else
                        {
                            //otherwise remove both ID's from the list and mark it as overlap
                            idList.Remove(fabric[x, y]);
                            idList.Remove(id);
                            fabric[x, y] = -1;
                        }
                    }
                }
            }

            //Count all spaces marked as overlap
            for (int i = 0; i < 1000; i++)
                for (int j = 0; j < 1000; j++)
                    if (fabric[i,j] == -1)
                        total++;
            
            Console.WriteLine(total);
            Console.WriteLine(idList[0]);
            Console.ReadKey();
        }
    }
}
