public class ReciboSueldo {
	public static void main(String args[]) {
		Operario operario = new Operario(24765918, "Alberto Mendoza", 1,"22-10-12", 20000, "produccion");
		
		System.out.println(operario.getNroLegajo());
		System.out.println(operario.getNombre());
		System.out.println(operario.getDni());
		System.out.println(operario.getAntiguedad());
		System.out.println(operario.getTipoEmpleado());
		
		System.out.println(operario.getDetalle());
		
		System.out.println(operario.getSueldoBruto());
		System.out.println(operario.getTributo());
		System.out.println(operario.getBonoAntiguedad());
		System.out.println(operario.getSueldoNeto());
	}
}
