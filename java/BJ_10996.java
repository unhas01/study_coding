import java.util.Scanner;

public class BJ_10996 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		
		for(int i = 1; i <= 2*N; i++){
			if(i % 2 == 1){
				for(int j = 1; j <= N; j++){
					if(j % 2 == 1){
						System.out.print("*");
					}
					else{
						System.out.print(" ");
					}
				}
			}
			else{
				for(int j = 1; j <= N; j++){
					if(j % 2 == 1){
						System.out.print(" ");
					}
					else{
						System.out.print("*");
					}
				}
			}
			System.out.println();
		}
		
		input.close();
	}

}
