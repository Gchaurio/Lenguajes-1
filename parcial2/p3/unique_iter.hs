module Main where

import Data.List

-- Genera todas las sublistas crecientes de una lista
-- de enteros con elementos únicos.
allIncreasingSublists :: [Int] -> [[Int]]
allIncreasingSublists [] = [[]]
allIncreasingSublists (x:xs) = [x:xs] ++ allIncreasingSublists (filter (<= x) xs)

-- Ejemplo
main :: IO ()
main = do
    putStrLn "Pon la lista pendejo\n"
    inputString <- getLine
    xs <- readList inputString
    print $ allIncreasingSublists xs