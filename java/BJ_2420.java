import java.io.*;

public class BJ_2420 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		
		long N = Integer.parseInt(s[0]);
		long M = Integer.parseInt(s[1]);
		
		System.out.println(Math.abs(N-M));
	}

}
