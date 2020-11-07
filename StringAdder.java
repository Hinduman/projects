//This Java file calculates the sum of numbers seperated by comma(or newline) in form of string
//if u want to change the delimiter from  comma to <your wish> place it like below
//"//<your wish>\n<number><your wish><number>..." 
//or 
//"//[<your wish1>][<your wish2>]..[<your wishn>]\n<number><your wish1><number>..."

import java.util.Scanner;

public class CustomException extends Exception{
	public CustomException(String s){
		super(s);
	}
}

public class StringCalculator{
	public int cnt=0;
	public int Add(String str){
		if(str.isEmpty())
			return 0;
		else if(str.startsWith("//[")){
			int nl=str.indexOf("]\n");
			return Add(str.substring(nl+2,str.length()),str.substring(3,nl).split("\\]\\["));
		}
		else if(str.startsWith("//")){
			int nl=str.indexOf("\n");
			return Add(str.substring(nl+1,str.length()),str.substring(2,nl));
		}
		else {
			cnt++;
			int sum=0,i=0;
			int[] neg=new int[str.replace("\n",",").split(",").length];
			try {
				for(String s:str.replace("\n",",").split(","))
					if(Integer.parseInt(s)<0)
						neg[i++]=Integer.parseInt(s);
					else if(Integer.parseInt(s)<1000)
						sum+=Integer.parseInt(s);
			}
			catch(Exception ex){
				return 0;
			}
			
			try {
				if(neg[0]!=0)
					throw new CustomException("Negative's not Allowed");
			}
			catch(CustomException ce){
				for(int j:neg)
					if(j!=0)
						System.out.print(j+" ");
				System.out.print(":"+ce.getMessage()+". So, sum of remaining number's is :");
			}
			return sum;
		}
	}
	public int Add(String str,String regex){
		return Add(str.replace(regex,","));
	}
	public int Add(String str,String[] regex){
		for(String s:regex)
			str=str.replace(s,",");
		return Add(str);
	}
	public int GetCalledCount(){
		return cnt;
	}
}

public class StringAdder{
	public static void main(String[] args){
		Scanner s=new Scanner(System.in);
		StringCalculator sc=new StringCalculator();
		System.out.println(sc.Add(""));
		System.out.println(sc.Add("1,2,3"));
		System.out.print("Give a string that has numbers seperated by ',':");
		int ans=sc.Add(s.next());
		System.out.println("Sum to your string is:"+ans);
		System.out.println(sc.Add("1\n2,3\n4"));
		System.out.println(sc.Add("//;\n56;33;2"));
		System.out.println(sc.Add("23,-43,3"));
		System.out.println(sc.Add("-45,67,-4,-78,7"));
		System.out.println("Add() function was called "+sc.GetCalledCount()+" times");
		System.out.println(sc.Add("23,56,1043,54"));
		System.out.println(sc.Add("//[***]\n4***5***7"));
		System.out.println(sc.Add("//[*][%]\n34*45%43"));
		System.out.println(sc.Add("//[^^][$$]\n55$$34^^23"));
	}
}

