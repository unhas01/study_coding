import java.io.*;
import java.util.*;

public class BJ_1764 {

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s [] = br.readLine().split(" ");
		int N = Integer.parseInt(s[0]);
		int M = Integer.parseInt(s[1]);
		
        HashSet<String> set = new HashSet<>(); 
        for (int i = 0; i < N; i++) {
            set.add(br.readLine());
        }
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String str = br.readLine();
            if(set.contains(str)){
                result.add(str);
            }
        }
        Collections.sort(result);
		System.out.println(result.size());
		for(String a : result) {
			System.out.println(a);
		}
	}

}
