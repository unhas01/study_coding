import java.io.*;

public class BJ_1100 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char str [][] = new char[8][8];
		
		int num = 0;
		
		for(int i = 0; i < str.length; i++) {
			String s = br.readLine();
			for(int j = 0; j < str[i].length; j++) {
				str[i][j] = s.charAt(j);
				if( (i+j) % 2 == 0 && str[i][j] == 'F' )
					num++;
			}
		}
		System.out.println(num);
	}

}
