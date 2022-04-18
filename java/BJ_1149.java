import java.io.*;

public class BJ_1149 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
//		int dp [] = new int[N];
		
		int rgb [][] = new int[N][3];
		
		for(int i = 0; i < rgb.length; i++) {
			String s [] = br.readLine().split(" ");
			rgb[i][0] = Integer.parseInt(s[0]);
			rgb[i][1] = Integer.parseInt(s[1]);
			rgb[i][2] = Integer.parseInt(s[2]);
		}
		
		for(int i = 1; i < N; i++) {
			rgb[i][0] += Math.min(rgb[i-1][1] , rgb[i-1][2]);
			rgb[i][1] += Math.min(rgb[i-1][0] , rgb[i-1][2]);
			rgb[i][2] += Math.min(rgb[i-1][0] , rgb[i-1][1]);
		}
		
		System.out.println(Math.min(Math.min(rgb[N-1][0], rgb[N-1][1]), rgb[N-1][2]));
		
	}

}
