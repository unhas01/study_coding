import java.io.*;

public class BJ_10824 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str [] = br.readLine().split(" ");
		
		long n1 = Long.parseLong(str[0] + str[1]);
		long n2 = Long.parseLong(str[2] + str[3]);
		
		System.out.println(n1 + n2);
	}

}
