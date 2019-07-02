/**
 * author: aesavas
 *
 * Problem 3:
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 */

public class Main {

    public static void findLargestPrimeFactor(long number)
    {
        int largest = 0;
        int factor = 2;
        while (number >= factor)
        {
            if (number % factor == 0)
            {
                largest = factor;
                number /= factor;
            }
            else
                factor += 1;
        }
        System.out.println("Largest prime factor : " + largest);
    }
    public static void main(String[] args) {
        findLargestPrimeFactor(600851475143L);
    }
}
