/**
 * author: aesavas
 *
 * Problem 4:
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
 * is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
 *
 */
public class Main {

    public static void Palindrome()
    {
        int largest = 0, result = 0;
        String resultString = "", invResultString = "";

        for (int i = 100; i < 1000; i++)
        {
            for (int j = 100; j < 1000 ; j++)
            {
                result = i * j;
                resultString = String.valueOf(result);  /**Convert int to string */
                StringBuilder builder = new StringBuilder();   /**Create StringBuilder to reverse string */
                builder.append(resultString);
                builder = builder.reverse();
                invResultString = builder.toString();
                if (resultString.equalsIgnoreCase(invResultString) && result > largest) {
                    largest = result;
                }
            }
        }
        System.out.println("Largest Palindrome Number is : " + largest);
    }
    public static void main(String[] args) {
        Palindrome();
    }
}
