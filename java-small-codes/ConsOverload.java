//Constructor Overloading

class Room{
	float len, wid;
	//Square shaped room
	Room(int x){	
		len = x;
		wid = x;
	}
	//Rctangular shaped room
	Room(int l, int w){
		len = l;
		wid = w;
	}
	float area(){
		return len*wid;
	}
}

class ConsOverload{
	public static void main(String args[]){
		Room sq = new Room(10);
		Room rec = new Room(12,10);
		float sq_area = sq.area();
		float rec_area = rec.area();
		System.out.println("Area of square shaped room : "+ sq_area);
		System.out.println("Area of rectangular shaped room : "+ rec_area);
	}
}