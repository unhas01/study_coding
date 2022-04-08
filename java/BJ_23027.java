import java.io.*;

public class BJ_23027 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s = br.readLine();
		
		if(s.contains("A")) {
			s = s.replace("B", "A");
			s = s.replace("C", "A");
			s = s.replace("D", "A");
			s = s.replace("F", "A");
		}
		if(!s.contains("A") && s.contains("B")) {
			s = s.replace("C", "B");
			s = s.replace("D", "B");
			s = s.replace("F", "B");
		}
		if(!s.contains("A") && !s.contains("B") && s.contains("C")) {
			s = s.replace("D", "C");
			s = s.replace("F", "C");
		}
		if(!s.contains("A") && !s.contains("B") && !s.contains("C")) {
			String A = "A";
			s = s.replaceAll(s, A.repeat(s.length()));
		}
		
		System.out.println(s);
	}

}
