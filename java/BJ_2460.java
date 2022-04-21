import java.io.*;
import java.util.Arrays;

public class BJ_2460 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr [] = new int[10];
		
		for(int i = 0; i < arr.length; i++) {
			String str [] = br.readLine().split(" ");
			int minus = Integer.parseInt(str[0]);
			int plus = Integer.parseInt(str[1]);
			
			if(i == 0)
				arr[i] = plus - minus;
			else if(i >= 1) {
				arr[i] = arr[i - 1] + plus - minus;
			}
		}
		
		Arrays.sort(arr);
		System.out.println(arr[9]);
	}

}
