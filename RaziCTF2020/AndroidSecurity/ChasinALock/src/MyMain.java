
public class MyMain {
	public static void main(String[] args) {
		//a1 a1Var = new a1();
        //a2 a2Var = new a2();
        //System.out.println(a2Var.run(i));
        //System.out.println(a1Var.run(0));
		/*
        int i = 0;
        a2 a2Var = new a2();
        //System.out.println(a2Var.run(i));
        String str = (" " + a1Var.run(i)) + a2Var.run(i);
        a3 a3Var = new a3();
        String str2 = str + a3Var.run(i);
        a4 a4Var = new a4();
        String str3 = str2 + a4Var.run(i);
        System.out.println(str3);
        a5 a5Var = new a5();
        System.out.println(str3 + a5Var.run(i)); 
        */
        int i = 0;
        a1 a1Var = new a1();
        a2 a2Var = new a2();
        String str = (" " + a1Var.run(i)) + a2Var.run(i);
        a3 a3Var = new a3();
        String str2 = str + a3Var.run(i);
        a4 a4Var = new a4();
        String str3 = str2 + a4Var.run(i);
        a5 a5Var = new a5();
        System.out.println(str3 + a5Var.run(i));
        
        
	}
}
