import java.io.*;

public class BJ_1924 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int x = Integer.parseInt(s[0]);
		int y = Integer.parseInt(s[1]);
		
		int day [] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		String week [] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
		
		int totalday = y;
		
		for(int i = 0; i < x - 1; i++) {
			totalday += day[i];
		}
		
		System.out.println(week[totalday % 7]);
	}

}
