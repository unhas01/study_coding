import java.util.Scanner; 

public class BJ_6359 { 
	
	public static void main(String[] args) { 
		Scanner scan = new Scanner (System.in); 
		int testCase = Integer.parseInt(scan.nextLine().trim()); 
		
		for(int ci=0; ci < testCase; ci++) { 
			int doorCount = Integer.parseInt(scan.nextLine().trim()); 
			boolean doorArray[] = new boolean[doorCount + 1]; 
			for(int i=2; i< doorArray.length; i++) { 
				int maxIndex = doorCount / i;
				for(int j=1; j <= maxIndex; j++) {
					if(doorArray[i*j] == true) 
						doorArray[i*j] = false; 
					else doorArray[i*j] = true; 
					} 
				} 
			int result = 0; 
			for(int i=1; i < doorArray.length; i++) {
				if(!doorArray[i]) result++;
			}
			System.out.println(result);
		} 
		scan.close(); 
	} 
}

