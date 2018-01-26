public class Fish extends Pet {
	private String typeWater;
	
	public Fish(String name, String race, int age, int weigth, String typeWater) {
		super(name, race, age, weigth);
		
		this.typeWater = typeWater;
	}
	
	public Fish(String name, String race, int weigth, String typeWater) {
		super(name, race, weigth);
		
		this.typeWater = typeWater;
	}
	
	public String talk() {
		return getName() + " dice: Gloo Gloo!";
	}
	
	public String getTypeWater() {
		return typeWater;
	}
}
