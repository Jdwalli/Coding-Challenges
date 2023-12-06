import java.nio.file.Paths;
import java.io.IOException;
import java.nio.file.Files;


public class Solution {


    static int solvePartOne(String sonarData) {
        String[] data = sonarData.split("\n");
        int increases = 0;

         for (int i = 0; i < data.length - 1; i++) {
            int current = Integer.valueOf(data[i].trim());
            int next = Integer.valueOf(data[i + 1].trim());

            if (next > current) {
                increases += 1;
            }
        }

        return increases; 
    }

    static int solvePartTwo(String sonarData) {
        String[] data = sonarData.split("\n");
        int increases = 0;
        int value = 0;

        for (int i = 0; i < data.length - 2; i++) {
            int windowValue = Integer.parseInt(data[i].strip()) + Integer.parseInt(data[i + 1].strip()) + Integer.parseInt(data[i + 2].strip());
            if (windowValue > value) {
                increases += 1;
            } 
            value = windowValue;
          }

        return increases - 1; 
    }

    

	public static void main(String[] args) {
		String path = "input.txt";

        try {
            String fileContent = Files.readString(Paths.get(path));
            System.out.println("Part One Solution: " + solvePartOne(fileContent));
            System.out.println("Part Two Solution: " + solvePartTwo(fileContent));
            assert solvePartOne(fileContent) == 1676;
            assert solvePartTwo(fileContent) == 1706;
        } catch (IOException  e) {
            e.printStackTrace();
        }


	}
}