package MyMath;
import java.lang.Math;

class SqrRoot{
	public static void main(String args[]){

		double x=26.5, y;
		y=Math.sqrt(x);
		System.out.println("y= "+y);

		System.out.println("Sq root of "+args[0]+ " is " +Math.sqrt(Float.valueOf(args[0])));
	}
}