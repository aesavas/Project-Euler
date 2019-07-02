import java.util.ArrayList;

/**
 * author: aesavas
 *
 * Problem 5:
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */

public class Main {

    public static void divible1to20()
    {
        ArrayList<Integer> listOfNumbers = new ArrayList<>();
        for (int i = 2; i <= 20; i++) {
            listOfNumbers.add(i);
        }
        ArrayList<Integer> factorList = new ArrayList<>();
        int numberOfFloor = 0;
        int factor = 2;
        int LSD = 1;
        while(true)
        {
            int notDivible = 0;
            for (int i = 0; i < listOfNumbers.size(); i++)
            {
                if (listOfNumbers.get(i) % factor == 0) {
                    int temp = listOfNumbers.get(i);
                    temp /= factor;
                    listOfNumbers.set(i, temp);
                    if (listOfNumbers.get(i) == 1) {
                        numberOfFloor += 1;
                    }
                }
                else
                {
                    notDivible += 1;
                }
            }
            if (notDivible == listOfNumbers.size()) {
                factor += 1;
            }
            else
            {
                factorList.add(factor);
            }
            if (numberOfFloor == listOfNumbers.size()) {
                break;
            }
        }
        for (int i = 0; i < factorList.size(); i++) {
            LSD *= factorList.get(i);
        }
        System.out.println(LSD + " is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.");

    }

    public static void main(String[] args) {
        divible1to20();
    }
}
