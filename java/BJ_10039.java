import java.io.*;

public class BJ_10039 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr[] = new int[5];
		
		int sum = 0;
		for(int i = 0; i < 5; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			if(arr[i] < 40) {
				arr[i] = 40;
			}
			sum += arr[i];
		}
		System.out.println(sum / 5);
	}

}
