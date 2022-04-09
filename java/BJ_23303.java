import java.io.*;

public class BJ_23303 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s = br.readLine();
		
		boolean chk1 = s.contains("d2");
		boolean chk2 = s.contains("D2");
		
		if(chk1 || chk2) {
			System.out.println("D2");
		}else {
			System.out.println("unrated");
		}
		
		
	}

}
