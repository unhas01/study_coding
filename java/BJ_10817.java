import java.io.*;
import java.util.Arrays;

public class BJ_10817 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int arr [] = new int [s.length];
		for(int i = 0; i < s.length; i++) {
			arr[i] = Integer.parseInt(s[i]);
		}
		Arrays.sort(arr);
		System.out.println(arr[1]);
	}

}
