import java.io.*;

public class BJ_2455 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = new String[4];
		for(int i = 0; i < 4; i++) {
			s[i] = br.readLine();
		}
		
		int res = 0;
		int people = 0;
		
		for(int i = 0; i < 4; i++) {
			String temp [] = s[i].split(" ");
			int minus = Integer.parseInt(temp[0]);
			int plus = Integer.parseInt(temp[1]);
			people = people + plus - minus;
			
			res = Math.max(res, people);
		}
		
		System.out.println(res);
	}

}
//0 32
//3 13
//28 25
//39 0
//
//0+32 = 32
//32-3+13 = 42
//42-28+25 = 39
//39-39+0 = 0