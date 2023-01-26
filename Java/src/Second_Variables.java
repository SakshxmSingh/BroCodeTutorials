
public class Second_Variables {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int x = 123;		/* int x; 	-------> declaration
							 *   +
							 * x = 123; -------> assignment
							 *   =
							 * int x = 123; ---> initialisation
							 */
														
		
		long w = 696969696969696969L;				//long is bigger version of int
		double y = 3.14;							//double is for fraction
		boolean z = true;
		char symbol = '@';							//for single character
		String name = "Bro";		
		
		System.out.println("Hello "+name);
		System.out.println("my number is "+ x);
		System.out.println("and my debt is "+w);
		
					//variable switching
		
		String a = "water";								
		String b = "Kool-Aid";
		String temp;
		
		temp = a;
		a=b;
		b=temp;
		
		System.out.println("a: "+a);
		System.out.println("b: "+b);
		

	}

}
