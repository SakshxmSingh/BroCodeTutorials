
import java.util.Scanner;

public class Third_UserInput {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scanner = new Scanner(System.in);			//scanner util needs to be imported before using scanner
		
		System.out.println("what is your name?");
		String name = scanner.nextLine();
		
		System.out.println("what is your age?");
		int age = scanner.nextInt();
		scanner.nextLine();									//done to empty the scanner.nextLine() before next step
		
		System.out.println("What food do you like?");
		String food = scanner.nextLine();
		
		
		System.out.println("Hello "+name);
		System.out.println("Your age is "+age);
		System.out.println("Yoou like "+food);
		
		scanner.close();
		
					
	}

}
