public class Operario extends Empleado {
	private String tipoMaquina;
	private static float bonoAntiguedad = 100;
	
	public Operario(int dni, String nombre, int nroLegajo, Date fechaIngreso, float sueldoBruto, String tipoMaquina) {
		super(dni, nombre, nroLegajo, fechaIngreso, sueldoBruto)
		
		this.nombreMaquina = nombreMaquina;
	}	
	
	public Operario(int dni, String nombre, int nroLegajo, float sueldoBruto, String tipoMaquina) {
		super(dni, nombre, nroLegajo, sueldoBruto)
		
		this.nombreMaquina = nombreMaquina;
	}
	
	public void incrementarSueldo() {
		sueldoBruto *= 1.08;
	}
	
	public int tributo() {
		tributo = sueldoBruto * 0.05;
	}
	
	public static float getBonoAntiguedad() {
		return Operario.bonoAntiguedad;
	}
	
	public static void setBonoAntiguedad(float bonoAntiguedad) {
		if(bonoAntiguedad > 0)
			Operario.bonoAntiguedad = bonoAntiguedad;
	}
}
