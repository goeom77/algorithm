import java.io.*;
import java.util.*;
class Solution {
    public String solution(String value) {
        value = value.toLowerCase();
        value = value.replaceAll("[^a-z0-9-_.]","");
;
        value = value.replaceAll("[.]{2,}",".");

        value = value.replaceAll("^[.]|[.]$","");

        if(value.isEmpty()) {
            value = "a";
        } 
        if (value.length()>=16) {
            value = value.substring(0,15);
            value = value.replaceAll("[.]$","");
        } 
        if (value.length()<=2) {
            value = value + value.substring(value.length()-1).repeat(3-value.length());
        }
        return value;
    }
}