/**
 * author: aesavas
 *
 * Problem 7:
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 *
 * What is the 10001st prime number?
 */

public class Main {

    public static boolean isPrimeNumber(int number)
    {
        int limit = (int) (Math.sqrt(number)+1);
        for (int i = 2; i < limit ; i++) {
            if (number % i == 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int counter = 1;
        int number = 2;
        while(counter != 10002)
        {
            if (isPrimeNumber(number)) {
                counter++;
                number++;
            }
            else{
                number++;
            }
        }
        System.out.println("10001st prime number is : "+ (number-1));
    }
}
