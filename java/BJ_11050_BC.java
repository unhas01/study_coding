import java.io.*;

public class BJ_11050_BC {

	static int dp [][];
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int N = Integer.parseInt(s[0]);
		int K = Integer.parseInt(s[1]);
		
		dp = new int [N+1][K+1];
		
		// bottom-up
		for (int i = 0; i <= K; i++) {
			dp[i][i] = 1;
		}
		
		// 2번 성질 (k == 0)
		for(int i = 0; i <= N; i++) {
			dp[i][0] = 1;
		}
		
 
		for (int i = 2; i <= N; i++) {
			for (int j = 1; j <= K; j++) {
				// 1번 성질
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
			}
		}
		
		System.out.println(dp[N][K]);
		
//		System.out.println(BC(N,K));	top down���
	}
	// top-down
//	static int BC(int n, int k) {
//		if (dp[n][k] > 0) {
//			return dp[n][k];
//		}
// 
//		if (k == 0 || n == k) {
//			return dp[n][k] = 1;
//		}
//
//		return dp[n][k] = BC(n - 1, k - 1) + BC(n - 1, k);
//	}
	
}
