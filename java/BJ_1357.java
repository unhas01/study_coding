import java.io.*;

public class BJ_1357 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str [] = br.readLine().split(" ");
		String X = str[0];
		String Y = str[1];
		
		StringBuffer sb = new StringBuffer(X);
		String revX = sb.reverse().toString();
		sb = new StringBuffer(Y);
		String revY = sb.reverse().toString();
		
		int sum = Integer.parseInt(revX) + Integer.parseInt(revY);
		
		String result = String.valueOf(sum);
		sb = new StringBuffer(result);
		String revResult = sb.reverse().toString();
		int intResult = Integer.parseInt(revResult);
		System.out.println(intResult);
	}

}
