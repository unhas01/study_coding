import java.io.*;

public class BJ_2960 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int N = Integer.parseInt(s[0]);
		int K = Integer.parseInt(s[1]);
		boolean b [] = new boolean[N+1];
		int cnt = 0;
		for(int i = 2; i <= N; i++) {
			b[i] = true;
	    }
		for(int i = 2; i <= N; i++) {
			for(int j = i; j <= N; j += i) {
				if(!b[j])
					continue;
				b[j] = false;
				cnt++;
				if(cnt == K) {
					System.out.println(j);
					break;
				}
			}
		}
		
	}

}
