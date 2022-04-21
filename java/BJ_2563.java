import java.util.Scanner;

public class BJ_2563 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int n = input.nextInt();
        int[][] map = new int[100][100];
        int cnt = 0;
    	
        for(int i = 0; i < n; i++) {
            int x = input.nextInt();
            int y = input.nextInt();
            for(int j = x; j < x + 10; j++) {
                for(int k = y; k < y + 10; k++) {
                    if(map[j][k] == 1)
                        continue;
                    map[j][k] = 1;
                    ++cnt;
                }
            }
        }
        System.out.println(cnt);
        
        input.close();
	}

}
