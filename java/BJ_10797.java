import java.io.*;

public class BJ_10797 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String str [] = br.readLine().split(" ");
		int cnt = 0;
		
		for(int i = 0; i < str.length; i++) {
			int t = Integer.parseInt(str[i]);
			if(N == t)
				cnt++;
		}
		
		System.out.println(cnt);
		
	}

}
