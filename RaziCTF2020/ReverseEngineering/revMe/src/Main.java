package revMe;

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	
	
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        System.out.print("Enter Flag: ");
        String YourFlag = myObj.nextLine();
        String OurWiredFlag="↳᨟࿤୘ᅨ࿤୘ᅨ࿤୘├࿤୘⌷࿤୘ᭂ࿤୘ᅨ࿤୘⑚࿤୘⌷࿤୘⚠࿤୘69524࿤୘⯮࿤୘68187࿤୘⌷࿤୘ᦾ࿤୘⮍࿤୘⣦࿤୘⌷࿤୘⩪࿤୘68187࿤୘⯮࿤୘65513࿤୘⣦࿤୘76209≵";
        
        System.out.println("Decoded Flag: " + decode(OurWiredFlag));
        
        if(encode(mess(YourFlag)).equals(OurWiredFlag)){
            System.out.println("RaziCTF{"+YourFlag+"}");
            System.out.println("here is the flag take it :)");
        }
        else {
            System.out.println("Try more you can do it!");
        }
    }
    public static String clean(String str){
        /*can you help clean my mess it will help you with flag :)*/
        return null;
    }
    public static String mess(String str){
        char a[]=str.toCharArray();
        int b=a.length;
        char fin[]=new char[b];
        int i=0;
        int j=1;
        int k=0;
        while (true){
            try {
                if (i%2==0){
                    fin[(b/2)-k]=a[i];
                    k++;
                }else if (i%2==1){
                    fin[(b/2)+j]=a[i];
                    j++;
                }
                else {
                    fin[i]= (char) (a[i]%5);
                }
                    i++;
            }catch (Exception e) {
                return Arrays.toString(a);
            }
        }
    }
    public static boolean CHECK(char str){
        int[] a=new int[10];
        for (int i=0;i<10;i++){
            a[i]=i+1;
        }
        try {
            int i=0;
            while (true){
                i++;
                String b=String.valueOf(str);
                String c=String.valueOf(a[i-1]);
                if(b.equals(c)){
                    return true;
                }
            }
        }catch (Exception ex){

            return false;
        }
    }
    public static String decode(String str){
    	int len = str.length();
    	String[] arr = new String[10];
        StringBuilder fin= new StringBuilder();
        for (int i=0; i<10 ;i++){
        	char ch = (char) (i + 48);
            arr[i] = String.valueOf(ch * 1337);
        }
    	String flag = "";
    	int index = 1;
    	String sub1 = "";
    	while (index < len){
    		sub1 = "";
    		if (index+5 <= len){
    			sub1 = str.substring(index, index+5);
    		}
    		else{
    			index = index + 2;
    		}
    		Boolean b = true;
    		for (int i = 0; i < sub1.toCharArray().length; i++) {
				if (!CHECK(sub1.charAt(i)) &&  sub1.charAt(i) != '0'){
					b = false;
					break;
				}
			}
    		
    		if (b == true){
    			for (int i = 0; i < arr.length; i++) {
    				if (arr[i].equals(sub1)){
    					flag += String.valueOf(i);
    					index = index + 7;
    					break;
    				}
    			}
			}
    		else{
    			int i = (int)(str.charAt(index))+ 200 ;
    			char res = (char)(i/97);
    			flag += res;
    			index = index+3;
    		}
    	}
        return flag;
    }
    public static String encode(String str){
        StringBuilder fin= new StringBuilder();
        for (int i=0; i<str.toCharArray().length;i++){
            if(CHECK(str.charAt(i))){
                char ch=str.charAt(i);
                fin.append(String.valueOf(ch * 1337));
            }
            else {
                fin.append((char)((str.charAt(i)*'a')-200));
            }
        }
        
        return fin.toString();
    }
    
    
}