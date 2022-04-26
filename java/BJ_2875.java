import java.io.*;

public class BJ_2875 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str [] = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		int k = Integer.parseInt(str[2]);
		
		int max =  n/2 < m ? n/2 : m; 
		k -= n + m - max*3;
		
		while(k > 0) {
			k -= 3; max--;
		}		
		System.out.print(max);
	}

}
