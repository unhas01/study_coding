import java.io.*;
import java.util.Scanner;

public class BJ_1932 {

	public static void main(String[] args) throws IOException{
		
		Scanner input = new Scanner(System.in);
		int N = input.nextInt();
		int num [][] = new int[N][];
		
		for(int i = 0; i < N; i++) {
			num[i] = new int[i + 1];
			for(int j = 0; j <= i; j++) {
				num[i][j] = input.nextInt();
			}
		}
		
		for(int i = N - 1; i > 0; i--) {
			for(int j = 0; j < i; j++) {
				num[i-1][j] += Math.max(num[i][j], num[i][j+1]);
			}
		}
		System.out.println(num[0][0]);
		
		input.close();
	}

}
