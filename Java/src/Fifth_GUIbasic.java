import javax.swing.JOptionPane;

public class Fifth_GUIbasic {
		
	public static void main (String[] args) {
		
		String name = JOptionPane.showInputDialog("Enter your name");					//for input with message 
		JOptionPane.showMessageDialog(null,"Hello "+name);								//for displaying message
		
		int age = Integer.parseInt(JOptionPane.showInputDialog("Enter your age"));		//Integer.parseInt() used to convert the string in () to int
		JOptionPane.showMessageDialog(null, "You are "+age+" years old");
		
		double height = Double.parseDouble(JOptionPane.showInputDialog("Enter your height (in meters)"));		//same for Double as above for Integer
		JOptionPane.showMessageDialog(null, "You are "+height+" meteres tall");
		
		
	}
}
