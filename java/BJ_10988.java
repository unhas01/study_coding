import java.io.*;

public class BJ_10988 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String text = br.readLine();
		
		String temp = "";
		
		for(int i = text.length()-1; i >= 0; i--) {
			temp += text.charAt(i);
		}
		
		if(text.equals(temp))	System.out.println("1");
		else					System.out.println("0");
		
	}

}
