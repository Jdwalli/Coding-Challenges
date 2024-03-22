import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.io.IOException;
import java.nio.file.Files;

public class Solution {

    static int solvePartOne(String diagnosticReport) {
        String gammaRate = "";
        String epsilonRate = "";
        String[] diagnosticArray = diagnosticReport.split("\n");
        List<List<Integer>> indexesList = new ArrayList<>();

        for (int i = 0; i < diagnosticArray[0].length(); i++) {
            List<Integer> currentList = new ArrayList<>();
            for (String binaryValue : diagnosticArray) {
                if (!binaryValue.isEmpty() && i < binaryValue.length() - 1) {
                    int currentIndex = Character.getNumericValue(binaryValue.charAt(i));
                    currentList.add(currentIndex);
                }
            }
            indexesList.add(currentList);
        }

        for (int i = 0; i < indexesList.size() - 1; i++) {
            int zeroCount = 0;
            int oneCount = 0;
            for (Integer value : indexesList.get(i)) {
                if (value == 0) {
                    zeroCount++;
                } else if (value == 1) {
                    oneCount++;
                }
                
            }
            if (zeroCount > oneCount) {
                    gammaRate += "0";
                    epsilonRate += "1";
                } else {
                    gammaRate += "1";
                    epsilonRate += "0";
                }
        }
        return Integer.parseInt(gammaRate, 2) * Integer.parseInt(epsilonRate, 2);
    }

    static int solvePartTwo(String diagnosticReport) {
        return 0;
    }

    public static void main(String[] args) {
        String path = "input.txt";

        try {
            String fileContent = Files.readString(Paths.get(path));
            System.out.println("Part One Solution: " + solvePartOne(fileContent));
            System.out.println("Part Two Solution: " + solvePartTwo(fileContent));
            assert solvePartOne(fileContent) == 3959450;
            // assert solvePartTwo(fileContent) == 1956047400;
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}