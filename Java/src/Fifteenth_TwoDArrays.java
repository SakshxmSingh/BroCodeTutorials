
public class Fifteenth_TwoDArrays {
	
	public static void main(String[]args) {
		
		//2D Arrays = A fucking matrix, its the horror all over again
		
		String[][] cars = 	{
								{"Urus", "Camaro", "Corvette"},
								{"Aventador", "Tesla", "AudiR8"},
								{"Chiron","Ferrari","McLarenP1"}
							 };

		for(int i=0; i<cars.length; i++ ) {
			System.out.println();
			
			for(int j=0; j<cars[i].length; j++ ) {
				System.out.print(cars[i][j]+"   ");
				}
			}
		
	}
}
