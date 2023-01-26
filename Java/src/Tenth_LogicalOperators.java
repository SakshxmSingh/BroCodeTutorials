import java.util.Scanner;
public class Tenth_LogicalOperators {
	
	public static void main(String[] args) {
		
		/*	logical operators = used to connect two or more expressions
		 *
		 * 			&& = (AND) both conditions must be true
		 * 			|| = (OR) either condition must be true
		 * 			! = (NOT) reverses boolean value of condition
		 */
	
		
	/*----------------example 1--------------------------*
		int temp = 15;
		if(temp>30) {
			System.out.println("It is hot outside");
		}
		else if(temp>=20 && temp<=30) {									//both statements must be true
			System.out.println("It is warm outside");
		}
		else {
			System.out.println("It is cold outside");
		}
	 */	
		
		/*------------example 2--------------------------*
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("You are playing a game. Press q or Q to Quit");
		String response = scanner.nextLine();
		
		if(response.equals("q")||response.equals("Q")) {				//any one statement must be true
			System.out.println("You have quit the game");
		}
		else {
			System.out.println("you are still playing the game");
		}
		*/
		
		
		/*---------------example 3-----------------------*/
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("You are playing a game. Press q or Q to Quit");
		String response = scanner.nextLine();
		
		if(!response.equals("q")&&!response.equals("Q")) {				//any one statement must be true
			System.out.println("you are still playing the game.");
		}
		else {
			System.out.println("You have quit the game");
		}
		
		scanner.close();
		
	}
	

}
