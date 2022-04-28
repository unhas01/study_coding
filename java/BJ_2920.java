import java.io.*;

public class BJ_2920 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int arr [] = new int[8];
		for(int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(s[i]);
		}
		String res = "";
		
		for(int i = 0; i < arr.length - 1; i++) {
			if(arr[i+1] == arr[i] + 1) {
				res = "ascending";
			}
			else if(arr[i+1]== arr[i] - 1) {
				res = "descending";
			}
			else {
				res = "mixed";
				break;
			}
		}
		System.out.println(res);
	}

}
