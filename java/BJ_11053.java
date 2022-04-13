import java.io.*;

public class BJ_11053 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int arr [] = new int[N];
		
		String s [] = br.readLine().split(" ");
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(s[i]);
		}
		
		int dp [] = new int[N];
		dp[0] = 1;
		
		for(int i = 1; i < N; i++) {
			dp[i] = 1;
			for (int j = 0; j < i; j++) {
				if (arr[j] < arr[i] && dp[i] <= dp[j]) {
					dp[i] = dp[j] + 1;
				}
			}
		}
		
		int max = 0;
		for(int i : dp) {
			max = Math.max(max, i);
		}
		System.out.println(max);
	}

}

//
//6
//10 20 10 30 20 50
//1
//2
//2
//3
//3
//4

// 1 2 1 3 2 4
