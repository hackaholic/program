import java.io.*;
import java.util.*;

class OpenFile { 
	private String file;
        private FileInputStream f;

	OpenFile() {
		System.out.println("Provide a File");
		System.exit(1);
	}

	OpenFile(String file){
		this.file = file;
		try {
			this.f = new FileInputStream(this.file);
		}
		catch (Exception e){
			System.out.println(e);
                        System.exit(1);
		}
	}

	FileInputStream getFile() {
		return this.f;
		}

	void close() throws IOException {
		this.f.close();
	}
}

class BubbleSort {

	static void display(ArrayList<Integer> list){
		Iterator it = list.iterator();
		while(it.hasNext()){
			System.out.println(it.next());
                }
        }

	public static void main(String args[]) throws IOException {
		System.out.println("I will perform bubble sort");
                ArrayList<Integer> list = new ArrayList<Integer>();
		OpenFile f = new OpenFile("../sample1.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(f.getFile()));
		String s;
		while ((s = br.readLine()) != null){
			list.add(Integer.parseInt(s));

		}
		f.close();
		display(list);
		System.out.println("Sorting data");
		int n = list.size();
		int i = 0;
		boolean flag = false;
		System.out.println("total size: " + n);
		while(true){
			if(list.get(i) > list.get(i+1)){
				int temp = list.set(i, list.get(i+1));
				temp = list.set(i+1, temp);
				flag = true;
			}
		        i += 1;
			if(i == n-1){
				i = 0;
				if (!flag){
					break;
				}
				flag = false;
			} 

		}
		display(list);
	}
}
