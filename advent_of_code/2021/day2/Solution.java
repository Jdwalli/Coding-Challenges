import java.nio.file.Paths;
import java.io.IOException;
import java.nio.file.Files;

public class Solution {

    static int solvePartOne(String submarineCommands) {
        int horizontalPosition = 0;
        int depth = 0;
        String[] commands = submarineCommands.split("\n");

        for (String command : commands) {
            String[] splitCommands = command.split(" ");
            String direction = splitCommands[0].strip();
            int value = Integer.parseInt(splitCommands[1].strip());

            if (direction.equals("forward")) {
                horizontalPosition += value;
            }

            if (direction.equals("down")) {
                depth += value;
            }

            if (direction.equals("up")) {
                depth -= value;
            }
        }

        return horizontalPosition * depth;
    }

    static int solvePartTwo(String submarineCommands) {
        int horizontalPosition = 0;
        int depth = 0;
        int aim = 0;
        String[] commands = submarineCommands.split("\n");

        for (String command : commands) {
            String[] splitCommands = command.split(" ");
            String direction = splitCommands[0].strip();
            int value = Integer.parseInt(splitCommands[1].strip());

            if (direction.equals("forward")) {
                horizontalPosition += value;
                depth += (aim  * value);
            }

            if (direction.equals("down")) {
                aim += value;
            }

            if (direction.equals("up")) {
                aim -= value;
            }


        }

        return horizontalPosition * depth;
    }

    public static void main(String[] args) {
        String path = "input.txt";

        try {
            String fileContent = Files.readString(Paths.get(path));
            System.out.println("Part One Solution: " + solvePartOne(fileContent));
            System.out.println("Part Two Solution: " + solvePartTwo(fileContent));
            assert solvePartOne(fileContent) == 1654760;
            assert solvePartTwo(fileContent) == 1956047400;
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}