import java.io.IOException;
import java.util.Scanner;

public class BJ_10798 {

	public static void main(String[] args) throws IOException{
		

		Scanner sc = new Scanner(System.in);
		char c [][] = new char[5][15];
		
		int max_length = Integer.MIN_VALUE;
    	
        for(int i = 0; i < 5; i++) {
            String s = sc.nextLine().trim();
            max_length = Math.max(max_length, s.length());
            for(int j = 0; j < s.length(); j++) {
                c[i][j] = s.charAt(j);
            }
        }
        for(int i = 0; i < max_length; i++) {
            for(int j = 0; j < 5; j++) {
                if(c[j][i] == '\0')
                    continue;
                System.out.print(c[j][i]);
            }
        }

        sc.close();
	}

}
