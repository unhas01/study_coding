import java.io.*;

public class BJ_1010 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < T; i++) {
			String s[] = br.readLine().split(" ");
			int K = Integer.parseInt(s[0]);
			int N = Integer.parseInt(s[1]);
			
			int dp [][] = new int[N+1][K+1];
			for(int j = 0; j <= K; j++) {
				dp[j][j] = 1;
			}
			for(int j = 0; j <= N; j++) {
				dp[j][0] = 1;
			}
			for(int j = 2; j <= N; j++) {
				for(int k = 1; k <= K; k++) {
					dp[j][k] = dp[j-1][k-1] + dp[j-1][k];
				}
			}
			System.out.println(dp[N][K]);
		}
	}

}
