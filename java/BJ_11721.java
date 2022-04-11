import java.io.*;

public class BJ_11721 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s = br.readLine();
		
		for(int i = 0; i < s.length(); i++){
			char c = s.charAt(i);
			System.out.print(c);
			if(i % 10 == 9) {
				System.out.println();
			}
		}
	}

}
