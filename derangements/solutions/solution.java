import java.util.Scanner;
import java.math.BigInteger;

class Solution {
  public static void main(String[] args) {
    System.out.println(tries(new Scanner(System.in).nextInt()));
  }

  static BigInteger tries(int n) {
    if (n == 0) return BigInteger.ZERO;
    return derangements(n).add(BigInteger.ONE);
  }

  static BigInteger derangements(int n) {
    BigInteger acc = BigInteger.ONE, correction = BigInteger.valueOf(-1);
    for (int i = 1; i < n + 1; ++i) {
      acc = acc.multiply(BigInteger.valueOf(i)).add(correction);
      correction = correction.negate();
    }
    return acc;
  }
}
