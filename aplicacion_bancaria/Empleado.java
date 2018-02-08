import java.util.Date;

public abstract class Empleado {
	private int dni;
	private String nombre;
	private int nroLegajo;
	private Date fechaIngreso;
	protected float sueldoBruto;
	
	public Empleado(int dni, String nombre, int nroLegajo, Date fechaIngreso, float sueldoBruto) {
		this.dni = dni;
		this.nombre = nombre;
		this.nroLegajo = nroLegajo;
		this.fechaIngreso = fechaIngreso;
		this.sueldoBruto = sueldoBruto;
	}
	
	public Empleado(int dni, String nombre, int nroLegajo, float sueldoBruto) {
		this.dni = dni;
		this.nombre = nombre;
		this.nroLegajo = nroLegajo;
		this.sueldoBruto = sueldoBruto;
		
		fechaIngreso = new Date();
	}
	
	public int getDni() {
		return dni;
	}
	
	public String getNombre() {
		return nombre;
	}
	
	public int getNroLegajo() {
		return nroLegajo;
	}
	
	public int getAntiguedad() {
		return antiguedad;
	}
	
	public float getSueldoBruto() {
		return sueldoBruto;
	}
	
	public abstract void incrementarSueldo();
	
	public abstract int getTributo();
	
	public abstract static void setBonoAntiguedad(float bonoAntiguedad);
	
	public abstract static float getBonoAntiguedad();
}
