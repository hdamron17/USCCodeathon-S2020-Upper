-- see https://en.wikipedia.org/wiki/Derangement#Counting_derangements
-- where it says !n = n[!(n-1)] + (-1)^n
derangements :: Integral a => [a]
derangements = scanl (\a (b,c) -> a*b+c) 1 . zip [1..] $ cycle [-1,1]

tries 0 = 0
tries n = 1 + derangements !! n
main = do
  n <- readLn :: IO Int
  print $ tries n
