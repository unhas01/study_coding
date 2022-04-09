import java.io.*;
import java.util.*;

public class BJ_20205 {
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int N = Integer.parseInt(s[0]);
		int K = Integer.parseInt(s[1]);
		
		String str [] = new String[N];
		for(int i = 0; i < N; i++) {
			str[i] = br.readLine();
		}
		
		for(int i = 0; i < N; i++) {
			String res = "";
			StringTokenizer st = new StringTokenizer(str[i], " ");
			//int n = st.countTokens();
			while(st.hasMoreTokens()) {
				res += (st.nextToken() + " ").repeat(K);	
			}
			for(int j = 0; j < K; j++) {
				System.out.println(res);
			}
		}
		
		
		
	}

}
