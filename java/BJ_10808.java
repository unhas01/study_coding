import java.io.*;

public class BJ_10808 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr [] = new int[26];
		String s = br.readLine();
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = 0;
		}
		
		for(int i = 0;i<s.length();i++) {
			arr[s.charAt(i)-97]++;
		}
		
		for(int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}

}
