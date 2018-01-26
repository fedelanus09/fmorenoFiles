public class PetShop {
	public static void main(String args[]) {
		Dog myDog = new Dog("Pichula", "Orejero Aleman", 2, 2, "Largo");
		
		System.out.println(myDog.talk());
		
		System.out.println(myDog.getName());
		System.out.println(myDog.getRace());
		System.out.println(myDog.getAge());
		System.out.println(myDog.getWeigth());
		System.out.println(myDog.getHairLength());
		
		myDog.eat();
		myDog.age();
		System.out.println(myDog.talk());
		
		System.out.println(myDog.getName());
		System.out.println(myDog.getRace());
		System.out.println(myDog.getAge());
		System.out.println(myDog.getWeigth());
		System.out.println(myDog.getHairLength());
		
		myDog.poop(2);
		System.out.println(myDog.getWeigth());
		
		Cat myCat = new Cat("Manchita", "Siames", 3, 3, "Celestes");
		
		System.out.println(myCat.talk());
		
		System.out.println(myCat.getName());
		System.out.println(myCat.getRace());
		System.out.println(myCat.getAge());
		System.out.println(myCat.getWeigth());
		System.out.println(myCat.getEyeColor());
		
		myCat.eat();
		myCat.age();
		System.out.println(myCat.talk());
		
		System.out.println(myCat.getName());
		System.out.println(myCat.getRace());
		System.out.println(myCat.getAge());
		System.out.println(myCat.getWeigth());
		System.out.println(myCat.getEyeColor());
		
		myCat.poop(2);
		System.out.println(myCat.getWeigth());
		
		Fish myFish = new Fish("Nemo", "Dorado", 4, 4, "Agua Dulce");
		
		System.out.println(myFish.talk());
		
		System.out.println(myFish.getName());
		System.out.println(myFish.getRace());
		System.out.println(myFish.getAge());
		System.out.println(myFish.getWeigth());
		System.out.println(myFish.getTypeWater());
		
		myFish.eat();
		myFish.age();
		System.out.println(myFish.talk());
		
		System.out.println(myFish.getName());
		System.out.println(myFish.getRace());
		System.out.println(myFish.getAge());
		System.out.println(myFish.getWeigth());
		System.out.println(myFish.getTypeWater());
		
		myFish.poop(2);
		System.out.println(myFish.getWeigth());
		
		Canary myCanary = new Canary("Alberto", "Roller", 5, 5, "Rizado");
		
		System.out.println(myCanary.talk());
		
		System.out.println(myCanary.getName());
		System.out.println(myCanary.getRace());
		System.out.println(myCanary.getAge());
		System.out.println(myCanary.getWeigth());
		System.out.println(myCanary.getPlumage());
		
		myCanary.eat();
		myCanary.age();
		System.out.println(myCanary.talk());
		
		System.out.println(myCanary.getName());
		System.out.println(myCanary.getRace());
		System.out.println(myCanary.getAge());
		System.out.println(myCanary.getWeigth());
		System.out.println(myCanary.getPlumage());
		
		myCanary.poop(2);
		System.out.println(myCanary.getWeigth());
	}
}
