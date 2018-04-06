// Useful docs:
// http://devdocs.io/openjdk~8/java/lang/string#split-java.lang.String-
// https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#split-java.lang.String-


class ReverseString {

    String reverse(String inputString) {
        String reversedString = "";
        String inputStringSplitted[] = inputString.split("");

        for(String c : inputStringSplitted){
            reversedString = c + reversedString;
        }

        return reversedString;
    }
  
}
