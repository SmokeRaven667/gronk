using System;
using System.Collections.Generic;
					
public class Program
{
	
	
	public static int minimumCoins(int input) {
		List<int> denominations = new() {
			25,
			10,
			5,
			1
		};
		int minimumCoins = 0;
		int tempInput = input;
		foreach(int denomination in denominations) {
			while(tempInput >= denomination) {
				if (input - denomination >= 0) {
					minimumCoins = minimumCoins + 1;
					tempInput = tempInput - denomination;
				}
			}
		}
		return minimumCoins;
	}


	public static void Main()
	{
		int min = minimumCoins(17);
		Console.WriteLine(min);
	}
}