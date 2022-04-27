import java.io.*;

public class BJ_5554 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t1 = Integer.parseInt(br.readLine());
		int t2 = Integer.parseInt(br.readLine());
		int t3 = Integer.parseInt(br.readLine());
		int t4 = Integer.parseInt(br.readLine());
		
		int sum = t1 + t2 + t3 + t4;
		
		System.out.println(sum / 60);
		System.out.println(sum % 60);
	}

}
