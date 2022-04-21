import java.io.*;
import java.util.Arrays;

public class BJ_2576 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr [] = new int[7];
		
		for(int i = 0; i < 7; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		int cnt = 0;
		int sum = 0;
		Arrays.sort(arr);
		int min = arr[6];
		for(int i = 0; i < 7; i++) {
			if(arr[i] % 2 == 1) {
				cnt++;
				sum += arr[i];
				min = Math.min(min, arr[i]);
			}	
		}
		
		if(cnt == 0) {
			System.out.println("-1");
		}
		else {
			System.out.println(sum);
			System.out.println(min);
		}
		
		
	}

}
