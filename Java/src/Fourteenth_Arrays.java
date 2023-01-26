
public class Fourteenth_Arrays {
	
	public static void main(String[]args) {
		
		//arrays = used to store multiple values in a single variable
		
	/*	String[] cars = {"Tesla","Camaro","Urus"};					//one way to write and assign an array
		System.out.println(cars[0]);								//would print the first entry in array, as entries start with '0'
	 */	
		
		String[] cars = new String[3];								//another way to assign a new array, [3] represents no of elements or length
		cars[0]= "Tesla";											//[0] represents element no
		cars[1]= "Camaro";
		cars[2]= "Urus";
		
		for(int i=0; i<cars.length; i++) {								
			System.out.println(cars[i]);							//for loop to print all the contents of an array
			
		}
	}

}
