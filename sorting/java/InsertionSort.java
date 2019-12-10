import java.util.*;
import java.io.*;

class InsertionSort {

	static void display(ArrayList<Integer> list){
		for( int x: list){
			System.out.println(x);
		}

	}
	public static void main(String argv[]) throws IOException {
		File file = new File("../sample1.txt");
	        ArrayList<Integer> list = new ArrayList<Integer>();
		try {
			Scanner s = new Scanner(file);
			while(s.hasNext()){
				list.add(s.nextInt());
			}
			s.close();

	        }

	        catch (Exception e){
		        System.out.println(e);
		        System.exit(1);
	        }
		display(list);
		int n = list.size();
		for(int i=0;i<n-1;i++){
			if(list.get(i) > list.get(i+1)){
				int tmp = list.set(i, list.get(i+1));
				tmp = list.set(i+1, tmp);
				int k = i;
				while(k>0 && (list.get(k-1) > list.get(k))){
					tmp = list.set(k-1, list.get(k));
                                        tmp = list.set(k, tmp);
					k-=1;
				}
			}
		}

		display(list);

	}
}
