import java.io.*;
class Reading{
	public static void main(String args[]){

		DataInputStream in = new DataInputStream(System.in);
		int a=0;
		float b=0f;
		try{

			System.out.println("Enter an integer");
			a = Integer.valueOf(in.readLine()).intValue();

			System.out.println("Enter a float ");
			b = Float.valueOf(in.readLine()).floatValue();
		}
		catch(Exception e){
			System.out.println("Error in input");
			//exit(0);
		}
		System.out.println("a= "+a);
		System.out.println("b= "+b);

	}
}