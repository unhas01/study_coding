import java.io.*;

public class BJ_5543 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr [] = new int [5];
		for(int i = 0; i < 5; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		int b = Math.min(Math.min(arr[0], arr[1]), arr[2]);
		int d = Math.min(arr[3], arr[4]);
		System.out.println(b+d-50);
		
	}

}
