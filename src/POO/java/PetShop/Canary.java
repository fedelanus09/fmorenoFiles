public class Canary extends Pet {
	private String plumage;
	
	public Canary(String name, String race, int age, int weigth, String plumage) {
		super(name, race, age, weigth);
		
		this.plumage = plumage;
	}
	
	public Canary(String name, String race, int weigth, String plumage) {
		super(name, race, weigth);
		
		this.plumage = plumage;
	}
	
	public String talk() {
		return getName() + " dice: Pío Pío!";
	}
	
	public String getPlumage() {
		return plumage;
	}
}
