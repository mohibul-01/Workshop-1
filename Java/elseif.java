package Java;
import java.util.*;

public class elseif
{
    public static void main(String[] args) 
    {
        //Input from user
        Scanner sc = new Scanner(System.in);
        int button = sc.nextInt();
        
        if ( button == 1){
            
            System.out.println("Hello");

        }
        else if ( button == 2){
            
            System.out.println("Namaste");

        }
        else if ( button == 3 ){
            
            System.out.println( "Hola");
        }
        else {
            
            System.out.println("Invalid");
        }
         sc.close();
    }
}