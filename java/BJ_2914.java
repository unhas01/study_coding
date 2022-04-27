import java.io.*;

public class BJ_2914 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int n1 = Integer.parseInt(s[0]);
		int n2 = Integer.parseInt(s[1]);
		
		System.out.println(n1 * (n2 - 1) + 1);
		
	}

}
