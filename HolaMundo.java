import java.util.ArrayList;
import java.util.List;

public class HolaMundo {

	public static void main(String[] args) {		
		//Scanner sc = new Scanner(System.in);
		//System.out.println("Ingresa un numero: ");
		//int numero1 = sc.nextInt();
		//System.out.println("Ingresa un numero: ");
		//int numero2 = sc.nextInt();

		//int suma = numero1 / numero2;
		//System.out.println("La suma da como resultado: " + suma);

		//sc.close();

		List<Integer> numeros = new ArrayList<>();
		numeros.add(5);
		numeros.add(9);
		numeros.add(3);
		numeros.add(4);
		numeros.add(7);

		int suma = 0;
		for(int numero:numeros){
			suma +=numero;

		}
		System.out.println("La suma es:"+suma);
		






	}

}