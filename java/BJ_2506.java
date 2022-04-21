import java.io.*;
import java.util.StringTokenizer;

public class BJ_2506 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int arr [] = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for(int i = 0; i < arr.length; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		
		int sum = 0;
		int jump = 1;
		
		if(arr[0] == 1)
			sum = 1;
		else
			sum = 0;
		
		for(int i = 1; i < arr.length; i++) {
			if(arr[i] == 1) {
				if(arr[i-1] == 1) {
					jump++;
				}
				sum += arr[i]*jump;
			}
			else {
				jump = 1;
			}
		}
		
		System.out.println(sum);
	}

}
