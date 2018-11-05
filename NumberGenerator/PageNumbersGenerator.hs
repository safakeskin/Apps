generator :: Integer -> Integer -> Integer -> Integer -> [Integer]
generator bi ei pps p = if p >= pps then [] 
    else merge (cnctntr bi ei pps p) (generator bi ei pps (p+1) )
        where
            cnctntr :: Integer -> Integer -> Integer -> Integer -> [Integer]
            cnctntr a b c d = [ (a+d), (a+d+c*2) .. b ]

merge :: [Integer] -> [Integer] -> [Integer]
merge xs []         = xs
merge [] ys         = ys
merge xs@(x':xs') ys@(y':ys')
    | x' <= y'  = x' : merge xs' ys
    | otherwise = y' : merge xs ys' 

main :: IO ()
main = do
    putStrLn "Begin index: "
    input1 <- getLine
    putStrLn "End index: "
    input2 <- getLine
    let bi = (read input1 :: Integer)
    let ei = (read input2 :: Integer)
    putStrLn "Page per sheet: "
    input3 <- getLine
    let pps= (read input3 :: Integer)
    print (generator bi ei pps 0)
    print ((generator (bi+floor (fromIntegral pps)) ei pps 0))