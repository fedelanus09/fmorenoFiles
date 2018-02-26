package com.ljv.controlador;

import java.util.ArrayList;

public class LiquidadorSueldos {
	private ArrayList<Empleado> empleados;
	
	public LiquidadorSuelds() {
		empleados = new ArrayList<Empleado>();
	}
	
	public int buscarPosicionEmpleado(Empleado empleado) {
		for(int i = 0; i < empleados.size(); i++) {
			if(empleados[i].getDNI() == empleado)
				return 1;
		}
		
		return -1
	}
	
	public void altaEmpleado(Empleado empleado) {
		
	}

}
