package Java;
import java.util.*;

public class switchh
{
    public static void main(String[] args) 
    {
        // Input from user
        Scanner sc = new Scanner(System.in);
        int button = sc.nextInt();

        switch (button)
        {
            case 1:System.out.println( "hii");
            break;
            case 2: System.out.println( "Hello");
            break;
            case 3: System.out.println("namaste");
            break;
            default: System.out.println("invalid");

        }
       
        sc.close();
    
    }
}