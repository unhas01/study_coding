import java.io.*;

public class BJ_2845 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int L = Integer.parseInt(s[0]);
		int P = Integer.parseInt(s[1]);
		
		int arr [] = new int[5];
		String temp [] = br.readLine().split(" ");
		for(int i = 0; i < 5; i++) {
			arr[i] = Integer.parseInt(temp[i]);
			System.out.print((arr[i] - L*P) + " ");
		}
	}

}
