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
