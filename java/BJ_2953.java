import java.io.*;

public class BJ_2953 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str [] = new String[5];
		int arr[] = new int[5];
		
		for(int i = 0; i < str.length; i++)
			str[i] = br.readLine();
		
		
		for(int i = 0; i < str.length; i++) {
			String temp [] = str[i].split(" ");
			int n1 = Integer.parseInt(temp[0]);
			int n2 = Integer.parseInt(temp[1]);
			int n3 = Integer.parseInt(temp[2]);
			int n4 = Integer.parseInt(temp[3]);
			
			arr[i] = n1 + n2 + n3 + n4;
		}
		
		int max = arr[0];
		int index = 0;
		
		for(int i = 1; i < arr.length; i++) {
			if(arr[i] > max) {
				max = arr[i];
				index = i;
			}
		}
		System.out.println((index+1)+ " " + max);
	}

}
