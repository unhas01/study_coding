import java.util.Scanner;

public class BJ_2444 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		
//		for(int i = 1; i <= N; i++) {
//			for(int j = 0; j < N-i; j++) {
//				System.out.print(" ");
//			}
//			for(int j = 0; j < i; j++) {
//				System.out.print("*");
//			}
//			for(int j = 1; j < i; j++) {
//				System.out.print("*");
//			}
//			for(int j = 1; j < N-i; j++) {
//				System.out.print(" ");
//			}
//			System.out.printlN();
//		}
//		for(int i = 1; i < N; i++) {
//			for(int j = 0; j < i; j++) {
//				System.out.print(" ");
//			}
//			for(int j = 0; j < N-i; j++) {
//				System.out.print("*");
//			}
//			for(int j = 1; j < N-i; j++) {
//				System.out.print("*");
//			}
//			for(int j = 1; j < i; j++) {
//				System.out.print(" ");
//			}
//			System.out.printlN();
//		}
		for(int i=0; i<N; i++) {
			for(int j=N-i-1; j>0; j--) {
				System.out.print(" ");
			}
			for(int k=N-1; k<N+i*2; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		for(int i=N+1; i<2*N; i++) {
			for(int k=0; k<i-N; k++) {
				System.out.print(" ");
			}
			for(int j=2*N-i*2+N*2-1; j>0; j--) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		input.close();
	}

}
