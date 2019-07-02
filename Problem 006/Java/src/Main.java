import java.util.ArrayList;

/**
 * author: aesavas
 *
 * Problem 6:
 * The sum of the squares of the first ten natural numbers is,
 *
 * 12 + 22 + ... + 102 = 385 --> 2 means square.
 * The square of the sum of the first ten natural numbers is,
 *
 * (1 + 2 + ... + 10)2 = 552 = 3025 --> 2 means square.
 * Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
 * 3025 − 385 = 2640.
 *
 * Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 */

public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> listOfNumber = new ArrayList<>();
        for (int i = 1; i <= 100; i++) {
            listOfNumber.add(i);
        }
        int total = 0;
        int squareTotal = 0;
        for (int i:listOfNumber)
        {
            total += i;
            squareTotal += Math.pow(i, 2);
        }
        int squareNumbersTotal = (int) Math.pow(total, 2);
        System.out.println("Result : "+squareNumbersTotal+" - "+squareTotal+" = "+(squareNumbersTotal-squareTotal));
    }
}
