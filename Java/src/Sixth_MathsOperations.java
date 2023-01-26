import javax.swing.JOptionPane;
import java.util.Scanner;

public class Sixth_MathsOperations {

		public static void main (String[] args) {
			
			double a = 3.14;
			double b = -89.5;
			
			double c = Math.max(a, b);			/*to assign value of the max of the two
												 *min would assign value of the min of the two
												 */
			
			double d = Math.abs(b);				// abs gives absolute value, modulus fnc
			
			double e = Math.sqrt(a);			//square root
			
			double f = Math.round(a);			/* would round to nearest integer
												 * Math.ceil would round to next greater integer
												 * Math.floor would round to previous smallest integer
												 */
			
			System.out.println(c);
			System.out.println(d);
			System.out.println(e);
			System.out.println(f);
			

			
					//GUI for hypotenuse calculation
			
			double x = Double.parseDouble(JOptionPane.showInputDialog(null, "Enter Side X"));
			double y = Double.parseDouble(JOptionPane.showInputDialog(null, "Enter Side Y"));
			double z = Math.sqrt((x*x)+(y*y));
			JOptionPane.showMessageDialog(null, "The hypotenuse is "+z+" units");
			
				
			
					//Scanner for hypotenuse calculation
	
			Scanner scanner = new Scanner(System.in);
			System.out.println("Enter side X");
			double i = scanner.nextDouble();
			scanner.nextLine();
			System.out.println("Enter side Y");
			double j = scanner.nextDouble();
			scanner.nextLine();
			double k = Math.sqrt((i*i)+(j*j));
			System.out.println("The hypotenuse is "+k+" units");
			scanner.close();
	
			
		}
}
