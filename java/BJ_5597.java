import java.io.*;

public class BJ_5597 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int arr [] = new int[30];
		for(int i = 0; i < 30; i++) {
			arr[i] = i;
		}
		
		for(int i = 0; i < 28; i++) {
			int n = Integer.parseInt(br.readLine());
			arr[n-1] = 0;
		}
		int index [] = new int[2];
		int j = 0;
		for(int i = 0; i < 30; i++) {
			if(arr[i] != 0) {
				index[j] = i;
				j++;
			}
		}
		
		System.out.println(Math.min(index[0], index[1])+1);
		System.out.println(Math.max(index[0], index[1])+1);

	}

}
