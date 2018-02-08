public class Supervisor extends Empleados {
	private int cantidadEmpleadosSupervisados;
	private static float bonoAntiguedad = 120;
	
	public Supervisor(int dni, String nombre, int nroLegajo, date fechaIngreso, float sueldoBruto, int cantidadEmpleadosSupervisados) {
		super(dni, nombre, nroLegajo, fechaIngreso, sueldoBruto)
		
		this.cantidadEmpleadosSupervisados = cantidadEmpleadosSupervisados;
	}	
	
	public Supervisor(int dni, String nombre, int nroLegajo, float sueldoBruto, int cantidadEmpleadosSupervisados) {
		super(dni, nombre, nroLegajo, sueldoBruto)
		
		this.cantidadEmpleadosSupervisados = cantidadEmpleadosSupervisados;
	}
	
	public void incrementarSueldo() {
		sueldoBruto = sueldoBruto * 1.10;
	}
	
	public int tributo() {
		tributo = sueldoBruto * 0.08;
	}
	
	public static float getBonoAntiguedad() {
	return Supervisor.bonoAntiguedad;
	}
	
	public static void setBonoAntiguedad(float bonoAntiguedad) {
		if(bonoAntiguedad > 0)
			Supervisor.bonoAntiguedad = bonoAntiguedad;
}
