import java.util.Scanner;

public class Thirteenth_NestedLoops {
	
	public static void main(String[]args) {
		
		//nested loop = a loop inside a loop
		
		Scanner scanner = new Scanner(System.in);
		
		int rows;
		int columns;
		String symbol;
		
		System.out.print("Enter no of rows: ");
		rows = scanner.nextInt();
		System.out.print("Enter no of columns: ");
		columns = scanner.nextInt();
		System.out.print("Enter the symbol to make rectangle of: ");
		symbol = (scanner.next());
		
		for(int i=1; i<=rows; i++) {
			System.out.println();
			
			for(int j=1; j<=columns; j++) {
				System.out.print(symbol);
			}
		}
		scanner.close();
	}

}
