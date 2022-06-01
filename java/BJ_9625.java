import java.io.*;

public class BJ_9625 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int dp1 [] = new int[N];	// A
		int dp2 [] = new int[N];	// B
		
		dp1[0] = 0;
		dp2[0] = 1;
		
		for(int i = 1; i < N; i++) {
			dp1[i] = dp2[i-1];
			dp2[i] = dp1[i-1] + dp2[i-1]; 
		}
		System.out.println(dp1[N-2] + " " + dp2[N-2]);
		System.out.println(dp1[N-1] + " " + dp2[N-1]);
	}

}
// dp