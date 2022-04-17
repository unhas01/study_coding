import java.util.Scanner;

public class BJ_2523 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		
		for(int i = 1; i <= N; i++) {
			for(int j = 1; j <= i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		for(int i = 1; i < N; i++) {
			for(int j = 1; j <= N - i; j++ ) {
				System.out.print("*");
			}
			System.out.println();
		}
		input.close();
	}

}
// 3 -> 5 = 3 + 2
// 4 -> 7 = 4 + 3
// 5 -> 9 = 5 + 4