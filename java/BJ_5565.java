import java.io.*;

public class BJ_5565 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int total = Integer.parseInt(br.readLine());
		int arr [] = new int[9];
		
		for(int i = 0; i < 9; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			total -= arr[i];
		}
		System.out.println(total);
	}

}
