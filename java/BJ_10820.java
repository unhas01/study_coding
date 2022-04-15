import java.io.*;

public class BJ_10820 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = "";
		
		while( (str = br.readLine()) != null){
			char c [] = str.toCharArray();
			int small = 0, large = 0, num = 0, blank = 0;
			for(char t:c) {
				if('a' <= t && t <= 'z')
					small++;
				else if('A' <= t && t <= 'Z')
					large++;
				else if('0' <= t && t <= '9')
					num++;
				else
					blank++;
				
			}
			System.out.println(small + " " + large + " " + num + " " + blank);
		}
	}

}
