import java.util.*;
import java.io.*;
import java.nio.file.*;
public class ImageEditor {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);  
        int count = 0;
        int newValue = 0;
       
        if (args.length != 3) { // 1
            System.out.println("Usage: java -cp bin ImageEditor {-i|-h|-g} infile outfile");
            System.exit(1);
        }
       
        String flag = args[0];
        String inputFile = args[1];
        String outputFile = args[2];
       
        if (flag != "-i" && flag != "-h" && flag != "-g") { // 2
            System.out.println("Usage: java -cp bin ImageEditor {-i|-h|-g} infile outfile");
            System.exit(1);
        }
       
        if (inputFile.substring(inputFile.length() - 4, inputFile.length()).equals(".ppm")) { // 3
            System.out.println("Invalid input file extension");
            System.exit(1);
        }
       
        if (outputFile.substring(outputFile.length() - 4, outputFile.length()).equals(".ppm")) { // 4
            System.out.println("Invalid output file extension");
            System.exit(1);
        }
 
        Path path = Path.of(args[1]); // 5
        if (!Files.exists(path)) {
            System.out.print("Unable to access input file: " + inputFile + "\n");
            System.exit(1);
        }
       
        boolean overwriteOkay = false; // 6
        path = Path.of(args[2]);
        if (Files.exists(path)) {
            System.out.println(args[2] + " exists - OK to overwrite ");
            System.out.print("(y,n)?: ");
            String overwrite = scnr.next();
           
            if (overwrite.charAt(0) != 'Y' && overwrite.charAt(0) != 'y') {
                System.exit(1);
            }
            else {
                overwriteOkay = true;
            }
        }
       
       
        // CHANGE BELOW
       
        if (overwriteOkay || !Files.exists(path))  {    // if ok to overwrite or file does not exist yet
            Scanner input = null;
            PrintWriter output = null;
            try {   // 7
                input = new Scanner(new FileInputStream(args[1]));
            }
            catch (FileNotFoundException e) {
                System.out.println("Cannot create output file");
                System.exit(1);
            }
           
            try {  // CHANGE LATER DON'T NEED
                FileOutputStream outputStream = new FileOutputStream(args[2]);
                output = new PrintWriter(outputStream);
            }
            catch (IOException e) {
                System.out.println("Cannot create output file");
                System.exit(1);
            }
           
            if (flag == "-i") {
                newValue = 0;
                    while (input.hasNextInt()) {
                        String format = input.nextLine();  
                        int cols = input.nextInt();  
                        int rows = input.nextInt();
                        // int invertedToken = invert(token);
                        // newValue = invertedToken;
                        int[][] pixels = new int[rows][3 * cols];
                        pixels = getPixelValues(input);
                        invert(pixels);
                    }
                    input.close();
                    try {
                        FileOutputStream outputStream = new FileOutputStream(args[2]);
                        output = new PrintWriter(outputStream);
                    }
                    catch (IOException e) {
                        System.out.println("Cannot create output file");
                        System.exit(1);
                    }
         //           output.print(pixels);
           //         output.close();
            }
           
    /*        if (flag == "-i") {
                newValue = 0;
                    while (input.hasNextInt()) {
                        String format = input.nextLine();  
                        int token = input.nextInt();  
                        int invertedToken = invert(token);
                        newValue = invertedToken;
                    }
                    input.close();
                    try {
                        FileOutputStream outputStream = new FileOutputStream(args[2]);
                        output = new PrintWriter(outputStream);
                    }
                    catch (IOException e) {
                        System.out.println("Cannot create output file");
                        System.exit(1);
                    }
                    output.print(newValue);
                    output.close();
            }
           
                        if (flag == "-i") {
                newValue = 0;
                    while (input.hasNextInt()) {
                        String format = input.nextLine();  
                        int token = input.nextInt();  
                        int invertedToken = invert(token);
                        newValue = invertedToken;
                    }
                    input.close();
                    try {
                        FileOutputStream outputStream = new FileOutputStream(args[2]);
                        output = new PrintWriter(outputStream);
                    }
                    catch (IOException e) {
                        System.out.println("Cannot create output file");
                        System.exit(1);
                    }
                    output.print(newValue);
                    output.close();
            }
        } */
           
           
  /*          
            // SEPARATION = ANITA CODE UNTIL NEXT CAPS COMMENT
           
            String operation = "";
            while (!operation.equalsIgnoreCase("Q")) {
                System.out.println("\nCipher - Please enter an operation below.");
                System.out.println();
                System.out.println("R - Reverse all lines");
                System.out.println("F - Shift all letters forward");
                System.out.println("B - Shift all letters backward");
                System.out.println("Q - Quit");
                System.out.print("\nOperation: ");
                operation = scnr.next();
           
                if (operation.equalsIgnoreCase("R")) {
                    count++;
                    if (count >= 2) {
                        try {
                            input = new Scanner(new FileInputStream(args[1]));
                        }
                        catch (FileNotFoundException e) {
                            System.out.println("Input file is not found");
                            System.exit(1);
                        }
                    }
                    str = "";
                    while (input.hasNextLine()) {
                        String line = input.nextLine();  
                        String reversedString = reverseLine(line);
                        str += reversedString + "\n";
                    }
                    input.close();
                    try {
                        FileOutputStream outputStream = new FileOutputStream(args[1]);
                        output = new PrintWriter(outputStream);
                    }
                    catch (IOException e) {
                        System.out.println("Cannot create output file");
                        System.exit(1);
                    }
                    output.print(str);
                    output.close();
                }                
                else if(operation.equalsIgnoreCase("F")) {
                    System.out.print("Shift amount (1-25): ");
                    if (!scnr.hasNextInt()) {
                        System.out.println("Invalid amount");
                        scnr.next();
                        continue;
                    }
                    else {
                        int shiftNum = scnr.nextInt();
                        if (shiftNum < SHIFT_LOWER_BOUND || shiftNum > SHIFT_UPPER_BOUND) {
                            System.out.println("Invalid amount");
                            continue;
                        }
                        count++;
                        if (count >= 2) {
                            try {
                                input = new Scanner(new FileInputStream(args[1]));
                            }
                            catch (FileNotFoundException e) {
                                System.out.println("Input file is not found");
                                System.exit(1);
                            }
                        }
                        str = "";
                        while (input.hasNextLine()) {
                            String line = input.nextLine();  
                            String forwardShifted = shiftLineLettersForward(line, shiftNum);
                            str += forwardShifted + "\n";
                        }
                        input.close();
                        try {
                            FileOutputStream outputStream = new FileOutputStream(args[1]);
                            output = new PrintWriter(outputStream);

                        }
                        catch (IOException e) {
                            System.out.println("Cannot create output file");
                            System.exit(1);
                        }
                           
                        output.print(str);
                        output.close();
                    }
                }
                else if (operation.equalsIgnoreCase("B")) {
                    System.out.print("Shift amount (1-25): ");
                    if (!scnr.hasNextInt()) {
                        System.out.println("Invalid amount");
                        scnr.next();
                        continue;
                    }
                    else {              // is an integer
                        int shiftNum = scnr.nextInt();
                        if (shiftNum < SHIFT_LOWER_BOUND || shiftNum > SHIFT_UPPER_BOUND) {
                            System.out.println("Invalid amount");
                            continue;
                        }
                        count++;
                        if (count >= 2) {
                            try {
                                input = new Scanner(new FileInputStream(args[1]));
                            }
                            catch (FileNotFoundException e) {
                                System.out.println("Input file is not found");
                                System.exit(1);
                            }
                        }
                        str = "";
                        while (input.hasNextLine()) {
                            String line = input.nextLine();  
                            String backwardShifted = shiftLineLettersBackward(line, shiftNum);
                            str += backwardShifted + "\n";
                        }
                        input.close();
                        try {
                            FileOutputStream outputStream = new FileOutputStream(args[1]);
                            output = new PrintWriter(outputStream);
                        }
                        catch (IOException e) {
                            System.out.println("Cannot create output file");
                            System.exit(1);
                        }
                        output.print(str);
                        output.close();
                    }
                }
                else if (operation.equalsIgnoreCase("Q")) {
                    //quits while loop
                }
                else {
                    System.out.println("Invalid operation");
                }
            }
   
        }
       
       // CHANGE ABOVE */
    }
    }
   
    /** Throws an IllegalArgumentException with the message
     * "Null file" if in is null
     * Reads and validates the ppm file and returns
     * a 2D array containing the pixel RGB values
     * The number of elements in each row of the array
     * will be 3 * the number of columns of pixels, since
     * 3 integers are used to represent each pixel.
     * Returns null, if any of the following are true
     *  - the first token in the file is not the string "P3"
     *   - the second token in the file, which represents the
     *    number of columns, is not an integer
     *  - the third toke in the file, which represents the
     *    number of rows, is not an integer
     *  - the fourth token in the file is not the integer 255
     *  - the fourth token is not followed by
     *    rows * cols * 3 integer values in the range 0 - 255
     * Any remaining tokens may be ignored.  
     */  
    public static int[][] getPixelValues(Scanner in) {
        if (in == null) {
            throw new IllegalArgumentException ("Null file");
        }
       
        while (in.hasNextInt()) {
            String format = in.nextLine();  
            int cols = in.nextInt();  
            int rows = in.nextInt();  
           
            int[][] pixels = new int[rows][3 * cols];
       
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < pixels[0].length; j++) {
                    pixels[i][j] = in.nextInt();
                }
            }

        return pixels;  
        }                  
}
   
    /** Throws an IllegalArgumentException with the message
     * "Null array" if pixels is null
     * Throws an IllegalArgumentException with the message
     * "Jagged array" if the pixels array is "jagged", i.e.,
     * each row does not have the same number of elements as
     * every other row.
     * NOTE: You must check for invalid parameters (arguments) in the order given above.
     * Inverts each of the RGB values in the pixels array
     */
    public static void invert(int[][] pixels) {    
        int rows = pixels.length;
        int cols = pixels[0].length;
        if (pixels == null) {
            throw new IllegalArgumentException ("Null array");
        }
        for (int i = 1; i < rows; i++) {
            if (pixels[i].length != cols) {
                throw new IllegalArgumentException ("Jagged array");
            }
        }
       
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                pixels[i][j] = 255 - pixels[i][j];
            }
        }
        outputPPM(PrintWriter out,pixels);
    }
   
    /** Throws an IllegalArgumentException with the message
     * "Null array" if pixels is null
     * Throws an IllegalArgumentException with the message
     * "Jagged array" if the pixels array is "jagged", i.e.,
     * each row does not have the same number of elements as
     * every other row.
     * NOTE: You must check for invalid parameters (arguments) in the order given above.
     * Converts the RGB values in the pixels array to high contrast
     */
    public static void highContrast(int[][] pixels) {
        int rows = pixels.length;
        int cols = pixels[0].length;
        if (pixels == null) {
            throw new IllegalArgumentException ("Null array");
        }
        for (int i = 1; i < rows; i++) {
            if (pixels[i].length != cols) {
                throw new IllegalArgumentException ("Jagged array");
            }
        }
       
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pixels[i][j] < 128) {
                    pixels[i][j] = 0;
                }
                else if (pixels[i][j] >= 128) {
                    pixels[i][j] = 255;
                }
            }
        }
        outputPPM(PrintWriter out,pixels);
    }
   
    /** Throws an IllegalArgumentException with the message
     * "Null array" if pixels is null
     * Throws an IllegalArgumentException with the message
     * "Invalid array" if the number of elements in row 0
     * is not a multiple of 3
     * Throws an IllegalArgumentException with the message
     * "Jagged array" if the pixels array is "jagged", i.e.,
     * each row does not have the same number of elements as
     * every other row.
     * NOTE: You must check for invalid parameters (arguments) in the order given above.
     * Converts the RGB values in the pixels array to grey scale
     */
    public static void greyScale(int[][] pixels) {
        int rows = pixels.length;
        int cols = pixels[0].length;
        if (pixels == null) {
            throw new IllegalArgumentException ("Null array");
        }
        if (pixels[0].length % 3 != 0) {
            throw new IllegalArgumentException ("Invalid array");
        }
        for (int i = 1; i < rows; i++) {
            if (pixels[i].length != cols) {
                throw new IllegalArgumentException ("Jagged array");
            }
        }
       
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j += 3) {
                int avg = (pixels[i][j] + pixels[i][j+1] + pixels[i][j+2]) / 3;
                pixels[i][j] = avg;
                pixels[i][j+1] = avg;
                pixels[i][j+2] = avg;
            }
        }
        outputPPM(PrintWriter out,pixels);
    }

    /** Throws an IllegalArgumentException with the message
     * "Null file" if out is null
     * Throws an IllegalArgumentException with the message
     * "Null array" if pixels is null
     * Throws an IllegalArgumentException with the message
     * "Invalid array" if the number of elements in row 0
     * is not a multiple of 3
     * Throws an IllegalArgumentException with the message
     * "Jagged array" if the pixels array is "jagged", i.e.,
     * each row does not have the same number of elements as
     * every other row.
     * NOTE: You must check for invalid parameters (arguments) in the order given above.
     * Outputs the following lines to out
     * Line 1: P3
     * Line 2: number of columns followed by a single space followed by the number of rows
     * Line 3: 255
     * followed by lines that contain the rows of pixels. Each row of pixels
     * must be on a separate line with one space between
     * each RGB value on the line, but no space after the last value on the line.
     */
     
    public static void outputPPM(PrintWriter out, int[][] pixels) {
        int rows = pixels.length;
        int cols = pixels[0].length;
        if (out == null) {
            throw new IllegalArgumentException ("Null file");
        }
        if (pixels == null) {
            throw new IllegalArgumentException ("Null array");
        }
        if (pixels[0].length % 3 != 0) {
            throw new IllegalArgumentException ("Invalid array");
        }
        for (int i = 1; i < rows; i++) {
            if (pixels[i].length != cols) {
                throw new IllegalArgumentException ("Jagged array");
            }
        }
        output.println("P3");
        output.println(rows + " " + (cols/3));
        output.println("255");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (j + 1 < cols) {
                    output.print(pixels[i][j] + " ");
                }
            }
            output.println();
        }
        output.close();
    }
}