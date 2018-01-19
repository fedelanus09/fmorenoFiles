public class PetShop {
	public static void main(String args[]) {
		Dog myDog = new Dog();
		
		myDog.name = "Pichula";
		myDog.race = "Obejero alemán";
		myDog.age = 5;
		myDog.weight = 30;
		
		myDog.bark();
		
		System.out.println(myDog.name);
		System.out.println(myDog.race);
		System.out.println(myDog.age);
		System.out.println(myDog.weight);
	}
}
