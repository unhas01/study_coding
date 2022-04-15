import java.util.Scanner;

public class BJ_10992 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		
		for(int i = 1; i <= N; i++) {
			if(i == N) {
				for(int j = 1; j <= 2*i-1; j++) {
					System.out.print("*");
				}
				System.out.println();
				break;
			}
			
			for(int j = 1; j <= N-i; j++) {
				System.out.print(" ");
			}
			for(int j = 1; j <= 2*i-1; j++) {
				if(j == 1 || j == 2*i-1)
					System.out.print("*");
				else
					System.out.print(" ");
			}
			
			System.out.println();
			input.close();
		}
		
	}

}
