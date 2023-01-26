import java.util.Scanner;
import javax.swing.JOptionPane;

public class Eight_IfStatements {
	
	public static void main (String[] args) {
		
		// if-else statement ---> performs a block of code if it's condition evaluates to be true
		
		
		int agex = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter age."));
		if (agex>=50) {
			JOptionPane.showMessageDialog(null, "Ok Boomer.");
		}
		else if (agex>=18) {
			JOptionPane.showMessageDialog(null, "You're an adult!!");
		}
		else {
			JOptionPane.showMessageDialog(null, "Grow up kid.");
		}
		
		
		
		
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter your age:");
		int age = scanner.nextInt();
		
		if (age>=50) {
			System.out.println("Ok Boomer.");
		}
		else if (age>=18) {
			System.out.println("You're an adult!!");
		}
		else {
			System.out.println("Grow up kid.");
		}
		scanner.close();
		
		
	}

}
