import java.io.*;

public class BJ_2745 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str [] = br.readLine().split(" ");
		String N = str[0];
		int B = Integer.parseInt(str[1]);
		int res = 0;
		for(int i = 0; i < N.length(); i++) {
			if('0' <= N.charAt(i) && '9' >= N.charAt(i))
				res = res * B + (N.charAt(i)-'0');
			else
				res = res * B + (N.charAt(i)-'A'+10);
		}
		
		System.out.println(res);
		
	}

}
