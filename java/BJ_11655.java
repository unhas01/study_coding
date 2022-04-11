import java.io.*;

public class BJ_11655 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String S = br.readLine();
		
		for(int i = 0; i < S.length(); i++) {
			int ascii = S.charAt(i);
			
			if(ascii >= 65 && ascii <= 90) {
				ascii += 13;
				if(ascii > 90) {
					int temp = ascii - 91;
					ascii = 65 + temp;
				}
			}
			else if(ascii >= 97 && ascii <= 122) {
				ascii += 13;
				if(ascii > 122) {
					int temp = ascii - 123;
					ascii = 97 + temp;
				}
			}
			System.out.print((char)ascii);
		}
	}

}
