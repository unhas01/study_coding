import java.io.*;

public class BJ_2475 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr[] = new int[5];
		String s [] = br.readLine().split(" ");
		for(int i = 0; i < 5; i++) {
			arr[i] = Integer.parseInt(s[i]);
		}
		
		int sum = 0;
		for(int i = 0; i < 5; i++) {
			sum += Math.pow(arr[i], 2);
		}
		System.out.println(sum % 10);
		
	}

}
