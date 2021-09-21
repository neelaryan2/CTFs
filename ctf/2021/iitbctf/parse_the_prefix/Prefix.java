import java.util.*;

class Prefix
{  
    public static void main (String args[])
    {  
        // the baseUnit defined in the new language
        String baseUnit = "metre";

        // the collection of all possible units formed by adding prefixes
        List<String> units = new ArrayList<String>();
        units.add(baseUnit);

        for (char i = 'a' ; i <= 'z' ; i++) {
            for (int j = 1 ; j <= 1000 ; j++) {
                String prefix = "";
                prefix += i;
                prefix += j;
                // concat as it is
                units.add(prefix + baseUnit);

            }
        }

        // taking user input
        Scanner sc=new Scanner(System.in);  
        System.out.print("Enter a quantity which can be parsed in more than 1 way: ");  
        String inp= sc.nextLine();
        inp = inp.replaceAll("\\s", "");
        // represents the number of ways in which the given quantity can be parsed
        int cnt = 0;

        for (int i = 1 ; i < inp.length(); i++) {
            String numericValue = inp.substring(0 , i);
            String unitValue = inp.substring(i);
            System.out.println(numericValue);
            System.out.println(unitValue);

            if (units.contains(unitValue)) {
                try {
                    double doubleValue = Double.parseDouble(numericValue);
                    cnt ++;
                }
                catch (Exception e) {
                }
            }

            // if number of ways is more than 1, then return the flag
            if (cnt > 1) {
                System.out.println("Here is the flag: [REDACTED]");
                System.exit(0);
            }
        }

        System.out.println("Given Quantity cannot be parsed in more than 1 way");
    }  
}
