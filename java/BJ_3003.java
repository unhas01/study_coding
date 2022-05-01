import java.io.*;

public class BJ_3003 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str [] = br.readLine().split(" ");
		
		int piece [] = {1, 1, 2, 2, 2, 8};
		
		for(int i = 0; i < str.length; i++) {
			int temp = Integer.parseInt(str[i]);
			int res = piece[i] - temp;
			System.out.print(res + " ");
		}
	}

}
