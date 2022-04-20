import java.util.Scanner;

public class BJ_2441 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		
		for(int i = N; i > 0; i--) {	// 5 4 3 2 1������ " "���
			for(int j = N; j > i; j--) {
				System.out.print(" ");
			}
			for(int j = 0; j < i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}

		input.close();
	}

}
