/**
 * author: aesavas
 *
 * Problem 9:
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 *
 * a2 + b2 = c2 --> 2s means square.
 * For example, 32 + 42 = 9 + 16 = 25 = 52. --> 2s means square.
 *
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 */
public class Main {

    public static void main(String[] args) {
        int total = 1000;
        for (int i = 1; i < (total/3)+1; i++) //'a' can be maximum 333
        {
            for (int j = i+1; j < (total/2)+1; j++) //range must be start a+1 because a < b
            {
                int x = total - (i + j);
                if(Math.pow(i, 2) + Math.pow(j, 2) == Math.pow(x, 2))
                {
                    System.out.println("A : "+i+"\nB :"+j+"\nC :"+x);
                    System.out.println("ABC : "+ i*j*x);
                    i = 333; // because we want to break other for loop
                    break;
                }
            }
        }
    }
}
