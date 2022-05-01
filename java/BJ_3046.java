import java.io.*;

public class BJ_3046 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s[] = br.readLine().split(" ");
		int R1 = Integer.parseInt(s[0]);
		int S = Integer.parseInt(s[1]);	
		
		int R2 = 0;
		R2 = S*2 - R1;
		
		System.out.println(R2);
	}

}
