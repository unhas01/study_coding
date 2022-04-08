import java.io.*;
import java.util.Arrays; 

public class BJ_1026 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int A [] = new int[N];
		int B [] = new int[N];
		
		String a [] = br.readLine().split(" ");
		for(int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(a[i]);
		}
		String b [] = br.readLine().split(" ");
		for(int i = 0; i < N; i++) {
			B[i] = Integer.parseInt(b[i]);
		}
		
		Arrays.sort(A);
		Arrays.sort(B);
		
		int sum = 0;
		for(int i = 0; i < N; i++) {
			sum += A[i] * B[N - 1 - i];
		}
		
		System.out.println(sum);
	}

}
