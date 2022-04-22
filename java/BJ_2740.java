import java.util.Scanner;

public class BJ_2740 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		int M = input.nextInt();
		int matrix1 [][] = new int[N][M];
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				matrix1[i][j] = input.nextInt();
			}
		}
		
		int B = input.nextInt();
		int K = input.nextInt();
		int matrix2 [][] = new int[B][K];
		
		for(int i = 0; i < B; i++) {
			for(int j = 0; j < K; j++) {
				matrix2[i][j] = input.nextInt();
			}
		}
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < K; j++) {
				int sum = 0;
				for(int k = 0; k < M; k++) {
					sum += matrix1[i][k] * matrix2[k][j];
				}
				System.out.print(sum + " ");
			}
			System.out.println();
		}
		
		input.close();
	}

}
