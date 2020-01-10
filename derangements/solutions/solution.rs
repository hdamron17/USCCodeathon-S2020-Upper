extern crate num;

use num::bigint::BigInt;
use num::{Zero, One};

fn derangements(n: u32) -> BigInt {
    (1..n+1).fold((BigInt::one(), -1),
        |(acc, correction), i| (acc*i + correction, -correction)
    ).0
}

fn tries(n: u32) -> BigInt {
    if n == 0 {
        BigInt::zero()
    } else {
        derangements(n) + 1
    }
}

fn main() {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    let n: u32 = buf.trim().parse().expect("should be valid number");
    println!("{}", tries(n));
}
